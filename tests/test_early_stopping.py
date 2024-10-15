# test_early_stopping.py

import pytest
from unittest.mock import Mock, patch
import torch
import numpy as np

from pytorchtools import EarlyStopping

# Fixtures to mock model and temporary checkpoint path

@pytest.fixture
def mock_model():
    """
    Fixture to create a mock PyTorch model.

    Returns:
        Mock: A mocked PyTorch model with a predefined state_dict.
    """
    model = Mock(spec=torch.nn.Module)
    model.state_dict.return_value = {'param': 'value'}
    return model

@pytest.fixture
def temp_checkpoint_path(tmp_path):
    """
    Fixture to create a temporary checkpoint file path.

    Args:
        tmp_path (Path): Pytest's built-in fixture providing a temporary directory.

    Returns:
        str: String representation of the temporary checkpoint file path.
    """
    checkpoint_file = tmp_path / "checkpoint.pt"
    return str(checkpoint_file)

# Tests

def test_initialization():
    """
    Test the initialization of the EarlyStopping class to ensure all attributes are set correctly.

    This test verifies that upon instantiation, the EarlyStopping object has its parameters and internal
    counters initialized as expected.
    """
    # Initialize EarlyStopping with specific parameters
    early_stopping = EarlyStopping(patience=5, verbose=True, delta=0.01)

    # Assert that all attributes are correctly initialized
    assert early_stopping.patience == 5, "Patience should be set to 5"
    assert early_stopping.verbose is True, "Verbose should be True"
    assert early_stopping.delta == 0.01, "Delta should be set to 0.01"
    assert early_stopping.counter == 0, "Counter should be initialized to 0"
    assert early_stopping.best_val_loss is None, "Best score should be None initially"
    assert early_stopping.early_stop is False, "Early stop flag should be False initially"
    assert early_stopping.val_loss_min == np.inf, "Initial val_loss_min should be infinity"

def test_initial_call_saves_checkpoint(mock_model, temp_checkpoint_path):
    """
    Test that the initial call to EarlyStopping saves the model checkpoint and updates best_val_loss.

    This test ensures that when EarlyStopping is called for the first time with a validation loss,
    it correctly saves the model's state_dict and updates the best_val_loss accordingly.

    Args:
        mock_model (Mock): A mocked PyTorch model.
        temp_checkpoint_path (str): Temporary file path for saving the checkpoint.
    """
    # Patch the torch.save method used inside EarlyStopping to prevent actual file I/O
    with patch('pytorchtools.torch.save') as mock_save:
        # Initialize EarlyStopping with specified parameters
        early_stopping = EarlyStopping(patience=5, verbose=False, path=temp_checkpoint_path)

        # Simulate the first validation loss
        initial_val_loss = 1.0
        early_stopping(initial_val_loss, mock_model)

        # Assert that model.state_dict() was called once
        mock_model.state_dict.assert_called_once_with()
        # Assert that torch.save was called once with correct arguments
        mock_save.assert_called_once_with(mock_model.state_dict(), temp_checkpoint_path)
        # Assert that best_val_loss was set correctly
        assert early_stopping.best_val_loss == initial_val_loss, "Best score should be set to negative initial_val_loss"
        # Assert that early_stop is not triggered
        assert not early_stopping.early_stop, "Early stop should not be triggered on initial call"

def test_validation_loss_improves(mock_model, temp_checkpoint_path):
    """
    Test that validation loss improvements trigger checkpoint saving and reset the patience counter.

    This test simulates a sequence of validation losses that consistently improve. It verifies that
    EarlyStopping saves the model checkpoint each time an improvement is detected and that the
    patience counter remains at zero, indicating no need to stop early.

    Args:
        mock_model (Mock): A mocked PyTorch model.
        temp_checkpoint_path (str): Temporary file path for saving the checkpoint.
    """
    # Patch the torch.save method used inside EarlyStopping
    with patch('pytorchtools.torch.save') as mock_save:
        # Initialize EarlyStopping with specified parameters
        early_stopping = EarlyStopping(patience=5, verbose=False, path=temp_checkpoint_path)

        # Simulate a series of improving validation losses
        losses = [1.0, 0.9, 0.8, 0.85, 0.75]
        for loss in losses:
            early_stopping(loss, mock_model)

        # Assert that torch.save was called once for the initial loss and three times for improvements
        assert mock_save.call_count == 4, "Checkpoints should be saved on initial and 3 improvements"
        # Assert that the patience counter remains at 0 after each improvement
        assert early_stopping.counter == 0, "Counter should be reset to 0 after improvements"
        # Assert that early stopping was not triggered
        assert not early_stopping.early_stop, "Early stop should not be triggered when losses improve"

