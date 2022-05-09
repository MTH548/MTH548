Weekly Digest 13
================

**Anjali asks:**

    Will we be accessing the mySQL database?

No, for simplicity we will be working with SQLite 
databases only. mySQL would require setting up a database 
server. SQL queries are similar in both cases though. 


**Steven asks:**

    Can we join tables or do nested queries in sqlite?

Yes, it works in SQLite simalarly as in other SQL databases. 
I will explain how to do it this week. 


**Cassandra asks:**

    Is text classification the last project? 

There will be one more, but it is optional.

**Luca asks:**

    Generally speaking, SQL is used to retrieve information and creates tables. 
    Then, we can use pandas and so on in Python for working on those data frames?

Yes, I will explain how to do it.


**Saiful asks:**

    Text Classification project: Do we need to apply same procedure (not asking about Naive Bayes) 
    for both datasets?  Can we add some others stop words? 

Naive Bayes should be used for both. As for stopwords, sure you can add 
more as you see useful. 

**Linggan asks:**

    The last project is optional, will the grade be bonus or will the grade be replacing for 
    the lowest project grade

The final project grade will be the average of the first 7 projects or all 8 projects - 
whichever will be higher. 


**Ninghui asks:**

    If I pass the data to dataframe then deal with by python code. Is it more efficient?

I am afraid I don't understand this question - what is more efficient 
compared to what? 



**bochun asks:**

    What is the optional project due date? And for the exercises, will our grades be quantified 
    by how many exercises we complete? For example, 10/10 is A and 8/10 goes to A- etc.

It is due on Friday, May 20. I have not decided how to grade it yet since some exercises 
are easier, some more difficult. 

**John asks:**

    Is Python the most common used programming language to carry out machine learning tasks?

I am not sure if this is the most common, but it certainly is one of 
the most popular languages used for machine learning and data analysis tasks.  


**Michael asks:**

    Is there any other topics or projects you would have liked to discuss or talk about 
    that we didn't have time to in class?

There are many such topics: neural networks, random forests, PCA, non-SQL databases etc. 
Even for the topics covered in this course, there is much more that can be said about them. 

**Qiang asks:**

    What If I get a very low grade on the optional project, will it make my average go down?

No. 

**Griffin asks:**

    What do you think is the most important topic discussed this semester?

I would not call it the most important topic, but the pandas library has probably most 
immediate applications, so it is worth to be familiar with it. The most important lesson 
from this course is probably the general understanding how data analysis and machine 
learning work and how you can apply them to practical problems that you may encounter 
in the future. 


**Haiyi asks:**

    For this week's exercise 1, create a data frame where each row corresponds to a post. 
    I don't know how the column should list the name of the newsgroup, the author of the article, 
    the subject of the article and the body of the article.

We worked on it in class last week. It is also a question for office hours, 
but it would be difficult to answer it here in writing. String operations 
and regular expressions are tools that are useful for such tasks. 


**Carter asks:**

    What are some projects we could work on after this course?

It depends on your interests. You can try to learn more about machine 
learning, do something with web scrapping, experiment with data visualizations etc. 

**Scott asks:**

    Besides cases where there is a large amount of data that is too much to handle 
    for pandas, when else would SQL be favored over pandas and when would pandas be 
    favored over SQL?

Pandas is a tool for analyzing data. SQL is used by database system that 
facilitate data storage, security, access to data for multiple users etc. 

**Dakota asks:**

    Will we know our grades for the class right after finals week?

The final project is due at the end of the finals week. It will take me 
a few days after that to grade it and calculate the course grades.  

**Meaghan asks:**

    Is there a good visualization of the way the naive Bayes classifier would work 
    for something like the upcoming project? I am struggling to visualize what would need to be done. 

A confusion matrix (that I explained when we were working on classification of MNIST images)
can be a good way of visualizing accuracy of predictions. This is especially true for the newsgroups 
data since it involves multiple newsgroups. Word clouds that I showed in class provide 
interesting illustrations too.  

**Netra asks:**

    Does a bonus help with your overall grade or the grade for just that project?

A bonus gives a higher grade on a project. Since project grades will be used to compute 
the final course grade, this affects the overall grade. 

**Metin asks:**

    I might have misheard / misunderstood this but... when you talked about an SQL file, you mentioned 
    something about identifying oneself (the sqlite:///gradebook_data.sqlite command used in class). 
    You mentioned something along the lines of our command being shorter than usual because we can freely 
    access the file. Could you give an example of what a more complex access command might look like? 

In this course we are working with SQLite databases that are stored in single files on a local 
computer. Full-scale databases are stored on remote servers and require a user name and a password
for access. This is just an extra step in connecting to such databases.  

**Farhat asks:**

    Would there be a way to incorporate SQL queries into previous projects that we did? 

You could create an SQL database and store in it some data processed in pandas (I will explain 
how to do it in class). However, this would probably not be very useful for the past projects.  

**Thinh asks:**

    As we are entering the last week of the semester, which resources would you recommend as we go 
    further from this course?

It depends on what are your interests. There are a lot of online resources on machine learning, 
data visualization, natural language processing, web scrapping, database systems etc. 

**Anna asks:**

    We will be able to know our grades with without the optional project?

I will compute just one final grade, taking everything into account. If you want to know an estimate 
of your final grade, you can check your average grade from all projects completed so far. Projects are 
worth 90% of the final grade, the remaning 10% is based on the completion of these weekly digests.

**Jason asks:**

    Are there advantages to using SQL over Pandas?

Pandas is a tool for analyzing sets of data that are not too large in size. 
SQL is used by database system that facilitate storage of sometimes huge 
amounts of data, provide access to the data for multiple users, provide 
data security etc.

