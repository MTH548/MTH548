Weekly Digest 8
===============

**Makenzie asks:**

    Does BeautifulSoup provide any true functional benefits or is it purely cosmetic?
    I guess what I'm really asking is does the time it take to process data through
    the BeautifulSoup get made up elsewhere in programs?

BeautifulSoup parses HTML or XML documents and provides tools for navigating
the parsed document structure. These are functional benefits. You could write
your own parser, but it would certainly take incomparably more time than running
a document though Beautiful soup. And then you would need to run the document through
the parser anyway.

**Guozheng asks:**

    why for the clear_output, if I don't put wait=True, the picture is very lag?

In the `clear_output()` function `wait=True` assures that the display is cleared only
when there is new content ready to replace it. If your computer takes longer time to
produce the new content then it will create lag.

**Houlin asks:**

    Can we use HTML or XML to change some contents in a website as a visitor ( when we
    request it from my local server)

If you change the source file on the server then a visitor will see the modified file.

**Amena asks:**

    Will there be an extra credit assignment or like an optional project that we can do to bring
    our grades up a little for those who struggle with the code?

You can get extra credit on each assignment if your report will go beyond expectations
in some respect. There will be no separate extra credit assignments.

**Zhongyang asks:**

    We can use api to get data from website. Can we use api to do more things to website?
    Like change some material on website.

Yes, if the API provides such functionality. For example, Twitter API lets one post
new tweets, Wikipedia API allows one edit Wikipedia pages etc.

**Alex asks:**

    Is there a way to check our mid semester grades so far?

80% of the final grade is based on project reports, so you can take the average of report grades.
The grade may be somewhat lower or higher depending on the other 20% which are based on
attendance and weekly digest submissions. If you assume that you are getting an "A" on the 20%
and combine it with your report grade average for the remaining 80%, it will give you the upper
estimate of the grade you can get at this point.

**Makhtar asks:**

    How late are we allowed to be late in lecture to be mark present?

I would rather not specify this. I will be reasonable, but you should be on time.

**Sean asks:**

    Are there any functions in the pandas library that work directly with json data?

There are a few such functions. ``pandas.read_json()`` converts a JSON string to a
DataFrame (provided that JSON is in one of the forms that pandas can understand), and
``pandas.DataFrame.to_json()`` converts a dataframe to a JSON string. There is also
``pandas.json_normalize()`` which attempts to flatten nested structures in a JSON string
and produce a dataframe in this way.

**Renjie asks:**

    Is it ok if we scrap from any website as long as there's no tool stopped us?
    Will it  be considered as an attack if we scrapping or requesting too fast from  a website.
    (like if we don't put the sleep commend in the loop, it is a way to attack a website right?
    By constantly scrapping or requesting something really fast.) If it is, what's the minimum
    spacing time  between two operation(because sometimes when we are on the website, we click
    fast as well).

You `US courts ruled <https://parsers.me/us-court-fully-legalized-website-scraping-and-technically-prohibited-it/>`_
that one can legally scrap any website. At the same time website owners can use tools
(capchas, cookies, fingerprinting etc.) to make scrapping more difficult. Even sites that
are scrapping-friendly may block your ip address if you create problems - e.g. by sending
requests too fast, ignoring robots.txt rules, not providing a meaningful User-Agent etc.
The reasonable rate of requests you make will depend on a website. Heavily used websites will
be able to handle thousands of requests per second without issues, but for a website hosted
on a small web server this number will be much smaller. One request per second should be good
in all circumstances. It is true that you can send more requests manually if you click fast on
a link in a web browser, but a Python script with asynchronous code will be able to send more
than a thousand of requests per second  - much more that you would be able to produce by clicking,
and enough to put a strain on many web servers.


**Miguel asks:**

    How many more projects do we have left? Also how many more libraries are we going to be working
    with?

We should have time for 3-4 projects. We will go back to some machine learning next, so
the focus will shift from introducing new libraries to other content.

**Souleymane asks:**

    How many more large projects do we have left?

We should have time for 3-4 projects.


**Sai asks:**

    Is there any regrading opp. for the assignments graded ?

No.


**Max asks:**

    Will we be learning how to use nosql databases?

No, there will not be time for it.


**Peter asks:**

    Is it possible to explore web pages through our code by giving inputs in textboxes?
    Example: to get the 50 top male marathon runners I used the webpage to first find
    this info and used that URL. Is there another way to get to this information without
    putting the exact URL into the program we write?

Yes, if a webpage contains a form it is possible to supply its values and submit the form
from a Python script. Here how could be done with the form posted on the Chicago marathon
results website:

.. code-block:: python

  import requests

    url = "https://results.chicagomarathon.com/well-known/2019/?pid=list"

    params = {"lang": "EN_CAP",
              "startpage": "start_responsive",
              "startpage_type": "lists",
              "event": "MAR",   # event = marathon
              "search[sex]": "M",   # male runners
              "search[age_class]": "%",   # all age groups
              "num_results": 50   # 50 runners per page
             }

    r = requests.post(url, params=params)

Submitting forms typically requires sending a POST request (as opposed to GET),
but the Chicago marathon website seems to work with both kinds. The parameters
that need to be send can be determined looking at the HTML code of the form.


**Matthew asks:**

    I know we've been using Jupyter notebook for this course, but do you have
    a recommended text editor for more general purposes?

I like `Visual Studio Code <https://code.visualstudio.com/>`_, but there are many
other good options.


**Darren asks:**

    Was wondering what the class average grade of the previous project is

The average on project 3 was a B (numerically 2.98/4.0).


**Waleed asks:**

    Whats the minimum amount of time we have to use the sleep function when
    web scraping without getting our IP restricted?

This will depend on a website. About 1 request per second should be good
in most cases, some websites may tolerate higher rate.


**Jeffrey asks:**

    Will we be able to create our own website after learning html and json?

To create a website from scratch you need to know HTML and CSS. JSON is not
needed for this. You can also use JavaScript for added functionality. However,
there are many tools for creating websites in a more user-friendly fashion.
For example, the website of this course uses Sphinx software. The source of
all pages of this website are Jupyter notebook files and some rst files. Sphinx
converts all these files into webpages adding the sidebar etc.

**Hannah asks:**

    How is our attendance being graded? Does having our camera on in class count
    for anything?

I explained in class at some point that having camera on or off will not impact
your grade, it is a matter of courtesy and kindness. Attendance is graded and
as it is stated in the syllabus it counts for 10% of the final grade.

**Elita asks:**

    Is there a debugger in jupyter notebook?

You can try the ``%debug`` magic, see `here <https://chrieke.medium.com/jupyter-tips-and-tricks-994fdddb2057>`_
for more information. `IPython debugger <https://ipython.readthedocs.io/en/stable/api/generated/IPython.core.debugger.html#>`_
is another option.


**Seungmin asks:**

    Will there be any other projects similar to project 4 where most of it is
    coding rather than a report.

Yes, project 5.

**Mohammedanas asks:**

    Will we have more projects like the 4th project?

Yes, project 5.

**Jonathan asks:**

    When we move on to learn about SQL (or perhaps after that), will we be introduced
    to frameworks like Flask as well?

No, the focus of this course are tools and methods used to process and analyze data.
Flask is fairly easy to learn on your own though.