def test_validation_loss_no_improvement_within_delta(mock_model, temp_checkpoint_path):
    """
    Test that the patience counter increments when validation loss does not improve beyond delta.

    This test simulates a scenario where validation losses do not improve sufficiently (i.e., the
    improvement is less than the specified delta). It verifies that the patience counter increments
    correctly and that early stopping is triggered once the patience threshold is exceeded.

    Args:
        mock_model (Mock): A mocked PyTorch model.
        temp_checkpoint_path (str): Temporary file path for saving the checkpoint.
    """
    # Patch the save_checkpoint method to monitor its calls directly
    with patch.object(EarlyStopping, 'save_checkpoint') as mock_save_checkpoint:
        # Initialize EarlyStopping with specified parameters
        early_stopping = EarlyStopping(
            patience=3,           # Number of epochs to wait for improvement
            verbose=False,        # Disable verbose output
            delta=0.01,           # Minimum improvement to qualify as an improvement
            path=temp_checkpoint_path  # Path to save the checkpoint
        )

        # First sequence of validation losses with sufficient improvements
        initial_losses = [1.0, 0.98, 0.97, 0.97, 0.95, 0.95]
        for loss in initial_losses:
            early_stopping(loss, mock_model)

        # After processing initial_losses:
        # - Checkpoints should be saved on initial call and on each improvement (Epochs 1, 2, 3, 5)
        # - Total save_checkpoint calls: 2
        # - Patience counter should have incremented to 1 (from Epoch 6)
        # - Early stopping should not have been triggered yet

        # Assert that save_checkpoint was called three times: initial call and three improvements
        assert mock_save_checkpoint.call_count == 3, "Checkpoints should be saved on initial and three improvements"

        # Assert that the patience counter has incremented to 1 (only Epoch 6 incremented it)
        assert early_stopping.counter == 1, "Counter should be incremented to 1"

        # Assert that early stopping has not been triggered yet
        assert early_stopping.early_stop is False, "Early stop should not be triggered yet"

        # Second sequence of validation losses that do not improve beyond delta
        worsening_losses = [1.0, 1.1]
        for loss in worsening_losses:
            early_stopping(loss, mock_model)

        # After processing worsening_losses:
        # - No checkpoints should be saved since losses are worsening
        # - Patience counter should increment by 2 (from 1 to 3)
        # - Early stopping should be triggered as patience is exceeded

        # Assert that save_checkpoint was still called three times (no new saves)
        assert mock_save_checkpoint.call_count == 3, "No additional checkpoints should be saved as losses worsen"

        # Assert that the patience counter has incremented to 3
        assert early_stopping.counter == 3, "Counter should be incremented to 3"

        # Assert that early stopping was triggered after patience was exceeded
        assert early_stopping.early_stop is True, "Early stop should be triggered after patience is exceeded"


def test_early_stopping_triggered(mock_model, temp_checkpoint_path):
    """
    Test that early stopping is triggered when the patience is exceeded without sufficient improvement.

    This test verifies that when the validation loss does not improve for a number of consecutive epochs
    equal to the patience parameter, EarlyStopping sets the early_stop flag to True, indicating that
    training should cease.

    Args:
        mock_model (Mock): A mocked PyTorch model.
        temp_checkpoint_path (str): Temporary file path for saving the checkpoint.
    """
    # Patch the save_checkpoint method used inside EarlyStopping to monitor its calls directly
    with patch.object(EarlyStopping, 'save_checkpoint') as mock_save_checkpoint:
        # Initialize EarlyStopping with specified parameters
        early_stopping = EarlyStopping(
            patience=2,           # Number of epochs to wait for improvement
            verbose=True,         # Enable verbose output to observe messages
            path=temp_checkpoint_path  # Path to save the checkpoint
        )

        # Simulate validation losses with no improvement after two patience steps
        losses = [1.0, 0.9, 0.85, 0.85, 0.85]
        for loss in losses:
            early_stopping(loss, mock_model)

        # After processing losses:
        # - Checkpoints should be saved on initial call and on each improvement (Epochs 1, 2, 3)
        # - Total save_checkpoint calls: 3
        # - Patience counter should have incremented to 2 (from Epochs 4 and 5)
        # - Early stopping should be triggered

        # Assert that save_checkpoint was called three times: initial call and two improvements
        assert mock_save_checkpoint.call_count == 3, "Checkpoints should be saved on initial and two improvements"

        # Assert that the patience counter has incremented to 2 (from Epochs 4 and 5)
        assert early_stopping.counter == 2, "Counter should be incremented to 2"

        # Assert that early stopping was triggered after patience was exceeded
        assert early_stopping.early_stop is True, "Early stop should be triggered after patience is exceeded"

