Weekly Digest 11
================

**Saiful asks:**

    Will we learn SQL databases in next classes? Is it possible to discuss the stochastic 
    gradient descent? You know that reaching to local min in gradient descent is big issue,  
    I know that in ML this issue is overcomed anyhow, but do not how. Can you please briefly explain it? 

We should get to SQL next week. Schochastic gradient descent is a regular gradient descent, 
but applied to a cost function which depends on a lot of data. In such case the data is divided into 
batches, and different interations of the gradient descent algorithm are using cost function computed 
using different batches. The goal is to make the whole process faster. 

There are a few different ways of dealing with local minima. One is to design machine learning algorithms 
using functions that have only one local minimum. It this is not possible, gradiant descent is sometimes 
run several times for a given function with different starting points, with a hope 
that one of these points will result in reaching the absolute minimum or something close to it. 


**Qiang asks:**

    Will we have one more project behind the string operation project?

Yes, the next one.  


**Griffin asks:**

    Will regular expressions be in the next project?

They will be useful for a part of it. 


**Ninghui asks:**

    Can linear regression make the results more precise by adjusting certain parameters? 
    For example, the choice of the number of neighbors in the KNN algorithm.

There are really no parameters of linear regression similar to the number of neighbors in 
k-NN. However, there are variants of linear regression that have such additonal parameters:
ridge regression, LASSO, elastic net etc.


**Luca asks:**

    I know the book Python Data Science Handbook. Do you have other suggestions?

It depends what suggestions you are looking for - general machine/statistical learning, 
particular tools (neural networks, linear models, ...) Python data analysis tools etc.?
"The Elements of Statistical Learning" is a good introduction to theory and applications
of machine learning. 

**Linggan asks:**

    What situation does KDE most use for?

KDE is used to estimate probability distribution of data. This can be then applied 
in various way: for data classification, clustering etc. 


**Cassandra asks:**

    What are some other machine learning algorithms other than knn?

We have seen some of the in this course already: k-means, KDE, linear regression. 
There are many others. 


**Carter asks:**

    It seems like we will be going into sentimental analysis soon. Can someone perform 
    sentiment analysis ethically?

I guess it depends on the character of the data. We will be working with 
movie reviews. I don't think that this will be controversial. 

**Scott asks:**

    What does the "core" mean in pandas.core or "Ipython.core.display"?

In both of these cases it indicates sublibraries that implement the most 
basic functionality of pandas and IPython, respectively. The rest of these 
libraries build on this functionality.

**Michael asks:**

    What are some tools that data scientists work with that we aren't able to 
    discuss in this class?

Neural networks, decision trees, random forests, support vector machines, 
principal component analysis, Gaussian processes, and many other.  


**bochun asks:**

    I did exercise 2, the regex. I found it hard to understand at the beginning, 
    and it took me a long time to search for the related syntax and their meaning. 
    Did the regex syntax also works in other programming languages? For example, 
    in python we use '\d' to represents letters, will this syntax be different in Java or C++?

Regex may vary somewhat in different languages, but its basic syntax is usually the same. 
In particular :code:`\d` represents a digit in Python, Java, and C++.  


**Adrian asks:**

    What are some pros and cons using the gaussian model compared to other models ?

This will depend on what data you are working with and what you are trying 
to accomplish.  


**Netra asks:**

    Can beautiful soup do what regex does or can you incorporate regex into 
    beautiful soup?

Beautiful Soup is for parsing HTML and XML documents. It does not replace regex. 
Regex is sometimes useful for scrapping information from websites, in addition to  
Beautiful Soup. 

**Thinh asks:**

    About regular expression, what is the application of using them and will we have 
    a project related to it ?

As for applications, I explained them in class: regex is used to process text. 
The next project will use it in part.  

**Anna asks:**

    Can regex ever be used for decryption?

Decryption of ciphers? It may be used to help with some processing of the cipher 
text, but not to actually decrypt a cipher. 

**Jason asks:**

    Do we have one more project left?

Probably two. 

**Dakota asks:**

    Will we be having a project based on regular expression? Especially String operations and such?

This will be useful for the next project.

**David asks:**

    Will there be a project based off regex? I'm really interested in getting good at regex.

Some regex will be useful for the next project. 


**John asks:**

    Is there another course that follows this course? For example, MTH 337 was the pre-req 
    for MTH 448, is MTH 448 the pre-req for any other course?

Not really, but the Computer Science Department offers several courses on machine learning, 
reinforcement learning etc. They develop further some topics mentioned in this course. 


**Farhat asks:**

    What is the difference between r.findall() and Raw String / re_show()?

:code:`re_show()` is a simple function I wrote to visualize regex matches. :code:`re.findall()`
is a function implemented in the :code:`re` library that returns regex matches found in a 
given string. Raw string is a type of Python string that does interprets backslashes literally, 
and not as parts of special character sequences.   

**Meaghan asks:**

    Is there a best recommended way to compare the accuracy of our predictions of parts 1 and 2 
    of the current project?

Compute the accuracy of predictions obtained each way and compare the results. 


**Metin asks:**

    Is the purpose of the regular expression package to perform text mining or is it for the exploratory 
    data analysis phase of study about a text ?  

It can be useful for both of these tasks.  

