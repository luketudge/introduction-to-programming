<h1>Contents<span class="tocSkip"></span></h1>
<div class="toc"><ul class="toc-item"><li><span><a href="#Windows-or-macOS" data-toc-modified-id="Windows-or-macOS-1">Windows or macOS</a></span></li><li><span><a href="#Linux" data-toc-modified-id="Linux-2">Linux</a></span></li></ul></div>

# Psychopy

Psychopy is an additional package for Python that allows you to write programs that control the screen, keyboard, mouse, etc. in order to gather psychophysical data from users/subjects. You can read more about it at the [Psychopy website](https://www.psychopy.org).

Because Psychopy needs to take some control over your computer's hardware, it is slightly more difficult to install. Because of Psychopy's special requirements, installing it can occasionally mess with the configuration of other installed Python packages. To avoid this problem, you can install Psychopy into its own 'virtual environment'. A virtual environment is a separate Python setup that stores its own configuration and versions of packages. If we install Psychopy into its own environment rather than in the main environment that you use for other Python tasks, we can minimize the risk that it may break other programs.

Follow the instructions for your operating system.

## Windows or macOS

You should first have installed Anaconda as described in the [general installation notes](install.md).

It is probably also a good idea to close any open instances of the Anaconda Navigator or Spyder. The Anaconda Navigator will probably only recognize the changes you are about to make after it has been closed and then restarted. Now search instead for an application called 'Anaconda Prompt'. This is a place where you can type in commands for Anaconda and for your computer's operating system in general.

The steps below involve typing text commands into this Anaconda Prompt. When you type the commands in the instructions below, beware that the command prompt is not particularly forgiving. If something is slightly mistyped, the prompt may tell you that a command is not found, or syntax is not correct. Check things carefully if you encounter error messages. This includes the distinction between lowercase and UPPERCASE and the accidental placement of a space in front of the command if you copy and paste it.

First you need to find out which directory on your computer the Anaconda Prompt is working in. The command prompt that appears should show which directory you are in. For example, you might see something like:

```
(base) C:\Users\mildred>
```

In this case, `C:\Users\mildred` is the directory that you are in. If you don't see anything like this, or if you are not sure which directory this points to, you can try typing in a command that will display the name of the directory. If you are on **Windows**, type `cd`. If you are on **macOS**, type `pwd`. You should then see the name of a directory printed out. Make a note of it and then go find it in your file explorer.

The makers of Psychopy provide a file that Anaconda can use to create the necessary environment for Psychopy to run in. Download the file (called *psychopy-env.yaml* from [this link](https://raw.githubusercontent.com/psychopy/psychopy/master/conda/psychopy-env.yml) and make sure you download it into the directory that you saw displayed in the Anaconda Prompt above.

Now return to the Anaconda Prompt and enter the following command (as described on the [Psychopy website](https://www.psychopy.org/download.html#anaconda-and-miniconda)):

```
conda env create -n psy -f psychopy-env.yml
```

This will create the necessary virtual environment under the name 'psy'. In order to be able to use Spyder to write Python programs in this new environment, you should also install Spyder into the 'psy' environment. Still in the Anaconda Prompt, first enter the following command:

```
conda activate psy
```

This 'activates' the new environment, so that any subsequent commands that you enter will take effect for this environment only. You should see that the prompt in the Anaconda Prompt is now prefaced with the name of the 'psy' environment. Something like this:

```
(psy) C:\Users\mildred>
```

Now you can enter a command to install Spyder, and it will be installed into this environment:

```
conda install spyder
```

When the installation has finished, you have finished setting up the environment and you can close the Anaconda Prompt window.

You will now have two environments in your Anaconda installation. One is called 'base', which is the default environment that was already created when you installed Anaconda. The other is called 'psy', and is the one in which you just installed Psychopy. When you want to write Python programs that use Psychopy, instead of launching Spyder directly, first launch an application called 'Anaconda Navigator'. This is the main graphical interface to Anaconda. In here, you can see a list of your environments under the 'Environments' tab. From the list of environments, click on 'psy' to activate the 'psy' environment. Once you have done so, find Spyder among the applications listed there, and click on 'Launch' to launch Spyder in the 'psy' environment.

## Linux

You will need first to install a Python program for creating virtual environments. It is called 'virtualenv' and you can get it via your normal package manager. Make sure that you get the Python 3 version. Assuming you are on Ubuntu, the following command in the terminal will install it:

```shell
sudo apt-get install python3-virtualenv
```

Once you have installed virtualenv, you can use it as a command in the terminal to create virtual environments. First use `cd` to navigate into the directory where you would like to store your virtual environment (or just open the terminal there by right-clicking on the directory in the file explorer and selecting 'Open in Terminal'). Then enter the following command to create a virtual environment in which to install Psychopy:

```shell
virtualenv --python /usr/bin/python3 psy
```

The `--python` option with the path to the Python 3 interpreter `/usr/bin/python3` ensures that the environment will be a Python 3 environment and not Python 2. And 'psy' is the name of the environment.

(Note that it is generally not a good idea to call your virtual environment by the same name as a Python package, as Python may then try to import the contents of the virtual environment whenever you instruct it to import the package with the same name. This is why you should opt for a name other than 'psychopy' for your virtual environment.)

Still in the terminal, enter the following command to activate the virtual environment:

```shell
source psy/bin/activate
```

This runs a short file in the virtual environment directory that makes subsequent commands in that terminal session take effect in that environment only.

Now use the Python package manager program (pip) to install Psychopy. If you want to write your Psychopy programs using Spyder, you should also install Spyder into the new environment:

```shell
pip install psychopy spyder
```

Finally, to launch Spyder in the new environment, just enter the following command:

```shell
spyder3
```

To quit the virtual environment, you can just close the terminal window. Whenever you want to write Python programs that make use of Psychopy, just open the terminal in the directory where you created the virtual environment and enter the command to activate it, followed by the command to launch Spyder:

```shell
source psy/bin/activate
spyder3
```

The directory 'psy' that contains the files for the virtual environment is a directory like any other. If you ever want to delete your virtual environment, just delete the 'psy' directory. And if you want to move it somewhere else in your file system, just move the 'psy' directory.

Some more information about virtual environments is provided at the [Hitchhiker's Guide to Python](https://docs.python-guide.org/dev/virtualenvs/#basic-usage).
