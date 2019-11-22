<h1>Contents<span class="tocSkip"></span></h1>
<div class="toc"><ul class="toc-item"><li><span><a href="#Strings" data-toc-modified-id="Strings-1">Strings</a></span></li><li><span><a href="#Assignment-and-immutability" data-toc-modified-id="Assignment-and-immutability-2">Assignment and immutability</a></span></li><li><span><a href="#Numeric-data" data-toc-modified-id="Numeric-data-3">Numeric data</a></span><ul class="toc-item"><li><span><a href="#Python-2" data-toc-modified-id="Python-2-3.1">Python 2</a></span></li></ul></li><li><span><a href="#Type-conversion" data-toc-modified-id="Type-conversion-4">Type conversion</a></span></li><li><span><a href="#User-input" data-toc-modified-id="User-input-5">User input</a></span><ul class="toc-item"><li><span><a href="#Python-2-again" data-toc-modified-id="Python-2-again-5.1">Python 2 again</a></span></li></ul></li><li><span><a href="#Methods" data-toc-modified-id="Methods-6">Methods</a></span><ul class="toc-item"><li><span><a href="#String-formatting" data-toc-modified-id="String-formatting-6.1">String formatting</a></span></li></ul></li><li><span><a href="#Other-types" data-toc-modified-id="Other-types-7">Other types</a></span><ul class="toc-item"><li><span><a href="#Boolean" data-toc-modified-id="Boolean-7.1">Boolean</a></span></li><li><span><a href="#None" data-toc-modified-id="None-7.2">None</a></span></li><li><span><a href="#Tuple" data-toc-modified-id="Tuple-7.3">Tuple</a></span></li><li><span><a href="#List" data-toc-modified-id="List-7.4">List</a></span></li></ul></li><li><span><a href="#Exercises" data-toc-modified-id="Exercises-8">Exercises</a></span><ul class="toc-item"><li><span><a href="#1" data-toc-modified-id="1-8.1">1</a></span><ul class="toc-item"><li><span><a href="#a)" data-toc-modified-id="a)-8.1.1">a)</a></span></li><li><span><a href="#b)" data-toc-modified-id="b)-8.1.2">b)</a></span></li><li><span><a href="#c)" data-toc-modified-id="c)-8.1.3">c)</a></span></li></ul></li><li><span><a href="#2" data-toc-modified-id="2-8.2">2</a></span></li></ul></li></ul></div>

# Variables and data types

