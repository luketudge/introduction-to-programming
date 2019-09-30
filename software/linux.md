# Installation on Linux

If you are using a major Linux distribution, for example a recent version of Ubuntu, then you can skip the installation of Anaconda if you wish, because your operating system will already have Python 3. This may save you some trouble, as Anaconda needs a bit of extra set-up on Linux. You can check just to be sure by opening a terminal and entering the following command (note the uppercase V):

```shell
python3 -V
```

You should see some information about your version of Python 3, if it is installed. If it is not, then you may see an error message or you may be prompted to install it.

However, Anaconda provides several extra add-ons or 'packages' for Python, including the Spyder IDE, which you will most probably not have by default on Linux. You will have to install these extras. Assuming that you are using Ubuntu, you can get them by entering the following command in the terminal:

```shell
sudo apt-get install spyder3 jupyter python3-bs4 python3-imageio python3-matplotlib python3-nltk python3-numpy python3-pandas python3-pytest python3-requests python3-sklearn
```

You will be prompted to enter your user password, and you should then see some printouts about the packages being downloaded and installed. Once complete, you should be able to find Spyder among your applications.
