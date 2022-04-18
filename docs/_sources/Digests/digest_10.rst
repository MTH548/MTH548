Weekly Digest 10
================


**Cassandra asks:**

    Is plotly the most commonly used graphing library in python libraries?

Matplotlib is probably most commonly used, in part because it has been in use 
the longest.  

**Griffin asks:**

    Will we be utilizing linear regression in the next project?

Yes. 


**Saiful asks:**

    Will we learn Python Class in the next weeks, which we can use for constructing 
    a probabilistic model in the next project? 

:code:`gaussian_kde` from :code:`scipy.stats` is such a tool we already used it last 
week. As for the construction of the Bayes classifier using KDE, for the next project
you will need to perform it yourself based on KDE computations.  


**Scott asks:**

    What is a regular array in python that does not involve numpy? What is 
    the significance of the value of kde at a particular point? Is it just 
    a relative value?

Python lists can be used in place of numpy array. However, lists are one-dimensional 
only, do not provide vectorization and are usually much slower. 

KDE is an estimate of the probability density function (PDF) describing probabilistic 
distribution of the data. Given a PDF function :math:`f`, the probability that a randomly 
selected data point :math:`x_0` will be in some range of values :math:`a\leq x_0 \leq b` 
is given by the integral of the PDF over that range: :math:`\int_a^b f(x)dx`.
For a small value of :math:`\varepsilon` the value of the integral 
:math:`\int_a^{a+\varepsilon} f(x)dx` is close to :math:`f(a)\cdot\varepsilon`. 
Thus we can consider :math:`f(a)\cdot\varepsilon` as the probability that a randomly selected 
data point  :math:`x_0` is in the range :math:`a\leq x_0 \leq a+\varepsilon` (assuming again 
that :math:`\varepsilon` is small).

**Qiang asks:**

    Will our next project be about K-nn and probabilities?

More on KDE than k-NN, but yes, it will involve probabilities.   

**Linggan asks:**

    How many projects left for the semester?

2-3 more. 


**Mikhael asks:**

    Do you have any links to videos from youtube for example to explain kde again?

I don't have any links, but if you search the web you should be able to find some. 

**David asks:**

    What's the difference between Himmelblau's function and Rosenbrock's function?

These are different functions, often used to test optimization methods.   


**Ninghui asks:**

    Linear regression is a very important algorithm in machine learning. How do we make 
    sure what type of data is better to deal with by linear regression? For example, when 
    we used KNN to deal with moon data, the result isn't good.

I am not sure what moon data you are refering to, but linear regression has an advantage 
over regression done using k-NN since its results are easier to interpret. Linear regression 
is useful if you want to model data using certain types of functions. This includes 
linear functions but also some other kinds - polynomial, exponential etc.   


**Luca asks:**

    I guess we are going to do SQL soon. Are we going to use a specific program? 
    Or we can use our usual Jupyter notebook?

We will use Jupyter.

**Metin asks:**

    1. Given the fact that Python is an open-source programming language and that it 
    is gaining more and more statistical libraries (due to being used so much for data 
    science / analysis), do you think that it will make R obsolete? In particular, is there 
    a project to code all of the R libraries into Python? 

    2. Are all of the libraries of Python written using C (you made a comment about the fact that 
    we are using C indirectly through numpy)? How does that work (using one programming language to 
    write the foundations of another one)?

1. Python is already more popular than R, but it does not mean that R will be obsolete 
any time soon. There are many people who are using R and who invested a lot of effort 
to develop R code suiting their needs, and they will continue using R. I don't think 
that anyone aims to replicate all R libraries in Python. People create new libraries 
because thay see a need for some tools, not because a library exists in a different 
language. 

2. Not all Python libraries are written in C. Many are written in Python, some are using 
other languages. There are different ways of connecting Python and C code. For example, 
Python `provides tools <https://docs.python.org/3/extending/extending.html>`_ for writing 
Python extensions, i.e. libraries written in C that can be imported in Python code like any 
other Python library. As for using one language to write foundations of another language - 
the most commonly used Python implementation (the one we are using) is itself written  
in C.   


**Adrian asks:**

    Are there any other ways to represent line regression besides the methods we already saw ?

I am not sure what you mean by representing linear regression. Linear regression
is one of the machine learning tools.  

**Steven asks:**

    Will we do other regression models in the future?

No, there will not be time for it. 

**Haiyi asks:**

    I'm a little confused about the third practice question of the week, 
    how to calculate the accuracy of the predictions.

As usual: compute what fraction of predictions was correct. 


**Thinh asks:**

    The gradient descent algorithm is how we learn the weight by minimizing the cost function. 
    How do we know how many iterations we have to take and which rate of learning is suitable ?

To some extent it is a trial and error, but there some methods 
that help with it.  


**Michael asks:**

    What are some other fields where these types of data analytics (Like what we used to 
    predict whether a runner was male or female based on finish time) would be incredibly useful?

Predicting is a runner is a male or female is just an exercise, but the same techniques
can be used to make prediction e.g. if a patient will respond to some treatment or not, 
if a person brosing a website will click on some link or not etc. These are types of 
predictions that many people are really interested in. 

**Anna asks:**

    Are there any other types of files we will work on? We've done csv, json, html 
    and I was just wondering if theres more beyond that.

We will work with text files and files created by the SQLite database. 


**Farhat asks:**

    Will we have to work with 3-D or Contour plots for upcoming projects?

You won't have to use them, but they may be useful.  


**Jason asks:**

    Can the 3D plot work for any functions regardless of complexity? 

Not any function - the function has to have 2 variables. As far as 
complexity is concerned, if you can compute the function then you should be 
able to plot it. 


**Dakota asks:**

    Will our next project have to do with probabilities and predictions with KNN 
    or will it have to do with the plots we are learning about? 

Plots may be useful for the project, but the main tasks will deal with probabilistic 
models and linear regression.  


**Netra asks:**

    Could you go over choosing the right bandwidth again?

It would require too much writing to explain it here, but I can explain it 
e.g. during office hours.  


**John asks:**

    Are the projects that we do in this class reflective of what data scientists 
    do during their day-to-day work?

Data scientists deal with a lot of different tasks. The projects deal with some
tools and issues that data scientists work with, but not all of them. 


**bochun asks:**

    This weeks' content is easy to understand. And Now I'm imaging what will the next 
    project be. Since currently we are doing more coding, will the next project still 
    be a short one?

No, it will be a regular, longer project.  

