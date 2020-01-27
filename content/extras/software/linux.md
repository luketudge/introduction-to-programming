# Installation on Linux

If you are using a major Linux distribution, for example a recent version of Ubuntu, Python 3 will already be installed on your computer. You can check just to be sure by opening a terminal and entering the following command:

```shell
python3 --version
```

You should see some information about your version of Python 3, if it is installed. If it is not, then you may see an error message or you may be prompted to install it.

However, we will also use several extra 'packages' for Python, including a program called Spyder, which you will most probably not have by default on Linux. You will have to install these. You can install these via your normal package manager. Assuming that you are using Ubuntu, you can get them by entering the following command in the terminal:

```shell
sudo apt-get install python3-bs4 python3-imageio python3-matplotlib python3-nltk python3-numpy python3-pandas python3-pytest python3-requests python3-seaborn python3-sklearn spyder3
```

You will be prompted to enter your user password, and you should then see some printouts about the packages being downloaded and installed.

Once you have finished installing these extras, you should be able to find Spyder among your applications. Once you have launched Spyder, follow the [recommended configuration steps](spyder.md).
