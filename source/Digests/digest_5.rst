Weekly Digest 5
===============

**Luca asks:**

    What is the main difference between pandas and SQL? Are they interchangeable?

Pandas is a Python library for processing data, SQL is a language for accessing 
and modifying data stored in relational databases. These tools are not interchangable, 
and they are often used together (SQL to retrieve data, pandas to analyze it)

**Steven asks:**

    Will we incorporate Naive Bayes Classifier in our machine learning algorithm?

Yes, we should get to this.  

**Adrian asks:**

    Will future projects be done on only supervised data or will we also learn to handle 
    unsupervised data as well ? 

Do you mean unsupervised learninig algorithms? We already used one such algorithm (k-means). 
We may encounter some other ones in this course. 

**Jason asks:**

    Are we going to have a project that explores more of Pandas?

Yes, the next one. 

**Linggan asks:**

    Can we have a project report example so we know what the perfect report looks like.

Possibly. I would need to get the persmission of the author of such report to distribute it.

**David asks:**

    Why can't we just work with C instead of using Python which uses a library that uses C.

A program written in C will typically run faster than a similar program written in Python, 
but writing it will usually require much more time and effort. Libraries such as numpy aim 
to combine the best features of both languages - the speed of C and the convenience of Python.  


**Netra asks:**

    What kind of data visualization techniques will we be exploring?

More tools than techniques. We will work with seaborn and plotly this week. 


**Dakota asks:**

    Is there a ballpark time when the new project will be due?

Saturday, March 19, 11:59 PM.


**Metin asks:**

    We only had one class last week. There are some parts of the material that I need to go over to understand 
    so it does not make sense to me to ask "what does that do again" type of questions before I actually made 
    a genuine attempt at understanding. At the same time, there is nothing deeply conceptual about the pandas 
    library (at least based on what I know of it so far). Thus, as much as I would have preferred to avoid this, 
    I find myself forced to ask questions about the structure of the class. 

    1. If I recall correctly, at the beginning of the semester, it was mentioned that we would have 8 projects. 
       I was not able to find this number on the syllabus. Is my memory correct?

    2. If so, given the fact that more than 1/3 of the semester is over (5 weeks out of 14) but only 1/4 of 
       the projects have been submitted so far (2 out of 8), can we still expect that the total number of projects 
       will be the same? 

    3. I know that there is a part of the syllabus called learning outcomes and have read it. Could you please give 
       us a more precise breakdown of what to expect (pandas for another week, than x library to do task y for z weeks, etc.)? 
       This is in no way urgent and can wait spring break if you are overwhelmed. A negative answer is also fine :-)  

There is nothing wrong with asking questions about the course organization. 

1. I think I said 7 or 8. This is not set in the syllabus, since I want to have flexibility to adjust the 
   pace of the course as needed.    

2. Yes. This may involve a couple of smaller projects with a shorter completion time. 

3. We will finish pandas and work with some plotting libraries this week, then move on to web scrapping. This will bring us
   to the spring break. The schedule for the second half of the semester is to be determined - I know what I want 
   to do, I still need to plan when to do it. 


**Bochun asks:**

    Can we expect a lowest project be dropped from the final grade? Or some extra credit for some in class quizzes something 
    like that?

Report grades are not dropped. For every report you can get an A+ grade which gives an extra credit toward 
final grade computations. I assigned such grades to some students for the first and second report. 
There are no quizzes in this course. 

**Saiful asks:**

    Is there any technique to grouping the numpy array similar to the pandas? To accomplish the projects in this class 
    I need a huge time, can you please suggest how can I do it as fast as possible? 

Numpy does not have an equivalent to the pandas groupby method, but usually it is not difficult 
to split a numpy array into subarrays based on some condition. How to do it will depend on what 
specifically one wants to accomplish. 

I am not sure if by time issues you mean that it takes you a lot of time to write the code, 
or that the code takes a lot of time to run? If you talk to me and explain what is the problem 
I will try to help.   


**Cassandra asks:**

    Do you know or have a rough estimate of how many projects we will do this semester? 

We should have time for 7 or 8.  


**Scott asks:**

    Will gzip be used for the baby names project? Also, how many projects will we have total?

We should have time for 7 or 8 projects. Baby names data is zipped, not gzipped. There is 
a different Python library for working with zipped files. 

**Anjali asks:**

    What is SVM used for?

It is used mainly for classification and regression. 

**Farhat asks:**

    Can we pass columns as arguments to the groupby.apply function and if so, how? 

groupby.apply applies a given function to the whole dataframes returned by the 
groupby operation. You cannot use it with a different function for each column, 
but you can use it with a single function which processes each column in a different way. 


**Haiyi asks:**

    When I was writing the exercise, I found that my result was different from the check given 
    by the teacher, and I encountered some difficulties when doing exercise6.

The exercises use data provided by the seaborn library. This data has been changed 
a bit in a newer version of this library, so the results of the exercises may differ 
somewhat depending on the version of seaborn that you have installed. 

**Thinh asks:**

    Is there any chance we can have extra credit ?

On every project there is a possibility of earning an A+ grade for work that exceeds 
expectations. This increases the average report grade, and thus counts as an extra 
credit. 


**Mikhael asks:**

    In short and simple explanations how is clustering use to classify images of digits? 
    And how does KNN and KMeans relate to one another? KMeans is not used for making predictions 
    but KNN is?

K-means is used to cluster data, k-NN is used to make predictions. K-means cannot classify 
images (since it is not a classification method), but a part of the second project was to check 
to what extent the clusters it produces correspond to different types of images (e.g. if all 
images of zero will end up in the same cluster etc.).

**Qiang asks:**

    Could you tell us how to get an A+ in one project?

Write a good report and add to it something that goes beyond the expected content. 
I assigned A+ grades for both project 1 and 2, so this is not a grade that is impossible 
to get. 

**Meaghan asks:**

    Should the in class material be a direct hint to what we should be using to complete the current project?

Yes, each project is based on the material from the previous few classes. 

**John asks:**

    Will we do a project on neural networks in this course?

I don't plan on it. There is only so much that can be fit in a single semester. 

**Anna asks:**

    Will projects get harder from here?

My intention is that all projects should be more or less of a similar difficulty. 





