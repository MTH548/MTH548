Weekly Digest 1
===============

**Tianyi asks:**

    is this class the following of the mth337?

Yes, but you can take it without taking MTH 337, as long as you know some Python. 

**Griffin asks:**

    Are the exercises on the course page going to be collected/graded?

No, only project reports will be collected and graded. However, solutions of exercises 
will often be needed to complete the projects. 

**Saiful asks:**

    What will be difficulty level of the project related to Machine Learning? 

The intention is for projects to be challenging enough to be interesting, but doable
without too much difficulty. Also, most projects will be open-ended, so you can 
decide how far you want to go with them. 


**Bochun asks:**

    Since this course is following the same structure as MTh337, will the grade rubric be similar to MTH337? 
    Specifically, I can earn a A+ grade in a project, and that + grade will be treated like some extra credit 
    when finalizing the letter grade for the course. Will we have these opportunities by any chances? 
    And if passible, I would like to learn some regex syntax because it's very useful.

Yes, you can get an A+ on any project report. Detailed project report rubrics are posted 
`here <../_static/report_rubrics.pdf>`_. I plan to talk about regex. 

**Qiang asks:**

    Is the proportion of each project the same? 

No, most likely there will be a couple shorter projects that will carry less weight toward 
the course grade. This will be specified in project descriptions. 


**Scott asks:**

    Is there a way instead of the argsort being from smallest to greatest that it can be greatest to smallest?

You can revert the array obtained with :code:`np.argsort()` using something like :code:np.argsort(arr)[::-1], 
where :code:`arr` is the array you want to sort. 


**Thinh asks:**

    If we are not able to solve all the exercises, will it mean that we will not do well on the project?

No. Not all exercises are needed for the project, and you can always ask for help in class or 
during office hours.  


**Metin asks:**

    When we are doing exercises, do you want us to only use tools that were taught in lecture up to that point 
    or is it acceptable to use google to find out more functions / commands? For example, for Exercise 1 
    of week 1, if we simply stick to what we learned in class, we can create a new array of zeros and change 
    its "middle" to the existing array. Otherwise, we can find commands to append the existing array with rows 
    and columns of zeros. Do you have a preference between these two solutions?

In general you can use any tools you know. When I will want you not to use some tools, 
I will specify it. In this particular case, appending works but it is not efficient since you need to 
use it a few times, and each append creates a new array. The first method - creating an array of zeros 
and changing some of its entries is faster. Numpy also has :code:`np.pad()` function which could be used here. 

**Carter asks:**

    Will we go over any SQL/database projects in this class? I am interested in data engineering stuff.

Yes, we should get to SQL at some point. 


**Linggan asks:**

    What is the due date of the first project?

We have not started working on it yet, but it should be due on Wednesday, 2/16. 


**Anjali asks:**

    How difficult will the projects be?

The intention is for projects to be challenging enough to be interesting, but doable
without too much difficulty. Also, most projects will be open-ended, so you can 
decide how far you want to go with them. 


**Meaghan asks:**

    What are some recomendations on stronger report writing? This is something that 
    I have struggled with previously. 

I will talk about it in class. See also the :doc:`Report Guide <../report_guide>`.


**Jena asks:**

    What will the projects be like? (Will they be 'cumulative' and build off most concepts 
    or will they focus on the current idea?)

Mostly focused, but they will use previous material too. 


**Luca asks:**

    Why Python and not Matlab? What is the difference between them?

Matlab is a focused on scientific and engineering computations and modeling. Python 
is a general purpose language, which has libraries that provide functionality
analogous to Matlab tools (and much more). Matlab is a proprietary commercial product. 
UB pays for Matlab access for students, but once you graduate you would need to buy 
a Matlab license yourself to use it. Python is open-source and anyone can use it for free. 
Python is consistenly ranked as one of the most popular and most in-demand programming languages, 
Matlab is not. 


**Farhat asks:**

    I'm not sure if this was mentioned in class but a question that I have for my own understanding 
    is if the show() function will change color spaces if we type in a different color space in 
    the previous function? For example, in the sorting part of class, when we used show() for a rng.random array, 
    it came out with blue, red, and white hues. Could we change the color scheme to another one if we wanted to? 

The :code:`show()` function is a function that I wrote to illustrate some features of 
numpy arrays. It is not a part of Python or any of its libraries, and we will probably 
not use it again in this course. This function takes an argument :code:`cmap` which you 
can use to specify a matplolib colormap. The color scheme depend on the choice of the colormap. 


**Kyle asks:**

    Can you please talk a bit louder in class? Sometimes it is hard to hear.

I will try. If I will be speaking not loudly enough, please let me know. 

**Cassandra asks:**

    Is there a particular reason to use jupyter notebook opposed to other coding languages/systems? 

Jupyter notebook is not a programming language, but an interactive programming environment. 
The programming language we are using in this course is Python. Python is one of the easiest 
programming languages to learn, and it is also one of the most popular - especially in 
data analysis applications.  

**Adrian asks:**

    Will the theory behind the projects and how it impacts us today be discussed in class ?

I will explain the theory beyond various tools for data analysis we will be using. 

**Dakota asks:**

    Is it possible to send a finished project report to the professor before the due date to get feedback?

I would prefer not to review project reports twice (it takes quite a lot of time). However, 
if you are uncerain about some elements of the report, please ask me either in class 
or during office hours and I will be happy to help.  

**David asks:**

    Are the work in this class a good representation of the work done in the data science industry?

The tools and techniques you will learn in this course are used by professional data analysts. 
However, a lot of other tools and underlying theory that data analysts use will not be covered 
in this course, since there is only so much that can fit in a single semester. So, the work in 
the class is a representation of the work done in the industry, but not a complete representation.  

**Steven asks:**

    Will the solution of the practice problems be posted?

I don't plan to do it, but you can ask me for help either in class or during office hours. 

**Jason asks:**

    When is the first project due? 

We have not started working on it yet, but it should be due on Wednesday, 2/16. 


**John asks:**

    How related is this course to MTH 337? Is it much more advanced in terms of difficulty, 
    or similar and more af an extension to MTH 337?

MTH 448 is intended as a continuation of MTH 337 focused on data analysis applications. 
Tools are more advanced, but the course overall should not be more difficult. 


**Michael asks:**

    Will we only be coding in Python, or will be using other programming languages throughout 
    the course?

We should get to SQL at some point, but otherwise we will use Python. 

**Felix asks:**

    Why don't Python lists natively operate like numpy arrays do. (Why weren't they 
    initially programmed into base python in that way)

This is a tradeoff. Python lists are already complex objects that can store any 
type of data, dynamically grow and shrink etc. Numpy arrays add some functionality, 
but also remove some - for example, their size cannot change once they are created. 
One could try to create "superlists" combining functionality of lists and numpy arrays, 
but then perfomance would become an issue - the structure of such objects would 
require a lot of memory and computing power to operate on them. If you want though, 
you could try to implement it yourself. Python is open-source, so it is possible 
to fork its repository and experiment with new implementations of lists. 
People do such experiments all the time, and from time to time they are incorporated 
into new Python versions.     

**Haiyi asks** 

    When I want to select elements in rows, but I want to select discontinuous rows, 
    what should I do, like elements in rows 1, 3, 5...

You can use fancy indexing: :code:`arr[[1, 3, 5]]` will select rows 1, 3, 5 
of the array :code:`arr`. 