# Software

To get the most out of the class, you should have some software installed on your own computer so that you can try out the exercises at home.

The instructions provided here assume that the operating system for your computer is either Windows or macOS. If instead of Windows or macOS you are using a popular distribution of Linux such as Ubuntu, follow the [instructions for Linux](linux.md) instead.

## Essentials

### Python 3

The main programming language that we will learn about is Python 3. You will need to install it.

The easiest way to get Python 3 on the most common operating systems (Windows and macOS), is to install a program called Anaconda. Anaconda is a 'distribution' of various related pieces of software used in data science. Anaconda installs these separate pieces of software and provides a convenient environment in which to organize, update, and add to them.

Download the installer for the Python 3 version of Anaconda [here](https://www.anaconda.com/distribution/). The page should detect your operating system automatically, but otherwise click on the relevant tab for Windows or macOS. Additional installation instructions can be found [here](https://docs.anaconda.com/anaconda/install/). If you encounter problems during or after installation, there is some help provided [here](https://docs.anaconda.com/anaconda/user-guide/troubleshooting/).

One thing that can occasionally cause problems for Anaconda is the name of the user account on your computer. If your username contains non-English characters (for example *ä* or *ß* or something in Arabic, or Devanagari, etc.), or if it simply contains spaces (for example 'Mildred Bonk' instead of 'Mildred.Bonk' or 'Mildred_Bonk'), then Anaconda may have trouble understanding which directory your files are stored in. If you encounter error messages about paths or filenames, you could try creating a new user account on your computer with a username that contains only basic English characters and no spaces. Switch to this account before installing and running Anaconda.

Be careful not to download and install Python 2. There are some important differences between Python 2 and 3. At a few points during the class we will note some of these differences just so that you are aware of them. But all of the example programs that we write will be for Python 3, and some may not even work correctly with Python 2.

### Spyder

Python programs are just text files, so we can (and occasionally will) create them in a normal text editor. But this is tedious. An alternative is to use an 'Integrated Development Environment' (IDE). An IDE is like a text editor specifically designed for writing computer programs, and provides many useful extra features such as automatically checking for mistakes in the program, and allowing us to run our program immediately to check whether it functions correctly.

There are many IDEs available for Python. For beginners I recommend [Spyder](https://www.spyder-ide.org/). Spyder is included by default in Anaconda, so if you have installed Anaconda you do not need to do anything more in order to get it. The user guide for Anaconda [here](https://docs.anaconda.com/anaconda/user-guide/getting-started/) shows how to launch Spyder from Anaconda.

Once you have launched Spyder, there are a few *highly* [recommended configuration steps](spyder.md) that you should carry out in order to be able to follow the class smoothly.

## Alternatives

If you have trouble installing the software as described above, you can instead opt to write and run your Python programs entirely online. [Python Anywhere](https://www.pythonanywhere.com/) is a website that provides online storage for your Python programs, along with a helpful text editor and the ability to run your programs in the browser. Sign up for a free account, log in, and visit the 'Files' tab to edit your programs or create new ones.

## Extras

There are a few tools that are useful just for one or two of the topics. Installing these is optional, and you can wait until we get to the relevant topic to decide whether you want to install them.

### GitHub

GitHub is a platform that allows you to store and publish computer programs. It provides a lot of useful tools for tracking changes to your programs and collaborating with other developers. When we come to learn about GitHub, if you want to follow along you will need your own GitHub account. It is free and you can sign up [here](https://github.com/join).

You can interact with GitHub directly in your web browser, and this is the simplest option if you would just like to get started and try it out. If you want to go further, then you can also download some software that allows you to interact with GitHub from your desktop.

Here are a couple of options:

#### Atom

Atom is a text editor produced by the developers of GitHub. Among many other things, it allows you to edit text files (for example Python programs) and send the changes straight to GitHub. You can download it [here](https://flight-manual.atom.io/getting-started/sections/installing-atom/).

#### GitHub Desktop

If you decide you don't like the look of Atom or can't get it to work on your computer, a good alternative for Windows or macOS users is GitHub Desktop. Like Atom, it synchronizes files on your computer with the same files stored on GitHub. You can download it [here](https://desktop.github.com/).

### Database browser

When we come to work with SQL and relational databases, it will be convenient to have a program that can display the contents of a database. The DB Browser for SQLite is a simple program for viewing and editing databases. You can download it [here](https://sqlitebrowser.org/dl/).
