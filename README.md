# Early Stopping for PyTorch
Early stopping is a form of regularization used to avoid overfitting on the training dataset. Early stopping keeps track of the validation loss, if the loss stops decreasing for several epochs in a row the training stops. The ```EarlyStopping``` class in ```early_stopping_pytorch/early_stopping.py``` is used to create an object to keep track of the validation loss while training a [PyTorch](https://pytorch.org/) model. It will save a checkpoint of the model each time the validation loss decrease.  We set the ```patience``` argument in the ```EarlyStopping``` class to how many epochs we want to wait after the last time the validation loss improved before breaking the training loop. There is a simple example of how to use the ```EarlyStopping``` class in the [MNIST_Early_Stopping_example](MNIST_Early_Stopping_example.ipynb) notebook.

Underneath is a plot from the example notebook, which shows the last checkpoint made by the EarlyStopping object, right before the model started to overfit. It had patience set to 20.

![Loss Plot](https://raw.githubusercontent.com/Bjarten/early-stopping-pytorch/main/loss_plot.png)

## Installation

### Option 1: Install from PyPI (Recommended)
```bash
pip install early-stopping-pytorch
```

### Option 2: Install from Source
For development or if you want the latest unreleased changes:

### 1. Clone the Repository
```bash
git clone https://github.com/your_username/early-stopping-pytorch.git
cd early-stopping-pytorch
```

### 2. Set Up the Virtual Environment
Run the setup script to create a virtual environment and install all necessary dependencies.
```bash
./setup_dev_env.sh
```

### 3. Activate the Virtual Environment
Activate the virtual environment:
```bash
source dev-venv/bin/activate
```

### 4. Install the Package in Editable Mode
Install the package locally in editable mode so you can use it immediately:
```bash
pip install -e .
```

## Usage

```python
from early_stopping_pytorch import EarlyStopping

# Initialize early stopping object
early_stopping = EarlyStopping(patience=7, verbose=True)

# In your training loop:
for epoch in range(num_epochs):
    # ... training code ...
    val_loss = ... # calculate validation loss

    # Early stopping call
    early_stopping(val_loss, model)
    if early_stopping.early_stop:
        print("Early stopping triggered")
        break
```

For a complete example, see the [MNIST Early Stopping Example Notebook](MNIST_Early_Stopping_example.ipynb).

## Citation

If you find this package useful in your research, please consider citing it as:

```bibtex
@misc{early_stopping_pytorch,
  author = {Bjarte Mehus Sunde},
  title = {early-stopping-pytorch: A PyTorch utility package for Early Stopping},
  year = {2024},
  url = {https://github.com/Bjarten/early-stopping-pytorch},
}
```

## References
The ```EarlyStopping``` class in ```early_stopping_pytorch/early_stopping.py``` is inspired by the [ignite EarlyStopping class](https://github.com/pytorch/ignite/blob/master/ignite/handlers/early_stopping.py).
