Weekly Digest 3
===============

**Saiful asks:**

    Do you have any plan for assigning long projects and possibly group project? 

Future projects should require similar effort as the first one. I don't plan 
to assign group projects. 


**bochunde asks:**

    what will be the next project focusing? we did a lot machine learning stuff these weeks, 
    will we gonna continue around this? and related to this week's content, I'm still confused 
    about the part I of the project.  In part I we are asked to build the k-nn function. 
    So is that necessary to use make_blobs to test its functionality in part I? Because I've run my 
    function on MNIST data and it worked just fine.

The second project is already posted on the course website, you can have a look. 
For the next topic, we will take a break from machine learning and work with 
pandas library. 

You don't need to test the knn function with :code:`make_blobs` data in the report, 
as long as you are sure that the function works correctly. 


**Cassandra asks:**

    Outside of the MNIST and recognizing digits, what else would k-NN be used for? 

k-NN can be used to classify any type of data. One can try to use it e.g. with  
medical data to predict which people are sick with some disease and which are not, 
or with data on used cars (car model, age, milage etc.) to predict the 
price of a car. In some classification problems k-NN will work well, in other 
cases different tools may be better.  


**Griffin asks:**

    With ipywidget, we only explored drop down menus, sliders, and checkboxes. 
    Will there be more complex elements that we will be using, like an input box 
    for typing out an input or other interactive features?

I may use other features if they will be useful in this course. You can also have 
a look at the `ipywidgets documentation <https://ipywidgets.readthedocs.io/en/latest/>`_ 
to learn more about them. 


**Luca asks:**

    During the class, you mentioned that it's better for timing reasons to avoid loops in Python 
    and use direct methods of the NumPy library. May this latter case create a problem of memory though?

It depends. Python objects typically take more memory than numpy datatypes, so a Python list 
will usually occupy more space than a numpy array with the same values. However, vectorized numpy 
computations sometimes create temporary arrays that would not be needed if one wrote an equivalent 
code using loops. In most cases numpy will be still much more efficient, but it is something to keep 
in mind, especially when dealing with large amounts of data. 


**Felix asks:**

    is K-NN more or less parallelizeable on some form of GPU, than a 'conventional' neural network.

It is difficult to compare which method is more parallelizable, but it is 
certainly possible to parallelize k-NN. 

**Netra asks:**

    Do most assignments focus on ML applications?

About half of the assignements should involve some machine learninig tools. 

**Steven asks:**

    Is it possible that we can get a 5 minutes break in the lecture? 

Let me think about it. 

**Adrian asks:**

    What are the pros and cons between the k-nn and k-means algorithm ? 

These algorithms serve different purposes. k-NN is an algorithm for predicting 
data labels, while k-means is for data clustering. 

**Linggan asks:**

    Will there be any projects that will not be done with python?

No. 

**David asks:**

    Will we ever be required to write a machine learning algorithm.

You already implemented one such algorithm (k-NN) for the first project. 
There will be other projects where you will need to implement different 
algorithms. 

**Dakota asks:**

    Is there a way to get one on one office hours during the week? I just want to make 
    sure I understand the current course material and on track for the rest of the semester.

So far my regular office hours were attended by few students, and I had one on one 
conversations with everyone who showed up. If this changes and the regular office 
hours will become busy, I may try to schedule additional times.  


**Scott asks:**

    I was wondering if there are any tips to making code more efficient and take less 
    time to run, and avoiding using loops. Is using widgets more efficient? Also, is 
    clustering better for more applications than k-NN?


Widgets are adding interactivity, but they do not make any more computations more 
efficient. Using numpy tools, on the other hand, can speed up the code a lot. Clustering 
has different goals than k-NN. The goal of clustering is to organize data in some groups 
in a possibly useful manner. k-NN is a used for classification: it predicts which label 
should be assigned to a data point. 



**Metin asks:**

    1. Given that "each project will have a weight of up to 10 points, with 10 points for more 
    work-intensive projects", can we assume that this was actually one of the longer projects of 
    this semester or is it 10 points mainly because it is the first project?

    2. Will we learn about the type of algorithm appropriate for clustering crescent moon like shapes 
    in this class?

1. The first project was one of the larger project. There may be 1-2 smaller project that will only
involve writing some code, with no narrative or analysis. 

2. I don't plan to talk about other clustering algorithms. We will be mnoving to differrent topics 
instead. There is only so much that can be fit in a single semester. 

**Jena asks:**

    For the projects, can we get a bit more information on the logic and implementation of it in the general 
    sense? (What this code can be used for, why, and how?)

I am trying to provide such information. It something is confusing or needs to be explained 
in more detail, please just ask me to clarify. 


**Thinh asks:**

    As we know, KNN algorithm helps us to classify the labels of the new datapoint. How about Kmean, what 
    is its purpose? Would you mind giving more examples about it?

K-means is a clustering algorithm, whose goal is to subdivide data into groups. One example 
of its application we have seen already was clustering colors in image. You will also use this 
algorithm for the second project. 


**Haiyi asks:**

    Outliers or interfering data will have a greater impact on the mean, resulting in a center shift. 
    How do we detect outliers to optimize the algorithm.

Do you to optimize k-means algorithm? Typically you do not discard the outliers in order to apply 
this algorithm. Once you perform clustering you can actually define that outliers are points that 
are far away from all clusters centroids.

**Farhat asks:**

    Moving forward, will we be allowed to utilize databases that have specific functions written for us in 
    our project or will we be expected to always create our own specific functions for the task at hand? 

In depends. For the next project, for example, you will be able to use k-NN and k-means functions 
implemented in the sklearn library.  

**Anjali asks:**

    How much analysis of our project is "enough"?

I will be indicartion what questions you may want to explore for each project. If you investigate 
in some depth a couple of such (or equivalent) topics, it will be enough. 

**Ninghui asks:**

    I have question about last project. If I pass all 60000 data to code, it takes long time to get 
    prediction value. Is there any way I can improve?

The second project will in part deals with the problem how to make k-NN faster without sacrificing 
its accuracy too much.  

**Mikhael asks:**

    I'd like to make the kNN algorithm a bit interactive similar to the Google quickdraw where the user 
    f the algorithm gets a 6x6 or NxN grid window with white tiles and they can use their cursor to create 
    the data point as a number. The grid has a box for each pixel of the data point. How can I go about 
    doing this since it is like a GUI element with Python?

You would need to create a GUI interface. There are many Python libraries that can be used 
to do it in various ways. Even matplotlib has tools for creating simple interactive plots that 
may suffice for such an application. You can also use e.g. the kivy library to create an interface 
usable with tablets and smarthones. 


**Qiang asks:**

    How many patterns have to be worked out for a project?

I am not sure what you mean. How many topics you should explore? A couple should be enough, or even 
one researched in some more depth. 


**Michael asks:**

    What is the difference between the K-NN and K-Means algorithm?

These algorithms serve different purposes. k-NN is an algorithm for predicting 
data labels, while k-means is for data clustering. 





