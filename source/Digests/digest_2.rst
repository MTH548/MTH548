Weekly Digest 2
===============

**Cassandra asks:**

    Is there a word processor that you would recommend for writing the project reports? 

Project reports need to be submitted as Jupyter notebook files, so it is easiest 
to prepare them using Jupyter notebook. 


**Saiful asks:**

     In k-NN project work, if someone does not  consider all the questions you mentioned 
     in the project instruction, will it be cause to reduce the points? 

The specific questions are just suggestions what you may include in the reoport. You 
can select 2-3 of them and develop them. You can also come up with some other topics 
that seem interesting to you. 


**Netra asks:**

    What do you mean by "neighbors" in the project (part we're returning along with 'label')? 
    How many neighbors does it return and does that come from the training data?

Training data is organized into a two dimensional array, where each row represents one 
data point (e.g. one image). The :code:`knn()` function should return row numbers of 
the nearest neighbors that were used to predict the label. Neighbors are always elements 
of the training data. The :code:`knn()` function is supposed take an argument :code:`n` 
which specifies the number of neighbors used to make the prediction. The number of neighbors 
returned will be determined by this value.   


**Bochun asks:**

    Currently I am working on let the k-nn function be able to recognize both hand written and 
    typed numbers. So far all the data set is based on MNIST database, which are well-organized, 
    but in actual application, the data will never be that perfect, in this case, I expect 
    my function be able to pre-process the images and then run through the k-nn function. 
    And that is where I stuck. In short, typed number are obviously looked the same as hand 
    written one-they are obviously in the same category. However, such 'obvious' will not be accepted 
    by computer, so I'm now trying to improve this.

It is true that data typically needs to be pre-processed before it is used in machine learning. 
For example, MNIST images were processed so that they are of the same size, and that the writing 
is positioned in the center of the image. 

To recognize images of typed digits you should use training data consisting of images of typed digits, 
and not handwritten ones. If the images you want to recognize use a specific font, then the training data 
can be small. Even one image per digit should suffice, since the each typed digits will look exactly 
the same every time it appears. 


**Griffin asks:**

    Will we be exploring other types of machine learning?

Yes. 


**Metin asks:**

    For people who do not have a computer science background, do you have a recommended 
    resource to quickly learn to write more efficient code (by that, I mean code that is 
    faster to run)? Do we necessarily have to take an algorithms & data structures class, 
    have a lot of experience coding different projects, or are there a few concepts that 
    we can easily and quickly learn that would significantly increase our capacity to write 
    more efficient code?

Knowledge of algorithms and data structures is certainly useful if you 
want to code efficiently, but this is also a matter of practice. 
For example, an appropriate numpy tool can often let you complete 
a complex looking task in a couple of lines, but numpy is a large library so it 
takes time to learn it.   

If you think that a particular snippet of your code is not elegant or not efficient, 
it is often useful to search the web to see how other people performed similar tasks. 
You are not allowed to copy somebody elses code in your project reports, 
but there is nothing wrong with reading code written by other people and trying 
to understand how it works. You can also ask for suggestions on how to improve your code 
either in class or during ofice hours.


**Adrian asks:**

    Can the K-NN model be explored more in how it can be applied more in real life ?

We will be working with k-NN again for the second project. 


**Mikhael asks:**

    Is there a library or way to draw within a 3x3 or non grid the number digitally that we 
    want to input to the ML Algorithm to classify? I’ve seen it done before but definitely 
    would like to learn how to implement it since I have a stylus and pen but could even be 
    done with a cursor. 

This can be done using various tools. For example, you can have a look at 
`this tutorial <https://kivy.org/doc/stable/tutorials/firstwidget.html>`_ which shows how one 
can create a drawing widget using the kivy library. 


**Farhat asks:**

    I'm not sure if this was discussed in class, but could the :code:`from sklearn.datasets import make_blobs` 
    code be interpreted as real data or is it simply a randomly generated set of data? Could we utilize 
    this in our project or would we have to implement our own set of data?

The function :code:`make_blobs` creates data randomly. The main objective of the first project is to work 
with MNIST data. This is real data, consisting of samples of handwritten digits. 


**Thinh asks:**

    Regarding the problem of choosing K neighbors in the KNN algorithms, what factors will affect 
    the numbers of K?

The number of neighbors in k-NN is a parameter. In different settings a different number of neighbors 
will give the best results. As a part of the first project you can experiment to check which number 
of neighbors will work best for recognizing MNIST images of digits. 

**David asks:**

    How much are we expected to write for our project analysis?

I will talk about it in class. 

**Jason asks:**

    When dealing with KNN, is it different from traditional ML algorithm in that there is no training/testing 
    stage of the pipeline?

k-NN is a non-parametric machine learning algorithm. There are other algorithms that are parametric,
which roughly means that before they can be used, they compute some parameters (say, neuron weights in 
case of neural networks). There are many parametric algorithms and many non-parametric ones. k-NN 
is not special, it just belongs to the latter class. 


**Steven asks:**

    Will we use the panda library in python later on in this course?

Yes. 


**Anjali asks:**

    Will we be working primarily with machine learning techniques throughout this class?

Not exclusively. There will be also some data processing, web scrapping, data visualization 
etc. 


**John asks:**

    I was thinking about if we can use neural networks to predict whether or not athletes will 
    become injured. For example, could we gather data, and using the injury data and other relevant 
    data points train a neural network to predict if athletes will get injured? It would probably 
    hold a certain economic value. 

I think the only way to answer this would be to try to implement it and see if it can give useful 
results. One challege, I imagine, would be to get enough training data. There is also the question 
what should the training data be, i.e. what variables should be used to make the predictions. 


**Qiang asks:**

     Are there other ways we can check the accuracy of predictions?

There are many ways of measuring prediction accuracy. Which ones are useful will depend 
in part on what you want to predict. 


**Linggan asks:**

    Are we allow to use the functions that we discussed in class for project 1?

Yes.


**Carter asks:**

    Are we allowed to put our reports on our personal website? Github?

Yes. My only request is that you do not mention that these are reports from this course. 
It is diffucult to come up with new projects each year, so I would prefer if these 
reports do not come up at the top of Google results when someone searches for 
MTH 448/548. 


**Meaghan asks:**

    What are some of the most important python topics to have a grasp on for this course?

The goal of the course it to teach about data processing and analysis, and 
about Python tools that help with such tasks.   


**Jena asks:**

    Could this be expanded into things like AI image processing?

I am not sure what you mean by "this", but if you mean k-NN classification, then it depends 
on what particular applications you have in mind. k-NN may be useful for some tasks related 
to image processing. 


**Haiyi asks:**

    Are there differences and calculation errors in the two formulas for calculating distances? 
    When the two calculation methods are different, how do we eliminate such calculation errors.

I am not sure what you mean by calculation errors. In k-NN you can use different ways of 
calculating distances between data points. Which method is the best may depends on the data 
you are dealing with. As a part of the first project you can experiment with what works best 
for the MNIST data. 


**Anna asks:**

    Will we be using ai in this course? I already consider this project ai. 

Machine learning is considered to be part of artificial intelligence, 
and k-NN is a machine learning algorithm. Thus this first project indeed 
deals with AI tools. 


**Dakota asks:**

    Are we going to have time during class to work on the project? Also is there anyway 
    we can ask for individual help outside of office hours? 

Most of the class time last Wednesday was spent on the individual work on the project. 
I plan to schedule some class time for work on future project too. 

It is best to ask for help either in class or during my office hours. I may be able to meet
at other times too, but it is a busy semester so I can't guarantee it. You can always ask 
though and I will see what I can do.  



