<h1>Contents<span class="tocSkip"></span></h1>
<div class="toc"><ul class="toc-item"><li><span><a href="#Imports" data-toc-modified-id="Imports-1">Imports</a></span><ul class="toc-item"><li><span><a href="#Debugging" data-toc-modified-id="Debugging-1.1">Debugging</a></span></li><li><span><a href="#Namespaces" data-toc-modified-id="Namespaces-1.2">Namespaces</a></span></li><li><span><a href="#Star-imports" data-toc-modified-id="Star-imports-1.3">Star imports</a></span></li><li><span><a href="#Selective-imports" data-toc-modified-id="Selective-imports-1.4">Selective imports</a></span></li></ul></li><li><span><a href="#Methods-revisited" data-toc-modified-id="Methods-revisited-2">Methods revisited</a></span></li><li><span><a href="#Special-names" data-toc-modified-id="Special-names-3">Special names</a></span><ul class="toc-item"><li><span><a href="#Special-variables" data-toc-modified-id="Special-variables-3.1">Special variables</a></span></li><li><span><a href="#Special-methods" data-toc-modified-id="Special-methods-3.2">Special methods</a></span></li></ul></li><li><span><a href="#Exercise" data-toc-modified-id="Exercise-4">Exercise</a></span><ul class="toc-item"><li><span><a href="#1" data-toc-modified-id="1-4.1">1</a></span></li><li><span><a href="#2" data-toc-modified-id="2-4.2">2</a></span></li></ul></li></ul></div>

# Modules

