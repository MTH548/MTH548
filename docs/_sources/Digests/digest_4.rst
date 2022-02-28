Weekly Digest 4
===============

**Ninghui asks:**

    Pandas is no less than Numpy in terms of visualization and convenience, or Pandas seems better. 
    Why does numpy seem to be used more? Is there anything better for us to learn about Numpy?

Numpy and pandas have different purposes. Numpy is primarily for numerical computations, 
pandas is for manipulating any sort of data arranged in tables. Numpy is a more basic package, 
in the sense that large parts of pandas functionality is build on top of numpy. Pandas is not 
better than numpy. It is better for some applications, but numpy is better for different ones. 

**Anjali asks:**

    What are some other machine learning algorithms other than knn and kmeans?

Too many to list. Random forests, support vector machines, neural networks, various methods 
for clustering, dimensionality reduction, regression, manifold learning etc. We will work 
with few more machine learning tools in this course. 

**Jason asks:**

    What is the pros/cons of using KMeans compared to other dimensionality reduction algorithms, 
    such as PCA.

What will work better depends on the data you are working with and what you are 
trying to accomplish. In general, PCA results will be easier to interpret than 
dimensionality reduction done with k-means. But in some applications k-means 
may be a better tool. 

In general, it is not easy to answer questions what works better. There is a lot 
of ongoing research that deals with such problems, but its results usually suggest 
what may work better in certain circumstances. 


**Mikhael asks:**

    Will we learn about CNN models w Keras this semester? Is it correct to say so far the machine 
    learning algorithms we have learned like kNN & kMeans are ‘non-AI” algorithms as in there isn’t 
    any actual learning and creation of new knowledge after training?

I don't plan to talk about neural networks in this course. k-NN or k-means are not 
'non-AI' or 'less-AI' than other machine learning algorithms. There are various ways 
of classifying AI tools, and you can use them to distinguish, say, neural networks from k-NN, 
but it does not mean that one of these methods belongs to AI and the other does not. 
They both do.  Also, when you finish training e.g. a neural network, then the network will 
stop learning. Thus there is no difference in this respect. 


**Linggan asks:**

    How do machines self learning?

Machines do not self-learn (at least not yet). You need to provide them with training 
data, and some code which specifies how to extract information or compute some 
parameters based on this training data. When this training process is completed, the 
computer may be able to use the information it acquired to perform some tasks
using new data that it have not seen before.


**Bochun asks:**

    I am curious about the project grade. On the first project report, you mentioned that 
    my code is taking longer time than it should be because I'm using python's built-in data structure, 
    and it will be much faster using numpy library. My question is, what cause they perform different? 
    To be honest, They looks very similar when I use them.

Numpy code is written mostly a C which is a language more difficult to work with than Python, 
but in some situation much faster than Python. In order to see benefits of numpy 
performance you need to structure your code appropriately, in particular 
avoiding Python loops. 

If you don't see a difference between performance of numpy-optimized and non-optimized code, 
then you can show me your code (e.g. during office hours) and I will check why. 


**Luca asks:**

    Maybe I missed it during the class.... Did you tell us a particular criterion to reduce dimensionality 
    of the dataset in the project? or we just should experiment by ourselves. Thanks.

Dimensionality reduction should be done using k-means. How many clusters you should use (i.e. 
how many dimensions the data should have after the reduction) is something you can experiment with. 

**Farhat asks:**

    Could we have imported Pandas and used that library to create a dataframe in our first project involving 
    the KNN Algorithm? 

It would be possible, but not really useful. You could store MNIST data in a pandas dataframe, 
but then this dataframe would need to be converted into a numpy array in order to apply k-NN to it.   

**Cassandra asks:**

    While we were working with datasets and pandas, I noticed a lot of similarities to excel. Are there certain 
    instances where jupyter/python is more beneficial to use? 

Yes. Pandas offers more tools for manipulating data and you can combine these tools with the content of
any other Python libraries. Also, once you write a script with pandas you can use it over and over again, 
automating data processing. Some of this automation can be achieved using Excel macros, but writing macros 
is comparatively a more complicated process. Finally, you don't need to choose between Excel and pandas. 
You can open an Excel or csv file using pandas, perform data processing or analysis, and save the results 
in an Excel file. 

**Scott asks:**

    Should/could we include the elbow method for Project 2 or is that for a future project?

