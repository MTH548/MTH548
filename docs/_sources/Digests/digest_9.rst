Weekly Digest 9
===============

**Saiful asks:**

    The probability things: The contents that you have provided on Thursday were defined by yourself. 
    So when we have to solve some problems probability related/Mathematical base have to define some 
    functions based on the problems. Will you provide sufficient materials for the next task/project? 
    More generally, can please explain shortly how kernel works as a response to this question or 
    in the class? 

    Is it possible to provide a grade statistics on each project, I believe it will help almost all 
    students to get idea about themselves and will try to do better?


I will talk more about kernel density estimates (KDEs) in class. It is not necessary 
to implement related tools from scratch. For example, as I have shown already, the 
:code:`gaussian_kde()` function from the :code:`scipy.stats` module computes KDE based 
on a given array of data.  

Since every report is graded using a letter grade, you can estimate your final grade by taking 
the average of letter grades from all reports (completion of weekly digest will affect the final 
grade to some extent too). However, here are the statistics for the reports graded so far:

| Report 1: 
| Number of submissions: 25
| Number of grades A-/A/A+: 11
| Number of grades B-/B/B+: 8
| Number of grades C+ or lower: 6

| Report 2: 
| Number of submissions: 27
| Number of grades A-/A/A+: 10
| Number of grades B-/B/B+: 9
| Number of grades C+ or lower: 8

| Report 3: 
| Number of submissions: 28
| Number of grades A-/A/A+: 11
| Number of grades B-/B/B+: 15
| Number of grades C+ or lower: 2

| Report 4: 
| Number of submissions: 28
| Number of grades A-/A/A+: 20
| Number of grades B-/B/B+: 6
| Number of grades C+ or lower: 2



**Linggan asks:**

    Which one is faster, JSON or dictionaries?

These are different tools. Dictionaries are a Python objects. JSON is a format 
for storing and transmitting data as text. JSON stings can be converted 
to Python objects (e.g. to dictionaries), and vice versa. 

**Cassandra asks:**

    Is there a final exam in this course? 

No.


**Luca asks:**

     Regarding the last project.  I am not sure and not remember well if you said it. 
     On Discord any user name has to be different? I.e., can there be two (or more) 
     users with the same name? 

All user names are unique. 


**Bochun asks:**

    what is the difference between 
    :code:`df[df['column'=='B' ] ['row1']=A`` and
    :code:`df[df['column'=='B']].replace(['row1'],'A')`
    what im trying to say is, when I want to change a value, 
    I can use replace function or directly assign it to a new value. 
    But the replace function often returns a warning and does not do the replacement. 
    I'm very curious about this.

Neither of these snippets is valid code. I guess in the first case the 
intention is to make the value in the column 'B' and row 'row1' equal to 'A'. 
This could be done using :code:`df.loc['B', 'row1'] = A`. On the other hand, 
:code:`df['B'].replace('row1', 'A')` will replace all values of the column 'B'
which are equal to the string 'row1' by the string 'A'. 


**Ninghui asks:**

    How to use KDE represent higher dimensional data?

Yes, I will talk about it in class. 


**Carter asks:**

    Will we go over Airflow and scheduling tasks with it>

No, the topic of this course is data analysis. 


**Steven asks:**

    Is there any data related course beside this one? (making my schedule for next semester)

Computer Science Department offers several such courses:
on machine learninig, reinforcement learninig, database management etc. 
In the Math Department MTH 450 Network Theory deals with concepts that 
are very frequently used in modern data analysis.   


**David asks:**

    Are other languages such as C ever used for data analysis? 

Some languages are more popular among data analysts than other, 
but any language can be used for data analysis, and many of them are. 
As for C, we are indirectly using it for data analysis in this course:
pandas library internally uses numpy, and most of numpy code is written 
in C.  


**Mikhael asks:**

    What are JSON parsers and tree builders?

These are tools that convert JSON-encoded strings into a data structure 
that can be used directly in a given programmimng language. In Python 
the :code:`json` standard library converts JSON strings into Python 
objects consisting of nested lists and dictionaries. 

**Jason asks:**

    What are some use cases for Kernel Density Estimation?

KDE gives an approximation of the probability distribution of data, 
which is of interest in all cases. It can be also used in other ways,
e.g. for classification of data. I started talking about it last week 
and we will continue with this topic, so it should become clearer. 


**John asks:**

    Are we going to have the lowest project dropped from our grade?

No.


**Michael asks:**

    Do you think it's ethical of Discord to keep a detailed log of 
    its users entering and exiting voice channels?

I don't know if Discord keeps such data (you can check their privacy policy). 
The JSON data for the project was collected using a bot added to a Discord server, 
not by the Discord itself. The users of the server were notified that the data 
was being logged. The data for the project was also anonymized to remove any personal 
or otherwise identifiable information.  


**Haiyi asks:**

    When using `pd.to_datetime(df['start']).dt.tz_convert("America/New_York")`, 
    the time can be converted to New York time. How does this function determine which 
    time zone this time is originally?

In the format `2021-02-11T18:40:51.96+00:00` the part `+00:00` indicates the timezone. 
In this example, it is the Coordinated Universal Time (UTC). For other timezones this value 
will show the amount of hours and minutes the timezone is either behind or ahead of UTC
(e.g. `-05:00` means 5 hours behind UTC, which corresponds to the daylight savings time in New York) 

**Farhat asks:**

    Will we have to work with Gaussian Kernels in an upcoming project?

Yes. 

**Qiang asks:**

    How many project will we have in next weeks?

Two or three more. 

**Meaghan asks:**

    What is the optimal way to sort the values of a JSON file and/ or sort a dictionary 
    based on the values in it.

To sort JSON data, you should convert it into a Python object, sort that object using 
Python tools, and convert back to JSON. To sort a Python dictionary :code:`d` according to 
its values you can use e.g. :code:`dict(sorted(d.items(), key=lambda x: x[1]))`.  


**Adrian asks:**

    What are the upcoming topics in this course will we encounter. Anything like k-nn and 
    k-means function again ?

We will go over kernel density estimates, Bayes classifiers, linear and logistic regression, 
naive Bayes.  These are machine learninig methods, so in this sense they are like k-NN and k-means. 

**Netra asks:**

    How do you use web scraping with pdfs? 

PDF uses entirely different data format than web pages. There are some  Python libraries for 
working with PDF files though.  



**Scott asks:**

    I noticed that there was ✨in the text for one of the websites we were scrapping. 
    Is there a way to implement unicode in python and if so does it have any applications?

Python 3 natively supports unicode. You can even use some (but not all) unicode characters 
in names of Python variables. As for applications, since unicode is routinely used, we often 
need to work with it and Python lets us do it. 


**Dakota asks:**

    Do you think that json files are a big part of the data science industry?

They are used very often. There are even some database systems (e.g. Mongo DB)
that are build around JSON-formatted data, as opposed to tabular data used by SQL 
databases. 

**Anna asks:**

    Since these are mini projects, will we use this in the future for larger projects?

In a sense yes. The next project will use the marathon data scapped from the web. 


**felix asks:**

    How often are data scraped from html pages like this in professional projects?

Some data analysis projects are based on data scrapped from the web, some use 
data from other sources. Both scenarios are common.  

**Griffin asks:**

    Will we be doing a project that takes advantage of these probability features?

Yes, the next one. 


**Metin asks**

    What resource (any particular textbook chapter or paper or simply the Wikipedia article)
    would you suggest to learn about kernels? 

If you search the web for kernel density estimate, you will see a lot of good resources. 
Wikipedia article on this subject is not a bad start. 