In the [previous lesson](functions.md) we learned how to define our own [functions](extras/glossary.md#function). I mentioned the possibility of re-using functions in a different file from the file in which the functions are defined. This is the main thing that we will learn about in this lesson.

You may reasonably ask why we would want to do this. If we are writing a program that requires one or more custom-defined functions, why not just define them in the same file that contains the program in which they are used? After all, this simpler one-file structure is the way that the [fun_facts.py](examples/fun_facts.py) example program is organized, and that program was written by a well-respected expert programmer.

For a simple program like *fun_facts.py*, a single file is fine, and is even a good idea. Multiple files are unnecessary for simple, short programs. But for more complex programs, separating functions off from the rest of the program has some advantages:

* **Clarity**. The functions file shows the algorithmic workings of each component of the program, but the main program file shows how those components are combined to create the overall program structure. We know which file to go to if we want to change either the overall structure or the details of the program.
* **Portability**. A file that contains only functions can be re-used by a different program. The alternative, copying and pasting the function definition into every program file that needs it, is prone to mistakes and makes our programs inflexible ('[DRY](https://en.wikipedia.org/wiki/Don't_repeat_yourself)').

A Python file that contains an actual program that will 'do something' when run is often termed a [script](extras/glossary.md#script), because it is providing the Python [interpreter](extras/glossary.md#interpreter) with line-by-line instructions telling it what to do, like the script for an actor. A file that instead contains only function definitions (and possibly also some variables) intended to be used elsewhere is often termed a [module](extras/glossary.md#module). A basic structure for a simple multi-file Python program is to have one module file providing some functions, along with a script file (the 'main' file) that gets those functions and actually does something with them.

Let's see how this works, using the [initials.py](examples/initials.py) file that we saw in the previous lesson. Take a look at the example program [ids.py](examples/ids.py). This program makes use of the `get_initials()` function that is defined in *initials.py*.

## Imports

We can almost already create a multi-file program given what we have learned so far, and there is very little in *ids.py* that is unfamiliar. We know how to use functions, and we know how to use additional [control statements](extras/glossary.md#control) to determine what actions are taken when, how often, and so on.

The only new ingredient is how to 'get' the contents of one file into another. This is fairly easy. The [keyword](extras/glossary.md#keyword) `import` runs another Python file and then makes its contents (i.e. any functions or variables that were created in the course of running it) available in the current file. The [syntax](extras/glossary.md#syntax) for importing the contents of a file is simply to write `import` followed by the name of the file, without the *.py* file extension.

So this is how we can import the contents of *initials.py* file into another Python file:


```python
import initials
```

We can see this command on [line 12](examples/ids.py#L12) of *ids.py*.

### Debugging

Note that in order for an `import` statement to work, the file that we are importing must be located in the directory that we are working in. This means the directory in which our main program file is saved. So if you are writing your own example program in the Spyder editor to test the example commands as we go along, make sure that your copy of *initials.py* is located in the same directory in which you have saved your example program.

If we try to import a module file that does not exist or is not in the current directory, we get an error:


```python
import nonexistent_module
```


    ---------------------------------------------------------------------------

    ModuleNotFoundError                       Traceback (most recent call last)

    <ipython-input-3-696f280e00ee> in <module>
    ----> 1 import nonexistent_module
    

    ModuleNotFoundError: No module named 'nonexistent_module'


Note also that module filenames should not contain any spaces. Otherwise when we try to import them, Python sees something that looks like two or more separate names, and this is not valid Python [syntax](extras/glossary.md#syntax):


```python
import badly named module
```


      File "<ipython-input-4-5524f6874f05>", line 1
        import badly named module
                         ^
    SyntaxError: invalid syntax



### Namespaces

I promised that after [importing](extras/glossary.md#import) our *initials.py* file, the function that it defines would be available for us to use. This doesn't seem to be the case. *initials.py* contains a function called `get_initials()`, but this function still doesn't seem to be available:


```python
get_initials('Mildred Bonk')
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-5-c5a44f04dc80> in <module>
    ----> 1 get_initials('Mildred Bonk')
    

    NameError: name 'get_initials' is not defined


There is just one more missing ingredient (I really promise this time, only one more). Instead of just taking everything from the imported file and putting it all into individual variables that we can use in the normal way, Python's `import` puts all the imported contents into their own '[namespace](extras/glossary.md#namespace)'. A namespace is a bit like a directory for variables. It stores multiple variables all under the same name, for neatness of organization. We can access individual variables within a namespace by writing first the name of the namespace (which here is simply the name of the imported module), followed by a dot `.`, like this:


```python
initials.get_initials('Mildred Bonk')
```




    'mb'



This is what we see on [lines 20 and 21](examples/ids.py#L20) of *ids.py*, where the `get_initials()` function from *initials.py* is first used.

Isn't this just an annoying extra complexity, another chance to get something wrong when we write our programs? Like many such things, Python's use of namespaces appears an annoyance at first but is really a blessing in disguise once we start writing more complex programs.

Imagine that you have a very long program containing a lot of variables. And then you decide that you want to import into this program a very useful but also very long [module](extras/glossary.md#module) that provides some great functions that you need. If `import` simply dumped everything from both files together in the same workspace, then you would need to first check carefully and make sure that none of the names of variables or functions in one file were the same as those in the other, because if they were, the names would 'clash' and one would overwrite the other. By keeping imported things in a separate namespace, such accidental overwrites are avoided. It is entirely possible to import a module (for example called *my_module.py*) containing a function or variable called `x` and also to have something called `x` in your main program. The former will be available as `my_module.x` whereas the latter will be available simply as `x`.

Likewise, imagine that you need to import functions from more than one module. Again, if these modules unfortunately happen to contain functions with the same name, they would overwrite each other if simply dumped into the main workspace. But thanks to namespaces, clashing function names are totally fine; one function can be available as, for example, `module_a.useful_function()` and the other as `module_b.useful_function()`.

### Star imports

If we really want to, it is possible to bypass `import`'s creation of separate namespaces for imported modules. The [keyword](extras/glossary.md#keyword) `from`, together with the `*` symbol, imports everything from a module into the main workspace of the current program:


```python
from initials import *
```

And now the contents of *initials.py* are available in the normal way without prepending `initials.`:


```python
get_initials('Mildred Bonk')
```




    'mb'



This is sometimes termed a 'star import', because of the use of the 'star' symbol `*` (you may also see it called a '[wildcard](extras/glossary.md#wildcard)'). In many contexts in programming, the `*` symbol stands for 'everything' or 'anything'. So the command above says 'import everything from *initials.py* (and dump it all into the main workspace)'.

The star import shortcut is there if you really need it, but the general consensus among Python users is that it is not a good idea. It erases all the benefits that namespaces bring for the robustness and clarity of our program. My advice is to reserve it only for very short programs that only import one module, and whose purpose is simply to demonstrate the use of that one module.

You will sometimes see star imports used in online examples or documentation, to help keep an example short ([here](https://plotnine.readthedocs.io/en/stable/generated/plotnine.geoms.geom_bar.html#examples) is one example). This is fine for examples and demonstrations, but don't copy it into your own programs.

### Selective imports

A better use of the `from` keyword is to select just one thing that we would like to import from a module. For example, we can import just the `get_initials()` function from *initials.py* (admittedly, this is somewhat redundant here, since `get_initials()` is the only thing in *initials.py* anyway):


```python
from initials import get_initials
```

A 'selective import' like this also makes the individual function `get_initials()` available directly without having to use a namespace.


```python
get_initials('Mildred Bonk')
```




    'mb'



But note that there is a big difference in clarity when compared to the star import. A selective `import` statement at least says explicitly *what* we are importing from the module. So if we begin our main program with `from initials import get_initials`, we and our collaborators can at least be sure when reading the remainder of the program that `get_initials()` refers to something that we have imported from *initials.py* (and that we haven't imported anything else from there). By contrast, with the star import no part of our program explicitly states which functions or variables are coming from where.

## Methods revisited

We have in fact already met [namespaces](extras/glossary.md#namespace) in a slightly different guise. We have learned about [methods](extras/glossary.md#method): functions that are 'attached' to only one [type](extras/glossary.md#type) of variable. We focused mainly on [string](extras/glossary.md#string) methods, because strings have lots of methods available to them. Each [variable](extras/glossary.md) in Python has its own namespace, and in that namespace are stored links to the methods available for variables of that type.

Recall how this works:


```python
user_name = 'Mildred Bonk'

user_name.upper()
```




    'MILDRED BONK'



This is the same 'dot' notation that we just used for getting something from an imported module's namespace, because the underlying mechanism is essentially the same.

Likewise, just as we used the `dir()` function to find out what methods a variable has available to it, we can also use `dir()` to find out the contents of an imported module's namespace (and again, we can ignore for now the 'special' contents surrounded by double underscores `__ __`):


```python
dir(initials)
```




    ['__builtins__',
     '__cached__',
     '__doc__',
     '__file__',
     '__loader__',
     '__name__',
     '__package__',
     '__spec__',
     'get_initials']



When we have imported a new module, it is a good idea to go to the console and use `dir()` to see what things it has made available to us.

## Special names

By now you will of course be burning with curiosity about those things that keep appearing surrounded by double underscores `__ __`. What are those? We have encountered them twice: once when we used `dir()` to see a list of [methods](extras/glossary.md#method) available for a variable, and once again just now when we used `dir()` to see a list of the contents of the [namespace](extras/glossary.md#namespace) of an imported [module](extras/glossary.md#module).

Python uses the 'double underscore' (you may sometimes see this called a '[dunder](extras/glossary.md#dunder)') to mark something as being involved in the 'behind the scenes' inner workings of a Python program. These things are not normally intended to be used directly, which is why I have so far instructed you on pain of benevolent chastisement to ignore them. However, we are now ready to learn a little bit more about these 'special' names.

### Special variables

Take a look at the list of the contents of the `initials` namespace above, and compare it with the actual contents of [initials.py](examples/initials.py). You will notice that the things that appear enclosed in double underscores in the list above are not variables that are [assigned](extras/glossary.md#assignment) explicitly anywhere in the *initials.py* file.

Python has added these special variables automatically, and does so for every Python file that we run or [import](extras/glossary.md#import). They contain various pieces of information that track the role of that file in our overall program. For example, the automatically-created `__file__` variable stores the full [path](extras/glossary.md#path) to the file that the contents of a namespace came from.


```python
initials.__file__
```




    '/home/lt/GitHub/introduction-to-programming/topics/examples/initials.py'



And `__doc__` stores the [docstring](extras/glossary.md#docstring) that we wrote for the file (if we were diligent and did so):


```python
print(initials.__doc__)
```

    
    A module providing a single function for getting the intials from a name.
    


It is rare that we will want to refer to these special variables in a simple program. But there is one common exception to this. Take a look at [line 43](examples/initials.py#L43) of *initials.py*. This line refers to a special variable, called `__name__`.

To understand how this special variable is being used here, let's first look at its contents:


```python
initials.__name__
```




    'initials'



The somewhat underwhelming answer is that the `__name__` special variable stores the name of an imported module's namespace, which in the case of the *initials* module is... wait for it... `'initials'`!

This seems at first a completely useless thing to know. To even access the `__name__` variable in a namespace, we need to already know the namespace's name, because this is what we must write before the dot.

The usefulness of the `__name__` variable only becomes apparent when we see what value it takes on when it does not find itself inside the namespace of an imported module, but instead finds itself in Python's 'main' overall namespace. The main namespace is just the place that Python puts anything that we define while using the console or running a program. We can see the contents of the main namespace using the `dir()` function again, but with no input [argument](extras/glossary.md#argument). By default, the `dir()` function lists the contents of the main namespace. If we have been messing around for a while in the console creating a few variables or if we have run a program, there may be quite a few things in there:


```python
dir()
```




    ['In',
     'Out',
     '_',
     '_10',
     '_11',
     '_12',
     '_13',
     '_15',
     '_6',
     '_8',
     '__',
     '___',
     '__builtin__',
     '__builtins__',
     '__doc__',
     '__loader__',
     '__name__',
     '__package__',
     '__spec__',
     '_dh',
     '_i',
     '_i1',
     '_i10',
     '_i11',
     '_i12',
     '_i13',
     '_i14',
     '_i15',
     '_i16',
     '_i2',
     '_i3',
     '_i4',
     '_i5',
     '_i6',
     '_i7',
     '_i8',
     '_i9',
     '_ih',
     '_ii',
     '_iii',
     '_oh',
     'exit',
     'get_initials',
     'get_ipython',
     'initials',
     'os',
     'quit',
     'sys',
     'user_name']



Ignore the various other weird things that Python has put in there for us and just note a few things that we recognize.

First of all, among the 'non-underscored' things at the end of the list is the `user_name` string variable that we created earlier in the lesson. Python puts all the variables that we create into the main namespace.

Likewise, the imported module `initials` is in there. As we saw above, `initials` is a subsidiary namespace that gathers everything that gets defined as a result of running *initials.py*. It itself is located in the main namespace, in conceptually the same way that a subfolder with its own file contents may be located in our 'home folder' on a computer.

But most importantly, among the double-underscored special variables, there appears the `__name__` variable that we just learned about. The main namespace has a `__name__` too. What is its `__name__`?


```python
__name__
```




    '__main__'



The main namespace (i.e. the place where everything goes that wasn't imported from elsewhere) is called `'__main__'`.

We can make use of this fact within our programs to find out whether our program has been imported into another program (in which case it will have its own `__name__` such as `'initials'` or `'my_module'` or whatever) or is just being run directly on its own (in which case its `__name__` will be `'__main__'`).

The short educational program [slim_shady.py](examples/slim_shady.py) demonstrates this difference in action. Let's see first of all what happens if we import *slim_shady.py* as a module:


```python
import slim_shady
```

    Hi!
    My __name__ is ... What?
    My __name__ is ... Who?
    My __name__ is ... slim_shady


The file is run. And since it contains some `print()` statements and a reference to the automatically-created `__name__` variable, it prints for us the value that Python has assigned into `__name__`.

Now open up *slim_shady.py* in the Spyder editor and instead of importing it, just run it on its own, in the same way that we have been running all our programs up until now, by clicking the 'Run' button. When *slim_shady.py* is run as its own program, its `__name__` becomes `'__main__'`.

You may now be asking yourself a question that has become quite familiar: This is amazing fun, but what use is it?

Take a look at [line 43](examples/initials.py#L43) of the *initials.py* module. This line applies a [condition](extras/glossary.md#condition), which is something that we are already familiar with. The condition checks whether the value of `__name__` is `'__main__'`, and so is effectively asking 'Am I being run as the main program (or am I just being imported into another program)?' This means that the indented lines following the condition will only be run if we have run the file as its own program, not if we import the file into another program. Try it out. Open *initials.py* in the Spyder editor and run it as a stand-alone program. You will see the results of the final two `print()` statements displayed in the console.

The `if __name__ == '__main__':` condition can be useful for us as programmers while developing and testing a [module](extras/glossary.md#module). If we place a few quick checks of our module's behavior beneath this condition, we can keep checking that our module still works as desired each time we make improvements or additions, by just running the module as a [script](extras/glossary.md#script). But our tests won't disturb us or our collaborators when we come to actually use the module by importing it into another program.

This concept of building in tests to our programs and checking their behavior as we go along is an important one, and we will come back to it later.

### Special methods

We are done with the most important concepts for this lesson: [modules](extras/glossary.md#module) and [namespaces](extras/glossary.md#namespace). For the sake of completeness, we will now also look briefly at the double-underscored [methods](extras/glossary.md#method) that appear when we `dir()` a [string](extras/glossary.md#string) variable. But consider this bonus material; it provides a peek behind the scenes in Python and is included just to satisfy your curiosity.

Let's take a look at these special string methods again, using a new string variable:


```python
word = 'Hello'

dir(word)
```




    ['__add__',
     '__class__',
     '__contains__',
     '__delattr__',
     '__dir__',
     '__doc__',
     '__eq__',
     '__format__',
     '__ge__',
     '__getattribute__',
     '__getitem__',
     '__getnewargs__',
     '__gt__',
     '__hash__',
     '__init__',
     '__init_subclass__',
     '__iter__',
     '__le__',
     '__len__',
     '__lt__',
     '__mod__',
     '__mul__',
     '__ne__',
     '__new__',
     '__reduce__',
     '__reduce_ex__',
     '__repr__',
     '__rmod__',
     '__rmul__',
     '__setattr__',
     '__sizeof__',
     '__str__',
     '__subclasshook__',
     'capitalize',
     'casefold',
     'center',
     'count',
     'encode',
     'endswith',
     'expandtabs',
     'find',
     'format',
     'format_map',
     'index',
     'isalnum',
     'isalpha',
     'isdecimal',
     'isdigit',
     'isidentifier',
     'islower',
     'isnumeric',
     'isprintable',
     'isspace',
     'istitle',
     'isupper',
     'join',
     'ljust',
     'lower',
     'lstrip',
     'maketrans',
     'partition',
     'replace',
     'rfind',
     'rindex',
     'rjust',
     'rpartition',
     'rsplit',
     'rstrip',
     'split',
     'splitlines',
     'startswith',
     'strip',
     'swapcase',
     'title',
     'translate',
     'upper',
     'zfill']



These special methods govern the behavior of a variable in different circumstances. For example, when we 'add to' a variable using the `+` [operator](extras/glossary.md#operator), behind the scenes the special method `__add__()` is [called](extras/glossary.md#call). So the following two statements achieve the same thing:


```python
word + ' world!'
```




    'Hello world!'




```python
word.__add__(' world!')
```




    'Hello world!'



Likewise, the `__eq__()` special method is called when we ask whether a variable is equal to something with `==`:


```python
word == 'Hello'
```




    True




```python
word.__eq__('Hello')
```




    True



And `__getitem__()` is called when we [index](extras/glossary.md#index) a variable using the square parentheses `[]`:


```python
word[0]
```




    'H'




```python
word.__getitem__(0)
```




    'H'



You get the general idea.

But please don't understand from this that you should actually use these double-underscored methods in your programs. You should not. They are not intended to be used directly. We will only encounter them again much later on in our programming careers, when we come to define our own new [data types](extras/glossary.md#type). Then we will need to define some of these special methods so that Python knows what to do with variables of our new type when we combine them with `+` or index them with `[]`. For now, forget about special methods.

## Exercise

### 1

Revisit the *words.py* program that you created in [exercise 2 of the previous lesson](functions.md#2) (or go and complete that exercise first if you haven't yet).

Use the `__name__` special variable as we learned above to add a 'test section' to the end of the program. Use this section to generate a printout that confirms the correct behavior of the `first_n_words()` function using the test phrase `'Hello my name is Mildred.'` and each of the three values `0`, `4`, and `9000` for the `n` argument.

Check that this printout is generated only when you open *words.py* and run it as its own program, and not when you `import` it.

### 2

Write a new program. Your program should:

* Import the *words.py* module that you created in [exercise 2 of the previous lesson](functions.md#2).
* Ask the user to type in a number `n`.
* Use the `first_n_words()` function from *words.py* to print for the user the first `n` words of the first verse of *Always Look on the Bright Side of Life* by Monty Python:

> If life seems jolly rotten  
> There's something you've forgotten  
> And that's to laugh and smile and dance and sing  
> When you're feeling in the dumps  
> Don't be silly chumps  
> Just purse your lips and whistle, that's the thing  

(Or you can use another short song if you prefer.)
