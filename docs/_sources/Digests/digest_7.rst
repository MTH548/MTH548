Weekly Digest 7
===============

**Makenzie asks:**

    Does every webscraper have to be tailored to the specific site being scraped and its format?
    I guess what I'm really asking is how much time am I going to need to spend parsing HTML?

Every website is structured differently, and scrapping needs to be customized to reflect
this structure. Unless, that is, you are looking for some some generic information. For example,
if you just want to get all text from the page and not particular pieces of text then the
same script will work with most pages.

How much time it will take to scrap a website will depend on how complex and large the website is.
Some websites use a lot of JavaScript and this requires additional tools for scrapping (such
as Selenium) and typically takes more work.


**Sean asks:**

    Will we learn about or use an api in a project for web data collection/processing? (i.e., Twitter
    API, YouTube API)

We will deal with it this week.


**Kevin asks:**

    Are there other IDE's like jupyter that don't use the browser and is lightweight that you would
    recommend?

I like `Visual Studio Code <https://code.visualstudio.com/>`_ and `PyCharm <https://www.jetbrains.com/pycharm/>`_.
VS Code is free. PyCharm Professional costs quite a bit, but students can get free education licenses.
VS Code is lighweight, PyCharm is more resource-heavy.


**Zhongyang asks:**

    If I feel curious about some part in this course, like machine learning, is there any recommended resources
    I can read more?

UB course CSE 474 gives a good introduction to machine learning. `Its website <https://mlcourse-ub.readthedocs.io/en/latest/>`_
has links to lecture notes and videos.


**Makhtar asks:**

    For project submission, can you allow multiple submissions? I read my project 3 and fixed some lines,
    but I was not able to submit again.

I usually remember to allow it, I forgot to set it this way for report 3. Let me know of such issues by email or
Discord, so I can fix them.


**Renjie asks:**

    When we type the html code in the notebook, it's just python simulating the html right? We can't really
    create like a website there right?

Jupyter notebook has a small web server running in the background which sends  HTML code to the web
browser, and then the browser renders it. Jupyter notebook is not a tool for creating websites. However,
Python does offer tools for web development. You can have a look at Flask or Django for example.


**Sai asks:**

    In the project So for national data that we have used, we don't have segregation based on state. But
    in the example, they are saying that they need some statistics statewise. For that single example,
    can we skip calculating that statistics or we have to consider state data for that one use case.
    so what I did is hair left the state part aside and flowed the national information. Is that correct?

I am not sure if I understand correctly what you wrote. The baby names project was open-ended.
You were asked to explore the data in some interesting way. If you developed the report
sufficiently, and if your computations and analysis are correct it is fine.


**Jeffrey asks:**

    Is there a way for other to look at my HTML page without share my file/code?

No. In order for someone to see your webpage, a web server needs to send HTML/CSS/JavaScript code
to that person's web browser. This is how web browsing works and there is no way around it.


**Alex asks:**

    Where/when is web scrapping usually used in an analyst type job?

Sometimes analysts need data which is available only on some websites and needs
to be scrapped first. Data can come also in other formats (more about it later in
this course), but in general bringing it to a usable form is a big part of data analysis.
People working in this field often say that 80% of their time is spent cleaning and
formatting data.


**Hannah asks:**

    Broadly, what topics are we going to cover through the rest of the semester?

Some data formats (JSON, XML), some machine learning (Bayes classification, regression),
some SQL. Perhaps something else if time permits.


**Matthew asks:**

    Is the marathon web scrapping project due this Friday (3/26)? The current tasks page lists both
    project 3 and 4 as the baby name project.

My mistake, it is fixed now. Project 4 is web scrapping and it is due on 3/26.


**Darren asks:**

    Are we allowed multiple submissions for the projects?

Sure, I am grading the last attempt. If multiple submissions of a report are not enabled on UBLearns
it is because of my omission - let me know and I will change it.


**Souleymane asks:**

    Will there be a large project that encompasses everything that we learned coming in the near future?

Some projects will use several tools, probably not all of them at once though.

**Peter asks:**

    We went over the /robots.txt for some sites - but are there ways sites can restrict your access to scrapping
    or is it always just a request?

The file robots.txt only indicates what is requested but does not enforce it. Some websites employ other
techniques to prevent scrapping - captchas, cookies etc. For example, if you use requests to connect to
the Amazon website (https://www.amazon.com) you will probably get a message, that if you want to scrap
this website you need to email Amazon support (which probably will write back that you cannot scrap the
website). Then, there are also ways around these restrictions.


**Miguel asks:**

    Is there a way to find the parents of elements that you select?

With BeautifulSoup the ``.parent`` attribute of an element gets the immediate parent, and
``.parents`` gives an iterator of all ancestors.


**Temitope asks:**

    Why is requests and beautifulSoup preferred over other web scraping tool. What are the limitations
    of both requests and beautifulSoup

Requests and BeautifulSoup are frequently used due to their functionality and convenient
interface. There are other tools providing similar features and which one to use is to some
extent a matter of preference. As for limitations, I remember that at one point I had
issues editing an XML file using Beautiful Soup and I had to switch to a different library.
Although it might have been a problem with an XML parser and not the Beautiful Soup itself.
I have never had any issues with requests.


**Seungmin asks:**

    Will there be any other projects that will be similar in terms of being given options for what we can
    branch off to?

Possibly.


**Mohammedanas asks:**

    I found the topic of web development really interesting. Are there any classes that go further
    into this area??

Yes, CSE 312 for example.


**Elita asks:**

    Just wondering if there is a reason why the names of the libraries are like Beautiful Soup and Pandas.

Pandas supposedly stands for "Python data analysis". Beautiful Soup is a reference to a song
from the book "Alice's Adventures in Wonderland" by Lewis Carroll.


**Jonathan asks:**

    Will there be any opportunities to make-up for missed work in this course?

No, sorry.
