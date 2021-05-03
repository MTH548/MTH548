Weekly Digest 13
================

**Amena asks:**

    will we work on sql after this week?

We will finish with a few SQL-related topics on Tuesday. The final, extra credit
project is on SQL.


**Makhtar asks:**

    I plan to get a certification in SQL, is there any version you recommend?
    The one I am about to take uses Oracle SQL.

Oracle databases are among the most popular SQL databases, together with MySQL,
PostgreSQL and Microsoft SQL Server. Unless you have some specific job in mind
which uses one of these databases, you can get certified on one of them and then
it should not be difficult to switch to a different system if needed. Personally,
I would start with PostgreSQL since it is an open source system and you can install
and use it for free.


**Guozheng asks:**

    Is it possible that SQL and Java script use together?

It is possible, but if you are writing a website or a web app then for security
reasons connections to an SQL database should be made on the server side, not
directly from the client. So, you can do it but probably you should not.


**Hannah asks:**

    The course website has a lot of very important information that I would
    like to be able to reference in the future; do you plan on keeping this up or
    should I save local copies of everything I might need?

The website will probably stay online until spring 2022 semester when this course will be offered
again. Source files are on `GitHub <https://github.com/MTH548/MTH548_site>`_.


**waleed asks:**

    What would be a reason to use something non-relational over a relational database?

Relational (i.e. SQL) databases have a rigid structure where data is organized into tables,
and each table consists of rows and columns. Non-relational (i.e. NoSQL) databases do
not impose such restrictions and store data e.g. as text files or JSON files.
Both types of databases have their advantages and disadvantages. SQL databases will in general
perform better with tabular data, but it is more difficult to use them for data which is not
easily organized into tables.


**Renjie asks:**

    Will we having a project on the Final week?

Yes, but it will be an extra credit project (i.e. you don't need to complete it).

**Sean asks:**

    Have you ever worked with NoSQL databases before? If so, how do they compare to SQL in the way
    they are utilized?

Yes, MongoDB. It feels more "Pythonic", closer to working with pandas or JSON files (which is fitting,
since MongoDB uses JSON files for storing data) than with SQL. Then, you can also work with SQL databases
in a somewhat similar manner, using for example the SQLAlchemy Python library. It provides an object
oriented interface to SQL databases.


**Miguel asks:**

    When will the sql project be assigned?

It is posted now.



**Temitope asks:**

    Are SQL statement case sensitive

No.

**Mohammedanas asks:**

    Is there any way we can estimate our grades based on the letter grades we have gotten
    on the past projects?

The procedure how to calculate the cumulative project grade is described in the
`course syllabus <https://www.mth548.org/#project-reports>`_.

**Makenzie asks:**

    If I wanted to continue learning about data analysis after this course ends, what course(s)
    or material would you recommend?

Computer Science Department offers several courses on machine learning, pattern recognition,
databases etc.


**Zhongyang asks:**

    Can we choose not to do SQL project ?

Yes.

**Jeffrey asks:**

    Is there a way to get a large text between two words with Complex regex?

I am not sure if I understand the question, but if you are asking whether it is possible
to match text enclosed between two specified words, then yes, you can do it with regex.


**Max asks:**

    How was it teaching this section? Was this your first time teaching the class or did
    you and the other professor who taught this class in the past switch on and off


I have not not taught MTH 448 before. It is an interesting class to teach, although
it requires quite a bit of work to prepare projects, grade them etc. It has been
a good experience.

**Matthew asks:**

    For someone who is interested in data analytics and really enjoyed the material
    and projects in this course, what would you recommend as a good next step to keep
    learning more?

The Computer Science Department offers several machine learning courses that you may
find interesting. Alternatively, there are a lot of great resources freely available
online. For example, `here <http://neuralnetworksanddeeplearning.com/chap1.html>`_ is
a very good introduction to neural networks and how to code one from scratch in Python.
While there are tools for building and training neural networks in just a few lines of code,
this approach gives a real appreciation and understanding how various elements of neural
networks work. This is not an easy reading, but definitely worth it.

Finally, the best way to learn something is by doing, so you can take some dataset
(you can find a lot of them e.g. on `Kaggle <https://www.kaggle.com/>`_) and do something
with it. You can also use Kaggle to see how other people analyze data.


**Sai asks:**

    Is there any SQL concept video link available, can you share any links about SQL .

If you are asking about the videos from this course, then they are posted on the course
website (SQL is in week 13 and will continue in week 14). If you are interested in other
video courses on SQL then there are plenty of them online, for example you can search YouTube for
`SQL <https://www.youtube.com/results?search_query=sql>`_. By the way, these videos promise
to explain SQL in anywhere between 4 hours to 100 seconds. I would be cautious with the
ones on the lower end of this scale.



**Alexander asks:**

    Thank you for being a great professor!

Thank you, but this is not a question.


**Darren asks:**

    Why would one choose SQL over pandas or vice versa?

SQL databases are systems for data storage and retrieval. They can work with
huge amounts of data, they can let multiple users access the data at the same time,
they can be used to restrict which data a given user can access or modify etc.
Such tasks cannot be performed with pandas since pandas does not deal with data storage
or access at all. However, pandas is a very useful tool for manipulating tabular data.
Moreover, since pandas is a Python library, it can be easily combined with other
Python tools e.g. for data visualization, machine learning etc. As I will explain on
Tuesday, pandas and SQL can be used together, so one does not need to choose one over
the other.


**Elita asks:**

    Why use SQL over Pandas or vice versa?

See the answer to Darren's question above.


**Souleymane asks:**

    What are some interesting project ideas that we could implement using
    the skills learned in this course?

You can have a look at `Kaggle competions <https://www.kaggle.com/competitions>`_ for some
ideas.

**Jonathan asks:**

    We've been working with SQLite which is just one of the many different kinds of SQL database
    management systems. Is there a large difference between some other popular variants in terms
    of how they interact with SQL? And which of the database systems would you recommend for us to
    become more familiar with for their wide use in the field?

For writing fairly simple queries there is not much difference. More advanced usage
will expose more differences. For example, various database systems extend standard
SQL in some ways, providing additional functionality.

PosgreSQL may be a good system to experiment with. It one of the most popular SQL database
systems, but it is open source so everyone can install and use it for free. It is also worth
to get familiar with a NoSQL databases (e.g. MongoDB).