In the [introductory lesson](intro.md), we learned how to assign some data into a [variable](extras/glossary.md#variable). Below are a few examples. We will use these variables in the remainder of this lesson.


```python
name = 'Mildred T. Bonk'
street = 'Credibility Street'
street_number = '221'
age = 22
height = 1.96
```

## Strings

We have also learned about the important distinction between variables that store text (termed [strings](extras/glossary.md#string) and abbreviated to `str`) and variables that store numbers. The form of the data stored in a variable (text, number, something else) is called its [type](extras/glossary.md#type).

In the examples above, the variables `name`, `street`, and `street_number` are of type string. We can see this from the way that they are written. The [syntax](extras/glossary.md#syntax) for creating a string is simply to enclose the text of the string in quote marks (`''`). Quote marks distinguish strings (i.e. literal text) from other things such as numbers, the names of other variables, or Python commands, all of which are written without quote marks. This is similar to the use of quote marks in everyday English. Think of the lyrics to the song [Say My Name](https://en.wikipedia.org/wiki/Say_My_Name) by Destiny's Child. When Beyoncé issues the instruction *say my name*, she intends *my name* to be replaced by her actual name when the instructions are carried out. This is equivalent to the following short Python program, albeit with `print()` in place of *say*, since Python has no `say()` function:


```python
my_name = 'Beyoncé'

print(my_name)
```

    Beyoncé


What if the lyrics to the song were subtly different and included quote marks around '*my name*' (i.e. *say 'my name'*)? One use of quote marks in English is to clarify that a piece of text is to be interpreted literally, and not replaced with whatever the text refers to. So this version of the song would be equivalent to the following short Python program:


```python
my_name = 'Beyoncé'

print('my_name')
```

    my_name


When it comes to data types, appearances can occasionally be deceptive. For example, the `street_number` variable that we created above is a string that happens to contain digits. These can occur from time to time in programming, in cases where the digits do not really represent a mathematical quantity or might sometimes need to have extra non-number characters added to them (for example, Sherlock Holmes lives at house number 221b, which we can't represent and manipulate as an actual number).

If we are unsure what type of data is stored in a variable, we can check at the console using the [built-in](extras/glossary.md#builtin) Python function `type()`:


```python
type(street_number)
```




    str



Python is fairly strict about what we can and cannot do with various types. If we try to get Python to [evaluate](extras/glossary.md#evaluate) a mathematical expression that contains a string variable, we will encounter an [error](extras/glossary.md#error).


```python
street_number + 1
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-5-69d4580a9089> in <module>
    ----> 1 street_number + 1
    

    TypeError: must be str, not int


However, some Python functions and [operators](extras/glossary.md#operator) are somewhat flexible, and may instead do different things depending on the type of the variable that they are applied to. For example, the multiplication operator `*` performs normal math multiplication for variables that store numbers, but for strings it instead repeats their contents.


```python
height * 2
```




    3.92




```python
name * 3
```




    'Mildred T. BonkMildred T. BonkMildred T. Bonk'



Python's occasional flexibility about data types is a double-edged sword. On the one hand, it allows for some concise intuitive commands, such as using `+` to combine strings or `*` to repeat them. But on the other hand, it means that we can occasionally make some big mistakes in our programs without immediately becoming aware of it. For example, if we found that `street_number` had been entered incorrectly and in fact needed an extra zero adding to it, then we might be tempted to multiply it by 10 in order to achieve this. Python would give no warning and would go ahead with what we asked even though the result is not what we want. In this case, our program might end up sending somebody's automated delivery a lot further down the street than we intended.


```python
street_number * 10
```




    '221221221221221221221221221221'



A correct way to add an extra 0 to a string would be to add another string containing the `'0'` *character*.


```python
street_number + '0'
```




    '2210'



## Assignment and immutability

'Assignment and immutability' is of course the title of a novel by Jane Austen. But it also refers to two important concepts in Python programming. We learned about [assignment](extras/glossary.md#assignment) earlier; when we assign some value to a variable, we store that value under the name of the variable, and can retrieve it using that name.

To understand immutability, let's remind ourselves of something. Take a look at the value of the `street_number` variable after everything that we have been doing with it above.


```python
street_number
```




    '221'



It hasn't changed since its original assignment. Although we have been performing various operations with the variable, we have merely been testing out and looking at the results of these operations. The value of the variable has remained unchanged. The value of a string variable will always remain the same unless we overwrite it by assigning it again. If we want to change or update the value of a variable with the result of some calculation, then we must assign that result back into the same variable name.

For example if we want to add a `'b'` to the `street_number` string (and then print it out to check its new value):


```python
street_number = street_number + 'b'

print(street_number)
```

    221b


The opposite of immutability is 'mutability'. As it turns out, there are some data types that are mutable. That is, their contents can change without us having to overwrite them. We will meet one of these at the end of this lesson. But all the simple data types, such as strings and numbers, are immutable; string and numeric variables will only ever change their contents if there is an `=` somewhere in our program that overwrites them.

Although this behavior can occasionally be a source of frustration, for example if we perform some calculations but forget to store the result in the relevant variable, in general immutability is a good thing. It would be annoying if every time we wanted to calculate something with our variables, this also overwrote their contents. For example, we might want to just print out the result of adding one year to somebody's age, without actually changing it.

Of course if we want to keep both the original value of a variable and store an updated one, we can just assign the updated value into a *new* variable. In such cases it is a good idea to choose an expressive variable name that says something about what the changed value means. For example:


```python
age_next_year = age + 1

print(age)
print(age_next_year)
```

    22
    23


## Numeric data

So far most of our examples have concerned the behavior of the [string](extras/glossary.md#string) data type. Let's now consider how Python manages numbers.

Python distinguishes between two different ways of representing numbers. Numbers can be stored either as whole numbers (`1`, `2`, `3`, etc.) or as non-whole numbers (for example `1.618`, `2.718`, or `3.142`). Whole numbers are called [integers](extras/glossary.md#integer) (abbreviated to `int`), and non-whole numbers are called [floating point numbers](extras/glossary.md#float) (abbreviated to `float`). Just as there is a particular [syntactical](extras/glossary.md#syntax) rule for creating a string, namely the use of quote marks, so there are syntactical rules for creating integers and floats. The presence of a decimal point (`.`) indicates a float, and its absence indicates an integer.

Take a look back at the `age` and `height` variables that we defined above. We can see that Python has stored these as two different types.


```python
type(age)
```




    int




```python
type(height)
```




    float



Note that even if the number represented is a whole number, if we include a decimal point its type will still be float.


```python
grade = 1.0

type(grade)
```




    float



For historical reasons, the syntax of programming languages (along with many other conventions in computing in general) is heavily influenced by British and US English. If you come from a part of the world where the comma is used as a decimal separator instead of the point, for example Germany, then beware that Python does not interpret it this way. If you try to create a float using the comma, the result will not be as expected. Surprisingly, however, you will not see an [error message](extras/glossary.md#error) either. Instead, Python interprets commas as separating two different things, and so will store the two numbers together in a new kind of variable (called a [tuple](extras/glossary.md#tuple)) that can contain more than one value.


```python
grade = 1,3

print(grade)
```

    (1, 3)


But more about tuples later.

How should we decide whether to store a number as integer or float? If we want to store a non-whole number, the decision is easy; it has to be a float. But what about something like somebody's age? Here, we have to think about what concept the number is supposed to represent in the real world, and consider whether we want to treat the units of that concept as atomic or as divisible into parts. For example, we can think of someone's age as being a count of the number of whole years that they have survived. But we can also think of it as a continuous measure of how much time they have survived. Children in particular often like to give their age as a continuous quantity like 'six-and-three-quarters'.

As it turns out, there are many cases in which the difference between integers and floats does not actually matter for the functioning of our program. Python is quite flexible with number types.

It allows us to mix integer and float numbers in the same mathematical expression:


```python
child_age = 6
precise_child_age = child_age + 0.75

type(precise_child_age)
```




    float



The result of a mathematical expression containing a mixture of integers and floats is always a float, even if the resulting quantity is a whole number:


```python
answer = 2 + 2.0

type(answer)
```




    float



A calculation that involves only integers and that results in a whole number will produce an integer:


```python
answer = 2 + 2

type(answer)
```




    int



If a calculation with integers results in a non-whole number then Python does the reasonable thing and nonetheless stores the result as a float instead of rounding it off:


```python
three_quarters = 3 / 4

type(three_quarters)
```




    float



Indeed, any calculation involving division will result in a float, even if the result is a whole number (you might find this rule a little less intuitive):


```python
two_halves = 2 / 2
type(two_halves)
```




    float



If we are dividing integers and we would like to insist that the result also be an integer, then we can use a double slash `//` for so-called 'floor division'. The result is 'rounded down':


```python
lego_bricks = 52
bricks_per_house = 10
houses_built = lego_bricks // bricks_per_house

print(houses_built)
```

    5


### Python 2

A previous version of Python, Python 2, was slightly less flexible about numeric data types. The result of division with integers in Python 2 was always an integer, with the non-whole part discarded. This could produce some surprises for the unwary, such as the result of `1 / 2` being `0`.

We are learning to program with Python 3, and almost all new Python software is written for Python 3, so you do not need to worry about this. Just be aware of it if you see some older Python examples or programs when searching online.

## Type conversion

What if we have data of one type, but we need it to be of another? For example, we have stored the house number of an address as a string because we might need to append letters to it, but now in another part of our program we need to do some math with it, perhaps in order to find out the address of a next-door neighbor.

Python has functions that convert one data type into another. Each of these functions has the same name as the abbreviated name of the data type that we are converting to. So for example `str()` converts to string, and `int()` to integer.

We can apply these functions to variables within a calculation that would otherwise result in an error:


```python
number_beast = '666'

neighbor_beast = int(number_beast) + 2

print(neighbor_beast)
```

    668


And here is a similar example but imagining we had first stored the house number as an integer:


```python
number_beast = 666

annexe_beast = str(number_beast) + 'b'

print(annexe_beast)
```

    666b


Remind yourself one more time that the values of string and numeric variables are not changed unless we overwrite them with an `=` assignment. Forgetting that this principle also applies to type conversion can lead to a common beginners' mistake.

Line 2 in this example has no effect on the type of the `number_beast`variable because it is not assigned anywhere:


```python
number_beast = 666
str(number_beast)

annexe_beast = number_beast + 'b'

print(annexe_beast)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-25-293d2fd1f181> in <module>
          2 str(number_beast)
          3 
    ----> 4 annexe_beast = number_beast + 'b'
          5 
          6 print(annexe_beast)


    TypeError: unsupported operand type(s) for +: 'int' and 'str'


Here the problem is fixed:


```python
number_beast = 666
number_beast = str(number_beast)

annexe_beast = number_beast + 'b'

print(annexe_beast)
```

    666b


We saw above that Python handles the two numeric data types integer and float fairly flexibly and intuitively if we mix them in mathematical expressions. For this reason it is not so often necessary to convert variables between these two types.

(The most common case in which we do want to do this is in order to convert float to integer. We will later encounter some situations in which we definitely need integers.)

## User input

Let's take a look at a common situation in which type conversion from string to numeric is necessary. In one of our first example programs, [greeting_personal.py](examples/greeting_personal.py#L9), we used the `input()` function in order to prompt the user to type something in at the console.

The `input()` function always [returns](extras/glossary.md#return) a string, even if the user types in a valid number. If we try to do math with the result, we will encounter an error:


```python
user_age = input('How old are you? ')
age_next_year = user_age + 1
```

    How old are you? 52



    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-27-e69a11705ffd> in <module>
          1 user_age = input('How old are you? ')
    ----> 2 age_next_year = user_age + 1
    

    TypeError: must be str, not int


Python has no way of knowing what type of data we want to get from the user. So in order to 'play it safe' and always be consistent, Python makes it a string and leaves it up to us to convert the contents of the string if necessary.

So if we want to get numbers from the user, we must first convert the result of `input()`:


```python
user_age = input('How old are you? ')
user_age = int(user_age)
age_next_year = user_age + 1

print(age_next_year)
```

    How old are you? 52
    53


The example program [age_next_year.py](examples/age_next_year.py) shows how to use this pattern of Python commands in a simple program. If you would like to explore type conversion a little more, open up the file in Spyder, save a new copy of it, for example under the name *age_next_year_v2.py*, and try out a few changes:

* Does it matter for the workings of the program if you convert the user input to float instead of integer?
* Why is it necessary to use the `str()` type conversion function on [line 14](examples/age_next_year.py#L14)? What happens if you remove it?
* What happens if the user enters a non-whole number for their age, such as `6.75`?

### Python 2 again

One of the other most noticeable differences in the previous version of Python was the behavior of the `input()` function. Confusingly, in Python 2 this function treated the user's input not as a string, nor even as a number, but as a *Python command*, which Python 2 would then [evaluate](extras/glossary.md#evaluate). In theory this allowed malicious or just clumsy users to completely mess up the workings of a program by entering their own Python commands at the console while the program was running. So Python 3 takes the much safer option of just treating all user inputs as strings.

Again, you do not need to worry about this since we will always be working with Python 3. Just be aware of it if you encounter old Python examples on the internet.

## Methods

As we have seen, Python's [type](extras/glossary.md#type) system lays down some (mostly) sensible rules about what we can and cannot do with various types of data. For example, we can perform division with integers and floats but not with strings. How does this work 'behind the scenes'? It turns out that for any variable we can access a list of the things that it is possible to do with a variable of that type. Along with the actual data stored in a variable, Python stores various links to the operations that it is possible to carry out with that type of data.

The `dir()` function returns this list of possibilities for a certain variable. Let's try it for our `name` variable. Since this variable is a string, `dir()` tells us what it is possible to do with strings.


```python
dir(name)
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



(Note that it is only very rarely that we will need to use the `dir()` function in an actual program. It is instead a useful function to enter at the console when we are experimenting and checking Python's behavior. It can be particularly useful when we encounter a new [type](extras/glossary.md#type) and want an overview of the sorts of things that it can do.)

In the output from `dir()` we see various things enclosed in double underscores `__ __`. We do not need to concern ourselves with these for the moment. They define the behavior of strings when they appear in various Python commands. For example, the `__add__` entry refers to the behavior of strings when we combine them with the `+` operator.

The entries that interest us for the moment are those without underscores. These are the names of functions that can be applied to strings. Functions that are defined especially for one data type and can be accessed through variables of that type are called '[methods](extras/glossary.md#method)' for that data type. For example, the penultimate entry in the list of string methods above is a method called `upper`. This method [returns](extras/glossary.md#return) an all UPPERCASE version of the string. This method is special to strings; it wouldn't make any sense for other data types.

The syntax for [calling](extras/glossary.md#call) a method has a lot in common with the syntax for calling any other function:

* place parentheses after the name of the method
* (optionally) place any input [arguments](extras/glossary.md#argument) for the method inside the parentheses

But there is an important difference. We first 'go into' the variable that we want to apply the method to, and get the method from there. To go into a variable like this in Python, we place a dot (`.`) after its name.

So to call the `upper()` method on our string variable `name`:


```python
name.upper()
```




    'MILDRED T. BONK'



Note that we do not also need to put the variable inside the parentheses, as we do with functions. Because we have accessed the method by first going into a particular variable, Python already understands that we wish to apply the method to that same variable.

Indeed, if we make this mistake, we may get an error message telling us that we have given too many [input arguments](extras/glossary.md#argument):


```python
name.upper(name)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-31-b59fa512a01b> in <module>
    ----> 1 name.upper(name)
    

    TypeError: upper() takes no arguments (1 given)


And remember once again that strings are [immutable](#extras/glossary.md#mutability). Calling a method of a string variable does not change the string, it merely [returns](extras/glossary.md#return) the result.


```python
name.upper()

print(name)
```

    Mildred T. Bonk


Some methods require additional input [arguments](extras/glossary.md#argument). For example the string method `count()` counts how many times a particular 'substring' appears inside a string variable. The input argument is the substring to count:


```python
print(name)

name.count('d')
```

    Mildred T. Bonk





    2



Note that Python strings are 'case-sensitive'. UPPERCASE characters are not considered the same as their lowercase counterparts:


```python
print(street)
street.count('s')
```

    Credibility Street





    0



Python [syntax](extras/glossary.md#syntax) allows methods to be applied one after another within the same command. Immediately after calling one method, we can use the `.` syntax again to call another method on the *result* of calling the first method.

For example, to first get a lowercase version of a string and then count the occurrences of a particular character in that lowercase version:


```python
street.lower().count('s')
```




    1



A common pattern when dealing with user input is to apply a few string methods to the input in order to 'clean' it. If we would like to make our program a little more robust to variations in user behavior, we can for example strip away any surrounding spaces that they typed by accident (with the `strip()` method), and then convert the result to lowercase (with the `lower()` method).

For example to allow the user to type `'yes'`, `'Yes'`, `'YES'`, or even `'      yEs'` and make all these inputs equivalent to `'yes'`:


```python
answer = input('Would you like a buttered crumpet? ')
answer = answer.strip().lower()

print(answer)
```

    Would you like a buttered crumpet?       YES
    yes


Now would be a good moment to turn to the console in Spyder and explore some of the other string methods. In the console, create yourself a string variable (for example by entering a command like `word = 'floccinaucinihilipilification'`), then use the `dir()` function to view its available methods, then try to apply some of them to see what they do.

Some string methods are a bit too complex for us at this stage. Try the following ones:

* `capitalize()`
* `count()`
* `endswith()`
* `find()`
* `index()` (Note the subtle difference from `find()`.)
* `lower()`
* `lstrip()`
* `replace()`
* `rstrip()`
* `split()`
* `startswith()`
* `strip()`
* `swapcase()`
* `title()`
* `upper()`

If you are feeling adventurous you can just try these out and see whether you can work out what they do. If so, make sure to test them with a variety of different strings to check that you have really understood their behavior. If you would like to check or need some help with examples, you can search online for *Python string method x* or you can read the official documentation for all of Python's string methods [here](https://docs.python.org/3/library/stdtypes.html#string-methods).

You might be wondering whether the two numeric data types that we have learned about also have methods. They do. But because we tend to work with numbers primarily using mathematical [operators](extras/glossary.md#operator), we rarely need to work directly with their methods as we do for strings.

### String formatting

We will look now at just one more string method together, because it is a very useful one, but whose use is not completely straightforward. The `format()` method inserts the values of other variables into certain positions in a string. This is particularly useful for preparing neat printouts for the users of our programs.

To use `format()`, our string must contain the characters `{}` in the positions where we would like to insert something. These positions are termed 'replacement fields', and they will be replaced by the values from the variables that we give as [arguments](extras/glossary.md#argument) to the `format()` method.

Let's see an example using `format()` to print out a few different pieces of information contained in the variables we created at the beginning of this lesson:


```python
message = 'User {} is {} years old and {} meters tall.'

message.format(name, age, height)
```




    'User Mildred T. Bonk is 22 years old and 1.96 meters tall.'



We can see that if we have multiple `{}` replacement fields, these are replaced with the values of the variables that we give to `format()` in the order that we enter them. Notice also that we did not have to use the `str()` type conversion function to convert the two numeric variables `age` and `height` into strings; `format()` handles variables of different types automatically.

There is a little bit more to the `format()` method than this. For example, we can also specify how many decimal places of a [float](extras/glossary.md#float) to insert into the string, and other details. But this is enough for now about `format()`, and about string methods in general. If you would like to see an example of a program that makes use of a few string methods, take a look at [name_trivia.py](examples/name_trivia.py).

## Other types

Are there other data types in Python? Is there anything in the world worth talking about other than words and numbers?

Yes. In fact there are lots more. We will finish this lesson with a quick overview of a few more types. We will learn about these in more detail in the lessons that follow.

### Boolean

Variables of [boolean](extras/glossary.md#boolean) type are very simple. They store one of only two possible values: `True` or `False`. Boolean values can be the result of various Python commands whose purpose is to check whether or not something is the case. For example, the string [method](extras/glossary.md#method) `startswith()` [returns](extras/glossary.md#return) a boolean value, `True` if the string starts with a particular substring, and `False` otherwise:


```python
print(name)

answer = name.startswith('m')

print(answer)
type(answer)
```

    Mildred T. Bonk
    False





    bool



(If you were expecting `True` above, remember that strings are case-sensitive.)

### None

Occasionally, the status of some piece of information in our program is neither true nor false nor a string nor a number nor anything, it is instead simply undefined. There is an 'empty' type called [`None`](extras/glossary.md#none) for this eventuality. We might occasionally [assign](extras/glossary.md#assignment) `None` into a variable as a default starting value, anticipating that this value might be changed later on in our program.


```python
proof_of_Riemann_conjecture = None

type(proof_of_Riemann_conjecture)
```




    NoneType



We can also sometimes get a `None` value if we try to [assign](extras/glossary.md#assignment) the result of a function that actually does not [return](extras/glossary.md#return) anything. For example, although the `print()` function serves to display output for the user of our program, it does not actually return any value that can be assigned. By default, a function that does not return anything returns `None`.


```python
x = print('Hi.')

type(x)
```

    Hi.





    NoneType



### Tuple

We briefly encountered the [tuple](extras/glossary.md#tuple) by mistake earlier, when we tried to create a [float](extras/glossary.md#float) using a comma for the decimal separator instead of a point. The comma is not the correct Python [syntax](extras/glossary.md#tuple) for the decimal separator, but it turns out that it *is* the correct syntax for something else: separating multiple values in a sequence. The result is a data type that does exactly that; it stores multiple values in a sequence. Although not an absolutely necessary aspect of the syntax, it is an extremely common convention to also place parentheses around the sequence of values when creating a tuple, as this makes our program clearer.

Here is an example of creating a tuple:


```python
shopping = ('eggs', 'bacon', 'black pudding')

type(shopping)
```




    tuple



We can refer to the values in a tuple using their [indices](extras/glossary.md#index), their numbered positions in the sequence. We place the index in square parentheses `[]` after the name of the tuple variable.

Beware that Python's numbering system for sequences begins at zero. So the first value in a tuple has index `0`, the second value has index `1`, and so on.


```python
print(shopping[0])
print(shopping[1])
```

    eggs
    bacon


We cannot change individual values in a tuple. Here is what happens if we try:


```python
shopping[1] = 'organic vegan bacon'
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-43-21c829b36b26> in <module>
    ----> 1 shopping[1] = 'organic vegan bacon'
    

    TypeError: 'tuple' object does not support item assignment


Like all the data types we have encountered so far, tuples are [immutable](extras/glossary.md#mutability). If we want to change the contents of a tuple variable, we must overwrite the whole thing by assigning it anew with `=`.


```python
shopping = ('eggs', 'organic vegan bacon', 'black pudding')
```

### List

Not being able to change individual values in a tuple seems like a very onerous restriction. What if we are working with data that need to be updated or added to as our program runs? [Lists](extras/glossary.md#list), the final data type that we will learn about in this lesson, provide just this ability. A list is an ordered sequence of values, just like a tuple, but it is [mutable](extras/glossary.md#mutability); we can change one item in a list without having to re-assign the whole thing.

The [syntax](extras/glossary.md#syntax) for creating a list is the same as for creating a tuple, except with square parentheses in place of round ones:


```python
shopping_list = ['eggs', 'bacon', 'black pudding']

type(shopping_list)
```




    list



Python allows us to change individual values in a list:


```python
shopping_list[1] = 'organic vegan bacon'

print(shopping_list)
```

    ['eggs', 'organic vegan bacon', 'black pudding']


There are also list [methods](extras/glossary.md#method), like the string methods we learned about above. For example, there is a list method called `append()` for adding a new value to the end of the list:


```python
shopping_list.append('sausages')

print(shopping_list)
```

    ['eggs', 'organic vegan bacon', 'black pudding', 'sausages']


Notice what just happened. The `append()` method changed the list without our having to [assign](extras/glossary.md#assignment) the result back into the list variable with `=`. This is different from the behavior of string methods. As we learned above, string methods always just [return](extras/glossary.md#return) the result of whatever it is that they do with the string, but they do not change the string while doing so. List methods just go ahead and change the list.

This distinction is important, and forgetting it can lead to some frustrating mistakes. Let's see what happens if we try to use a list method as if it were a string method, and assign its return value back into the original list variable:


```python
shopping_list = shopping_list.append('more sausages')

print(shopping_list)
```

    None


The `print()` function suddenly seems to have no effect, and prints nothing. This is because our list has gone. List methods do not do their work by outputting a [return value](extras/glossary.md#return) as string methods do. Most list methods do not output anything. As we learned a moment ago, the output of a function that does not have any defined output is the `None` value. So our list has become just `None`.


```python
type(shopping_list)
```




    NoneType



So beware. If you want to change a list, it is enough to just use the list method. Don't assign the result back into the list variable.

As you did for string methods above, take a moment to go to the console in Spyder and explore the behavior of some of the list methods. Try to discover what the following methods do:

* `clear()`
* `count()`
* `index()`
* `insert()`
* `remove()`
* `reverse()`
* `sort()`

Because list methods just change the contents of the list behind the scenes and do not produce output, you will need to `print()` your list after applying each method to see what change has taken place.

## Exercises

### 1

A good way to strengthen your understanding of how Python works is to test that understanding regularly. When you test out a command in the console, try first to predict what the result will be, and only then type it in to check whether you were right. What is the result of each of the following short programs?

#### a)

```python
name = 'Mildred T. Bonk'
name.lower()
m_count = name.count('m')
print(m_count)
```

#### b)

```python
info = ('Mildred T. Bonk', 22, 1.96)
print(info[1].lower())
```

#### c)

```python
names = ['Mildred', 'T.', 'Bonk']
print(names.reverse())
```

### 2

The ['half-your-age-plus-seven' rule](https://en.wikipedia.org/wiki/Age_disparity_in_sexual_relationships#The_%22half-your-age-plus-seven%22_rule) is a folk rule of thumb used to calculate the minimum socially acceptable age of your dating partners, given your age. The rule asserts that if your age is $x$, then the minimum socially acceptable age for your partner is:

$$
\frac{x}{2} + 7
$$

Write a program that asks the user for their age, and then tells them the result of applying this rule of thumb.
