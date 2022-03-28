Weekly Digest 7
===============

**Saiful asks:**

    Project 3:
    I think there are very shortcut command which can do the task that were assigned in the project 3. 
    But It takes me to think in a long way sometimes using loop. It would be better if you do provide 
    complete solution/ at least some command lines after the project submission dead line (This request 
    is for all projects). 

    Next project you are going to assign, will be like in text mining?
    The projects so far we completed were short/long project? 

As a general principle while using pandas and numpy libraries you should think how to 
avoid using loops, since these libraries provide tools that can usually perform equivalent
computations more efficiently without explicit iterations. 

I have been showing examples how to use pandas and numpy in this vectorized way in class. 
I am also happy to give more suggestions, either in class or during office hours. 
I do not plan to provide code for past project reports, in part because in some 
projects (e.g. the baby names project) are open-ended and you can choose what you want to 
do with them. 

We will work on a project related to text-mining. 

The projects you completed so far are the longer ones, the next one will be shorter. 


**Ninghui asks:**

    There are many useless things in the code of web pages, how to get rid of these things? 
    There are many pictures on the website, can I get these pictures by request? What sites 
    contain large amounts of data that can be extracted by request?


Libraries such as Beautiful Soup are specifically designed to make it easier to retrieve 
relevant information from webpages. You can download images from a website: retrieve links 
to image files using Beautiful Soup, then use requests to download each image, and then save 
it to a file.  


**Steven asks:**

    Are we going to do a project about web scrapping?

Yes, the next one. 


**Cassandra asks:**

    Are we going to explore machine learning again?

Yes. 


**Metin asks:**

    1. The code that we write to retrieve information from a website very strongly depends 
    on the design (source code) of the website. Is there a way around this? If we want 
    to reuse the code that we wrote at a future date, do we just have to pray that 
    the website's design has not been changed fundamentally? 

    2. I would assume that the information of a directory is first available on an offline document 
    (maybe a csv file) and then gets put on the web. Does a human need to sit and code that information 
    into HTML or is there some software that automates the process? (take the information from each 
    cell of the csv file and insert it into the appropriate spot of an HTML code generated based 
    on a few specifications). If so, what is that software (just a function in a commonly known 
    language - C, C++, Python, etc. - or something different altogether)? 

1. There is no way around it. If the structure of a webpage substantially changes, then 
   the script scapping information from the page may need to be adjusted. Sometimes it will
   require writing the whole script from scratch. 

2. Math Department website (as most websites in existence) was not manually written in raw HTML.
   It was created and it is maintained using the UB content management system (UBCMS) that 
   provides a graphical interface for editing webpages. One does not need to know any HTML 
   to use it, although it is useful for more complex tasks. 
   
   I think that the Math Department directory information was manually entered using UBCMS and it is 
   now manually updated as needed. This is doable (if not very efficient), since the directory pages 
   are fairly small and do not change frequently. Larger websites use frameworks that can pull data 
   from a database and create a webpage populated with the data on the fly, when someone tries to 
   access the page. There are a lot of tools that provide such functionality, including popular Python 
   web frameworks such as Django or Flask. Additionally, Beautiful Soup can be used to create and 
   modify HTML documents, so it can be used for simpler tasks, e.g. to covert a csv or Excel file
   into HTML. 

**Adrian asks:**

    Is it possible to use k-means algorithm on a data frame  ?

Yes, as long as the dataframe contains numerical data (since k-means works with this type of data).  


**David asks:**

    Is beautiful Soup used very often in the industry as opposed to stuff like Selenium for web scraping?

As far as web scrapping is concerned, Selenium is used usually with webpages where content 
is dynamically generated in the browser e.g. by executing JavaScript code. Such dynamic content 
cannot be retrieved by Beautiful Soup, since Beautiful Soup does not execute JavaScript. 
On the other hand, Beautiful Soup is much faster and requires much less resources than Selenium, 
so in the cases when it works, it is usually a better option.  


**Carter asks:**

    How does one create a plotting library? How important is the aesthetics of these images?

Building a plotting library completely from scratch is hard. Many libraries start with 
some existing library and add to it an interface that simplifies the process of creating plots 
in some way. Seaborn was built this way on top of matplotlib. Matplotlib also does not 
create plots out of nothing - it translates Python code into more primitive plotting instructions, 
and then passes these instructions to one of several backends that are responsible for
creating graphics. 

Aethetics are important - people are more likely to use a plotting library that creates
nice plots. Another important consideration is how easy is to use a given library.   


**John asks:**

    How many projects do we have left this semester?

We should have time for 4 or 5 more. 


**Jason asks:**

    Will we be learning about other machine learning methods in this course? 

Yes. 

**Mikhael asks:**

    Will we get to work on Neural Nets and CNNs in this class?

No, there is only so much that can fit in a single course. 

**Meaghan asks:**

    Is there any resources that you would suggest to get more hands on learning with 
    some newer tools that we have learned about such as requests and Beautiful Soup?

You will be able to practice using requests and Beautiful Soup for the next project. 
The best way to get experience with these tools is to use them - just pick a webpage 
and try to scrap some information from it. If you will not know how to do something 
(there are many intricacies of web scrappping that I did not mention in class), search 
the web and you will most likely find information that will help you. 


**Farhat asks:**

    Will we work with Beautiful Soup in an upcoming project? 

Yes. 

**Thinh asks:**

    In my opinion, plotly is more appealing than seaborn. Therefore, is there any advantages of using seaborn? 

Plotly interactivity is not useful if you are creating plots for inclusion in pdf files, 
printed documents etc. Also, the internal code used to create plotly plots saves all data that 
is shown in the plot. This means that if you are plotting a lot of data, plots will use a lot 
of memory and will create very large files when saved. There are ways to go around this problem, 
but they require more work. This is not an issue with seaborn since the size of seaborn plots 
does not depend on what is being plotted. 

**Scott asks:**

    Will we explore machine learning using data frames later in the course?

Yes.

**Anna asks:**

    Are we going to be making websites? Or doing that of some sort?

No, the focus of this course is data processing and analysis. I talked about
webpages because this is one of the sources of data. 



