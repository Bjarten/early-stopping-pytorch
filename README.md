# early-stopping-pytorch
Early stopping is a form of regularization used to avoid overfitting on the training dataset. Early stopping keeps track of the validation loss, if the loss stops decreasing for several epochs in a row the training stops. The ```EarlyStopping``` class in ```pytorchtool.py``` is used to create an object to keep track of the validation loss while training a [PyTorch](https://pytorch.org/) model. It will save a checkpoint of the model each time the validation loss decrease.  We set the ```patience``` argument in the ```EarlyStopping``` class to how many epochs we want to wait after the last time the validation loss improved before breaking the training loop. There is a simple example of how to use the ```EarlyStopping``` class in the [MNIST_Early_Stopping_example](MNIST_Early_Stopping_example.ipynb) notebook.

Underneath is a plot from the example notebook, which shows the last checkpoint made by the EarlyStopping object, right before the model started to overfit on the MNIST. It had patience set to  20.

![Loss plot](loss_plot.png?raw=true)

### References
The ```EarlyStopping``` class in ```pytorchtool.py``` is inspired by the [ignite EarlyStopping class](https://github.com/pytorch/ignite/blob/master/ignite/handlers/early_stopping.py).
