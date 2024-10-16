# Early Stopping for PyTorch
Early stopping is a form of regularization used to avoid overfitting on the training dataset. Early stopping keeps track of the validation loss, if the loss stops decreasing for several epochs in a row the training stops. The ```EarlyStopping``` class in ```early_stopping_pytorch/early_stopping.py``` is used to create an object to keep track of the validation loss while training a [PyTorch](https://pytorch.org/) model. It will save a checkpoint of the model each time the validation loss decrease.  We set the ```patience``` argument in the ```EarlyStopping``` class to how many epochs we want to wait after the last time the validation loss improved before breaking the training loop. There is a simple example of how to use the ```EarlyStopping``` class in the [MNIST_Early_Stopping_example](MNIST_Early_Stopping_example.ipynb) notebook.

Underneath is a plot from the example notebook, which shows the last checkpoint made by the EarlyStopping object, right before the model started to overfit. It had patience set to 20.

![Loss plot](loss_plot.png?raw=true)

## Usage

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

### 5. Use the Package
You can now import and use the package in your Python code:
```python
from early_stopping_pytorch import EarlyStopping
```

---

### Summary of Commands

1. Clone the repository:
   `git clone https://github.com/your_username/early-stopping-pytorch.git`

2. Set up the environment:
   `./setup_dev_env.sh`

3. Activate the environment:
   `source dev-venv/bin/activate`

4. Install the package in editable mode:
   `pip install -e .`

5. Optional: Build the package for distribution:
   `./build.sh`

## References
The ```EarlyStopping``` class in ```early_stopping_pytorch/early_stopping.py``` is inspired by the [ignite EarlyStopping class](https://github.com/pytorch/ignite/blob/master/ignite/handlers/early_stopping.py).
