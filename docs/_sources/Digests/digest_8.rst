Weekly Digest 8
===============

**linggan asks:**

    Why is beautiful soup called beautiful soup?


It refers to the "soup" of HTML or XML tags that it processes. 
It is also a reference to a song in the book "Alice's Adventures in Wonderland" 
by Lewis Carroll.


**Saiful asks:**

    Can you please suggest some resources to learn web scrapping? 

It you search the web for "web scrappping with Python" you will get see a lot of 
results. I have had a look at some, and they looked useful. There is even a book 
"Web Scraping with Python" published by O'Reilly. The best way to learn web scrapping 
is to practice with some webpages. 


**Metin asks:**

    I have very little understanding of how the world wide web works (despite nearly using it 
    to breathe at this point) so please excuse the questions below. 

    1. Could you give us some additional examples of websites (besides Wikipedia) that would deny 
    a request coming from Python's requests if the user agent is not identified? 

    2. Are there any websites that only accept requests from a predetermined set of user agents 
    (that is, for which there is a list of approved possible user agents and the request gets 
    denied if it does not use an agent from that list)? 


This should anwer both questions. Amazon.com routinely blocks requests it recognizes as coming 
from scripts. In particular, it will block a request if the user-agent is not one that is associated 
with some commonly used web browser. To circumvent it, people scapping amazon pages set 
their user-agent to the user-agent of some browser, effectively pretending that their script is 
a web browser. There are many web pages that list user-agents of various web browsers, here is
[an example](https://developers.whatismybrowser.com/useragents/explore/). 

Faking a user-agent for scrapping amazon may work in a short term, but after a few requests 
the script can still get blocked if amazon servers notice that too many requests are coming from 
the same IP address. Then there are ways around it, e.g. by using proxy servers. 


**Scott asks:**

    I was wondering if there is a way to save variables in python or jupyter like you can in MATLAB. 

In Jupyter notebook you can use [%save](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-save)
magic. For more general applications, saving variables and their value to e.g. to a json file 
is a good option. 


**Griffin asks:**

    Will we be using web scrapping with a more data analytical approach in a future project?

We be will using the marathon data (that you were scrapping for project 4) for some analysis. 


**Mikhael asks:**

    Can you explain User-header again in class just as review?

You can have a look [here](https://www.mth548.org/Tools/requests/requests.html#User-Agent). 
You can also search the web for "user-agent web scrapping". There are many pages that 
explain what user-agent is and how to use it. 


**Ninghui asks:**

    Every website can be turn to API form or just specific website has API. Does json have 
    any limitation?

Some websites/web services have API, some don't. As for JSON, it depends what you mean by
a limitation. For example, JSON stores data as text, which may require more space than some 
other data storage formats. On the other hand, text can be read by humans, text files are easy 
to transfer between computers etc. Thus what from one point of view is a limitation, from
a different perspective is a useful feature. 


**Steven asks:**

    Will there be web scrapping in the future projects?

No, we will move on to different topics.


**Luca asks:**

    What is the best format to handle a huge data set?

It depends on the kind of data. For some data types, a database of some kind may be a good solution. 
For truly large sets of data, the problem will be not just the data format but the hardware needed to 
store and handle the data. In such cases, you may consider using one of the commercial data warehouses
such as Google BigQuery, Amazon RedShift, Microsoft Azure Data Lake etc. These services use specialized 
servers, specifically designed to store and process very large amounts of data. 


**felix asks:**

    How are real enterprise-scale web crawlers (like pagerank etc) implemented?  
    Presumably they don't use python.

PageRank is an algorithm for ranking webpages, not a web crawler. Google, Microsoft etc.
use proprietary software for crawling the web, I am not sure how much of their source 
code they make public. It is possible to write a fully-featured web crawler using Python, 
see e.g. [Scrapy](https://scrapy.org/). 


**Haiyi asks:**

    For me, I find it difficult to use the information of the web page to draw pictures, and many times 
    I don't know how to determine where the information I want is on the web page.

I am not sure what is the question here.


**David asks:**

    Will we learn about other web scraping libraries?

No, we will be moving on to different topics.  


**Cassandra asks:**

    Is there a faster way to scrap data from a website than what we did 
    in class or is that the most efficient way to get data? 

In general, scrapping a webpage will will follow a similar process 
to the one we went over in class.  


**John asks:**

    Are we going to have a final project that combines a little bit 
    of everything we learned this semester?

No, a project using all tools covered in this course would be just too long. 


**Dakota asks:**

    How many projects do we have left in semester?

We should have time for 3-4 more. 

**Netra asks:**

    Are we going to create our own webpage for a project?

No, this is not related to the main subject of this course which is data analysis. 

**Bochun asks:**

    I'm confused about the project distribution. This project is a short project that 
    only need code. So I'm kind of confused about the report organization and code documentation. 
    What kind of comment of the code is necessary? I found it difficult to describe what does 
    each lines do, because if someone complete know nothing about coding, my comments won't help him
    understand the codes. And someone who do know about coding, especially python, will not need 
    that amount of comment.

There should be enough code documentation to be useful to someone who knows Python. 
This does not have to be much, but brief explanation what various pieced of code are 
doing are helpful. In general, tt is a good practice to document code even if you 
are the only person that will use it. 

**Farhat asks:**

    Could beautifulsoup work with a PDF file? 

No, PDF format is entirely different than HTML/XML, and much less pleasant to work with.
There are other Python libraries though for processing PDF files. 

**Jason asks:**

    Will we have a project where we utilize XML/Json files? 

 Working with XML files is similar to working with HTML files which was 
 the subject of project 4. You will be working with JSON for the next project.

**Michael asks:**

    Is there a way for website to prevent outside users from scrapping data?

There is no way to prevent scrapping entirely, but there are ways to make it more difficult. 
This is for example what all the websites using [captchas](http://www.captcha.net/) are doing.  


**Adrian asks:**

     Will we learn how to automate certain tasks throughout the semester ? 

This is essentially what we are doing most of the time in this course. Instead of manually 
editing Excel worksheets you can use pandas, instead of copying and pasting data from the web 
pages you can scrap them using request and BeautifulSoup etc.  


**Meaghan asks:**

    Should we expect to be working with a lot of excel/csv files in the next coming projects?

There will be csv files used, but not a lot of them. 
 

**Thinh asks:**

    Is there any competitive library which support the scrapping such as BeautifulSoup? 
    Also, is there any security issue when scrapping a certain website?

As for BeautifulSoup compatitors, there are several e.g. Scrapy or lxml. 
I don't think that basic web scrapping brings any special security issues. 