def test_verbose_output(mock_model, temp_checkpoint_path, capsys):
    """
    Test that verbose outputs are printed correctly when verbose is enabled.

    This test checks that when the verbose parameter is set to True, EarlyStopping prints
    informative messages about validation loss improvements and patience counter increments.

    Args:
        mock_model (Mock): A mocked PyTorch model.
        temp_checkpoint_path (str): Temporary file path for saving the checkpoint.
        capsys: Pytest fixture to capture output to stdout and stderr.
    """
    # Patch the torch.save method used inside EarlyStopping to prevent actual file I/O
    with patch('pytorchtools.torch.save'):
        # Initialize EarlyStopping with verbose enabled
        early_stopping = EarlyStopping(patience=2, verbose=True, path=temp_checkpoint_path)

        # Simulate validation losses with and without improvement
        losses = [1.0, 0.95, 0.95, 0.95]
        for loss in losses:
            early_stopping(loss, mock_model)

        # Capture the output printed by the trace_func
        captured = capsys.readouterr()
        # Check that verbose messages for validation loss decrease are printed
        assert 'Validation loss decreased' in captured.out, "Should print validation loss decrease message"
        # Check that verbose messages for counter increments are printed
        assert 'EarlyStopping counter: 1 out of 2' in captured.out, "Should print first counter increment"
        assert 'EarlyStopping counter: 2 out of 2' in captured.out, "Should print second counter increment"


def test_no_early_stop_when_validation_improves_within_patience(mock_model, temp_checkpoint_path):
    """
    Test that early stopping is not triggered when validation loss continues to improve within patience.

    This test ensures that as long as validation loss keeps improving (even intermittently), the
    patience counter does not reach the threshold, and early stopping is not triggered.

    Args:
        mock_model (Mock): A mocked PyTorch model.
        temp_checkpoint_path (str): Temporary file path for saving the checkpoint.
    """
    # Patch the torch.save method used inside EarlyStopping
    with patch('pytorchtools.torch.save') as mock_save:
        # Initialize EarlyStopping with specified parameters
        early_stopping = EarlyStopping(patience=3, verbose=False, path=temp_checkpoint_path)

        # Simulate validation losses with intermittent improvements
        losses = [1.0, 0.95, 0.90, 0.85, 0.80, 0.85, 0.80, 0.75]
        for loss in losses:
            early_stopping(loss, mock_model)

        # Assert that torch.save was called on initial and four improvements
        assert mock_save.call_count == 6, "Checkpoints should be saved on initial and five improvements"
        # Assert that the patience counter is reset to 0 after each improvement
        assert early_stopping.counter == 0, "Counter should be reset to 0 after each improvement"
        # Assert that early stopping was not triggered
        assert not early_stopping.early_stop, "Early stop should not be triggered when validations continue to improve within patience"

def test_delta_functionality(mock_model, temp_checkpoint_path):
    """
    Test that the delta parameter correctly influences the checkpoint saving behavior.

    This test verifies that when the improvement in validation loss exceeds the delta threshold,
    EarlyStopping saves the model checkpoint and resets the patience counter. However, once early stopping is
    triggered, the early_stop flag remains True even after a significant improvement.

    Args:
        mock_model (Mock): A mocked PyTorch model.
        temp_checkpoint_path (str): Temporary file path for saving the checkpoint.
    """
    # Patch the save_checkpoint method of EarlyStopping to monitor its calls directly
    with patch.object(EarlyStopping, 'save_checkpoint') as mock_save_checkpoint:
        # Ensure that the mocked model's state_dict returns a valid state
        mock_model.state_dict.return_value = {'layer1.weight': torch.tensor([1, 2, 3])}

        # Initialize EarlyStopping with delta set to 0.1
        early_stopping = EarlyStopping(
            patience=3,                 # Number of epochs to wait for improvement
            verbose=False,              # Disable verbose output
            delta=0.1,                  # Minimum improvement to qualify as an improvement
            path=temp_checkpoint_path    # Path to save the checkpoint
        )

        # Simulate validation losses with varying improvements
        losses = [1.0, 0.95, 0.91, 0.9, 0.79]
        for loss in losses:
            early_stopping(loss, mock_model)

        # Expected behavior:
        # Initial loss: 1.0 (save)
        # 0.95: improvement of 0.05 (less than delta=0.1) -> no save, counter=1
        # 0.91: improvement of 0.04 (less than delta=0.1) -> no save, counter=2
        # 0.9: improvement of 0.01 (less than delta=0.1) -> no save, counter=3
        # 0.79: improvement of 0.11 (larger than delta=0.1) -> save, counter reset to 0, but early_stop still True

        # Assert that save_checkpoint was called on initial and final significant improvement
        assert mock_save_checkpoint.call_count == 2, "Checkpoints should be saved on initial and final significant improvements (delta=0.1)"

        # Assert that the patience counter was reset after the final improvement
        assert early_stopping.counter == 0, "Counter should be reset after significant improvements"

        # Simulate further validation losses that do not improve beyond delta
        worsening_losses = [0.8, 1.1]
        for loss in worsening_losses:
            early_stopping(loss, mock_model)

        # Since early stop was already triggered earlier, it should remain True
        assert early_stopping.early_stop, "Early stop should remain True after it was triggered"

        # Assert no new checkpoints were saved after early stopping was triggered
        assert mock_save_checkpoint.call_count == 2, "No additional checkpoints should be saved after early stopping was triggered"


