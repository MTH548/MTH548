Weekly Digest 12
================

**Jason asks:**

    Is there a drop for lowest project grade?

No. 


**Qiang asks:**

    Will you consider some extra bonus ?

You can get extra credit (i.e. an A+ grade) on any project report
as long as it includes some content that exceeds expectations. 


**Linggan asks:**

    How many projects are there left after the naive Bayes project?

There may be one more, but if so it will optional. 


**Steven asks:**

    Can we add words to the list of stop words provided?

Yes, for example adding 'movie' and 'film' to the list of stopwords used 
for the classification of movie reviews would be sensible.  


**Ninghui asks:**

    How to calculate probability for text file and how to classify them?

There are several methods for text classification, e.g. the naive Bayes that 
we used last week. 


**Griffin asks:**

    Is Text classification with naive Bayes the last Project?

There may be one more, but if so it will optional. 


**Adrian asks:**

    What other python specific functions will we use in conjunction with the new material 
    that we will be learning. And how would a naive bayes algorithm compare to the k-nn 
    algorithm at predicting words ?

We will work with SQL, including some tools that make it possible to use SQL in Python scripts. 
k-NN is not commonly used for text classification - it is difficult to say what a neighbor 
of a given text should be.  


**Saiful asks:**

    Is the  text classification last project? Besides SQL what are the topics we will learn 
    in the upcoming weeks? To be a proficient Data scientist/engineer which programming languages 
    (e.g. C, C++, FORTRAN )besides Python one should learn? 

1. There may be one more project, but if so it will optional. 

2. There is time for SQL only. 

3. For a data scientist knowledge of additional data analysis tools and techniques will be more 
important than knowledge of additional programming languages. As far as languages go though, 
R can be useful since it is used by many people who work with data.   


**Cassandra asks:**

    Will Text Classification be the last project? 

There may be one more, but if so it will optional. 


**Luca asks:**

    What is the best tool for sentiment analysis?

There are a lot such tools - some open source, some commercial. They have different features and 
I don't think there is one clearly better than all others.


**Haiyi asks:**

    I am confused about how to use naive bayes with Laplace smoothing to calculate probabilities.

We will continue working on this in class on Monday. Just let me know what you 
find confusing and I will explain.   


**Anjali asks:**

    What are some of the other ways the naive bayes can be applied?

Naive Bayes can be used in all cases when we try to approximate probability distribution
of data that consists of multiple features. It is not the most accurate way of computing 
probability distribution, but it is relatively easy and it works in cases when it would be 
difficult to find probabilities by other means. 


**Michael asks:**

    With Data Scrapping and Naive Bayes Classifier, would it be possible to create a fact checker?

It is possible to automate some aspect of fact-checking, but I don't know if 
there are any currently available tools that would let one build a reliable computer-based 
fact checker. Anything like that would require much more sophisticated tools than naive Bayes.


**Mikhael asks:**

    Is it possible to use Bayes Theorem, KDE, and K-NN analysis to predict if a given day it will rain 
    based on past data for the same week?

Yes, but there is always an issue how accurate predictions we could obtain in such way. 
The current meteorological models would most likely perform much better. However, it is an interesting project. 


**Bochun asks:**

    How to add axis labels to KDE plot? When I use plt.xlabel('str'), it returned an error said 'str object is not callable. 

:code:`plt.xlabel()` should work. I would need to see your code to tell what generated 
the error. 


**Carter asks:**

    Will the project for SQL be extra credit? Worth 5 or 10 points?

If there will be a project on SQL it will be optional. I have not decided on it yet. 


**Dakota asks:**

    Would the class notes be available to look back on when the class ends or will we have to download them to have? 

There will be available until the next spring semester. The source files of the website 
are also available on `GitHub <https://github.com/MTH548/MTH548_site>`_.


**Scott asks:**

    Will there be a project after the naive Bayes project?


There may be one more, but if so it will optional. 


**Thinh asks:**

    We already learn how to scrap the data. Can we auto the process, such as make 
    it continuously scrap the weather data daily in real time?

Yes, you would just need to run the web-scrapping script automatically as often as 
you want. You can use your own computer for it or you can host the process 
using one of online services such as www.pythonanywhere.com.


**John asks:**

    Is the Text Classification project the last one of the semester?

There may be one more, but if so it will optional. 


**Anna asks:**

    Is training data really that necessary?


Some problems can be solved without relaying on machine learning and training data. 
For some other problems, the best way is to use machine learninig methods. Such methods 
require training data to work.


**Meaghan asks:**

    For reports, should we be drawing all of our conclusions specifically in the conclusion 
    section of the report or is it ok to do them by individual section and recap at the end?

It is fine for conclusions to be scattered through the report. The main goal 
is to create an interesting, well-written narrative. 

**Farhat asks:**

    A question I have always wondered is: Are the Python Machine Learning Libraries the same 
    functionality as the ones we create? As in, if our code implementation works for a specific algorithm, 
    is that the same way the Library Algorithm import would work (eg, if we created our own Bayes 
    Theorem Algorithm, would it work the same as the Python Machine Learning Library version?)

The basic principle will be the same, but libraries such as sklearn will implement 
algorithms with some optimizations that can make them faster. Tools included in such libraries 
usually also allow for optional argument that let a user fine-tune working of the algorithm.  

**Netra asks:**

    Why does the naive bayes algorithm assume observations are independent to each other?

This is a simplification. If we can't compute something more accurately, we make 
this independence assumption and hope that the results we obtain will be still close enough 
to being right that we can use them for something useful.  