You could experiment with it to see how it works with the MNIST data (or some part of the MNIST data, 
e.g. images of a given digit). I am not sure if it will be of use in future projects. I showed it 
as an illustration of how one can try to find the optimal number of clusters. 

**Thinh asks:**

    Will it be able to show some good work as an example in class so we can improve our work this time ?
    (you can hide the name)

I will think about it, but in any case I would do it only with permission of the author of such 
a report. 

**Jena asks:**

    is pandas similar to dictionary?

You could find some similarities between dictionaries and pandas series (e.g. you are accessing series values 
using key in the series index), but these are really different structures. 


**Qiang asks:**

    Did anyone get A+ for last project?

Yes. 

**Meaghan asks:**

    What do you recommend as the best way to investigate data in a project and make sure that we are making 
    insightful discoveries with the data we are given?

State precisely what questions you want to research in your report, investigate them while explaning 
what you are doing, and describe results of your investigations. If you have more specific questions, 
please talk to me either in class or during office hours, tell me what you are planning to do or what 
you are unsure about, and I will do my best to help.    


**Michael asks:**

    Will our next project be using data frames?

Yes.

**Dakota asks:**

    Is it possible to send a finished project to you in the middle of the week to make sure it is in top 
    shape before turning it in?

I will traveling most of this week (thus no class on Wednesday), and I may not be able 
read the draft and respond. I will have office hours at 4:00-5:30 on Saturday, and 
I can to have a look at your report at that time and possibly offer suggestions. 

**Saiful asks:**

    You know that same tasks (code related) can be done in many different ways, but all are not efficient, 
    some need more time than others, some do not look good. What are the ways of solving a problem with 
    the most efficient coding? 

I don't think that there is a general rule for this. Knowing various libraries helps, since 
they may include optimized tools for a given task. Going deeper, it is sometimes helpful 
to know how Python and its various libraries are implemented, 
since then you can understand what will perform well and what may be a bottleneck. 
And of course it is good to know various algorithms, since a right algorithm can make 
a difference between a code that takes forever to run and a code that finished almost instantly.

**Haiyi asks:**

    I feel that data processing that can be done with Pandas can also be done with Numpy, and I would 
    like to know what is the difference between the two tools.

Pandas includes some specialized tools that are useful for processing data but are not 
implemented by numpy. For example, the dataframe groupby method that I will be talking about 
on Monday does not have a numpy equivalent. The same applies to various dataframe merging
operations that we will be looking at next week. 


**Metin asks:**

    Let me preface my question by stating that I understand that since the semester only has 14 weeks, there 
    is a choice to be made about topics to be covered and the topic below may not be among those topics.
    For part 2b of project 2, would an alternative way to reduce dimensionality be to work with the principal 
    components? If so, in theory, are there a set of conditions that result in the two approaches (reducing 
    dimensionality with K-means vs. reducing with PCA) having the same answers or do they typically give different 
    answers?


PCA is a common dimensionality reduction method, so it could be used in place of k-means. 
I expect to to use k-means in this project, but if you would like to compare the results 
with ones obtained using PCA, feel free to do it.  

In most cases these two approaches to dimensionality reduction will give different results, 
since they use entirely different methods. PCA is using an orthogonal projection of the data, 
while k-means is measuring distances of points to cluster centers. If the data does not naturally 
split into clusters, the results returned by k-means may change each time you run the algorithm, 
since k-means starts with a random selection of initial cluster centers. On the other hand, PCA does 
not depend on any random choices, so it will give the same results every time (except for very 
special cases when the data has the same variance in different directions).

**John asks:**

    How would someone go about creating their own dataset instead of using the MNIST default ones?

It depends on what dataset you want to create. If you want data similar to MNIST, then you 
would probably need to do it the same way MNIST was created: gather writing samples from
a lot of people, and then clean the data so that it is easily usable. 

**Anna asks:**

    Will our next project be similar to the first two? Or a completely different one

It will be different - it will involve no machine learning (unless you find a way to use it), 
but it will require pandas.   

**Netra asks:**

    I didn't quite understand part 2b of the project. How is that reducing dimensionality of the data?

I showed it in class (see my notebook from week 4). After clustering training data, you can transform 
the data replacing each data point by the array of its distances to the centroids of all clusters. 
The transformed data will have as many coordinates as the number clusters you created. For example 
if you use this approach with the MNIST data (which originally has 784 coordinates) and use 100 clusters, 
then the transformed data will have 100 coordinates. Thus the dimensionality of the data will be 
reduced from 784 to 100. 



