# Spyder configuration

In order to avoid some common difficulties, you should change two important options within Spyder. Start up Spyder. Go to the **Tools** menu and select **Preferences**. You should change a few of the preferences.

## Running programs

![](images/spyder.png)

Under the section **Run**, make sure that the option **Remove all variables before execution** is selected, and that the section **Default working directory is:** is set to **The directory of the file being executed**. Click **Apply** to make these options take effect. Together, these options ensure that each Python program that we run will start from a clean slate in its own directory and will not be affected by the actions carried out by a previous program or by files contained in some other directory. This is important because we want our programs to work for anyone, and not be dependent on other actions that we have taken before running the program or on the contents of our home folder.

![](images/spyder_run.png)

## Default working directory

Second, outside of Spyder create for yourself a new directory somewhere on your computer. This is the directory where you will save all your notes for the class, and where you will save any extra files that we work with during the class demonstrations. Now return to the **Preferences** window in Spyder and under the section **Current working directory** select **the following directory** and click the button on the right to navigate to the directory that you just created. Again, click **Apply** once you have done this. This sets the default directory that Spyder will look in when it launches. As long as you save the course materials in this directory, you will be able to find them easily from Spyder. If you now close and restart Spyder you should see that the path to the directory you chose now appears at the top right of the Spyder window.

![](images/spyder_directory.png)

It is totally fine to create subdirectories within this directory if you would like to organize your notes more neatly. But just remember that each program you write must be stored in the same subdirectory as any additional files that that program requires in order to run. So for example if you write a program called *amazing_machine_learning.py* and this program reads data from a file called *really_big_data.db*, then these two files must be located in the same directory in order for your program to work.

## Variable explorer

Finally, under the section **Variable explorer**, make sure that the options **Exclude capitalized references**, **Exclude all-uppercase references**, and **Exclude unsupported data types** are all *unselected*. Again, click **Apply** once you have unselected them.

![](images/spyder_variable_explorer.png)

This option is less important, but it ensures that when you use Spyder to explore the contents of Python's 'memory', it will show you all the relevant contents, and won't hide from you things that might be important.
