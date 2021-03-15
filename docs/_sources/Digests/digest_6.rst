Weekly Digest 6
===============

**Temitope asks:**

    What do we do when our code in Jupyter Notebook is taking forever to run.

It depends. Sometimes it is due to incorrect or inefficient code, sometimes to
the actual number of computations involved. For projects in this course it is
unlikely that you would need code that takes more than a few minutes to run.
Unless you try to do something that I have not planned for.


**Hannah asks:**

    You mention in the syllabus that extra credit can be awarded for the projects
    if extra work is put in. How many extra points would this be, and what would
    be an example of an analysis earning extra credit in the previous projects?

Extra credit means the next higher letter grade (including an A+ if the grade is
already an A). There will be a checkmark in the "Bonus" cell of the report
score table if you get it. I have not awarded it yet but it does not mean that it
is impossible to get - I will be happy to give extra credit for work which goes
somewhat beyond regular expectations.

**Sindy asks:**

    1. Why do we always import python as np(similarly, panda as pd) instead
    of "from python import*"?

    2.How do you make a specific name show for the years of even numbers?

1. Using the syntax ``from some_module import *`` is in general a bad practice.
Names imported in this way may clash with names already existing in the code, or
with names imported from other modules. For example, both modules ``numpy`` and ``math``
include the ``sin()`` function. If you use ``from numpy import *`` and
``from math import *`` you may end up using a function  coming from a different
module than you intended. Since the function from ``numpy`` works with numpy
arrays, and the one from ``math`` does not, this makes a difference.

2. I am not sure what you mean.


**Sean asks:**

    What is the biggest mistake you see in project reports?

Not the biggest but most common are reports which consist mostly of code with
hardly any narrative, analysis etc. In a report code should be a tool for analyzing
data and the narrative should guide the user through the analysis and its results.
Good data analysts are people who can tell story with data, not just write code.


**Waleed asks:**

    Will we be doing more machine learning in this course?

Yes.

**Jeffrey asks:**

    Is it possible to create subplots with the px.choropleth?

Yes, you can use ``facet_row`` and ``facet_col`` arguments to create subplots as
in other Plotly Express plots. See the  `documentation <https://plotly.github.io/plotly.py-docs/generated/plotly.express.choropleth.html>`_
for details.


**Alex asks:**

    Would you be able to put up notebooks after each lecture? I feel like sometimes
    I can't keep up during lecture and it would help me stay on track throughout
    the week

I can do it.


**Guozheng asks:**

    Why we keep using reset, Can we just make a new name instead using reset?

I am not sure what you mean. Feel free to talk to me so we can clarify this.


**Mohammedanas asks:**

    Will we be given chances to improve our grade with extra credit sometime
    in the semester??

You can get extra credit on each project for work which exceeds expectations.
There will be no separate extra credit assignments.


**Miguel asks:**

    I don't have a question this week

You should come up with something, this is a part of the assignment.

**Max asks:**

    What will our next project look like? Will it be data analysis or will it relate
    to machine learning?

The next topic is how to retrieve data from web pages and the next project
will be related to this.

**Renjie asks:**

    For the topics, how many topics are you expecting, at least.

Do you mean projects? If so, we should have time for 7-8.

**Matthew asks:**

    Are there any courses at UB that you'd recommend for somebody interested
    in data visualization?

I don't know any, which it does not know that they do not exists, check the
UB course catalog. There are a lot of good resources on data visualization though.
Books by Edward Tufte are considered classics in this area.

**Sai asks:**

    Not concepts but my report 2 i got a remark that my implementation was wrong.
    But I really understand I did something wrong but I really don’t know what
    mistakes cost me that remark. I would like to talk to you regarding that.

In the body of your report I included a comment explaining what was incorrect.
Of course I am available to talk about it in person - ask me after class or
during my office hours.

**Darren asks:**

    In this line of code, ``fig.update_yaxes(matches=None)``, I am wondering what
    (matches= None) does. Is the purpose of that separating the information into
    multiple graphs?

By default, if you create several subplots with Plotly Express, all of them will have
the same values on the y-axis. This is not always desirable. For example, in class
I was plotting the number of male and female babies named "John" each year.
In this case values on the y-axis in the subplot for males need to go to tens
of thousands, but for girls they should go only to hundreds since there are few girls
named John. The code ``fig.update_yaxes(matches=None)`` indicates that each subplot
can have different y-axis values.


**Houlin asks:**

    Can we export the modified table in our jupyter notebook as a new Excel file?

Pandas dataframe can be saved as an Excel file using ``to_excel()`` method.
See `Pandas documentation <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_excel.html>`_
for details.

**Peter asks:**

    Are there any dropped projects or leniency at the end of the course if we
    miss or just do poorly on one?

I will not drop any projects, but if someone does poorly on one project and much better
on the remaining ones then I will take it under account while assigning final grades.


**Justin asks:**

    Midterm grades be given?

I don't plan to give midterm grades, but you can estimate them yourself. Just take the average
of grades from your reports. The actual grade will also take into account your Zoom/Discord
participation and whether you were submitting weekly digests, so it may be somewhat higher or lower.


**Seungmin asks:**

    Is it possible to discuss about what situations the topics we've learned could be applied in the future?
    Personally I'm still not sure of which direction I could go career-wise and I would like more information
    to possibly narrow down on what I could pursue in the future.

The topics are discussing in this course are very practical, since data processing and analysis are
very common tasks. If there is something specific you are interested in, it may be best if we talk about it
in person. You are welcome to stay after class or come to my office hours.


**Yuxun asks:**

    What is the main advantage and/or disadvantage of using plotly over seaborn?
    Can we run statistical analysis using plotly?

Plotly is interactive, seaborn creates static images. For a large amount of plotted
data, files with Plotly plots will in general be also large. Files with seaborn plots
do not depends in a significant way on how much data is plotted.

Plotly  and seaborn provide similar tools for visualizing statistical information
(trend lines, kde etc.).

**Jonathan asks:**

    Will we eventually be trying to combine the basics of machine learning that
    we discussed earlier in the semester with later topics like using SQL and
    advanced plotting? Or will things be more like learning a set of tools
    individually?

Some future projects will combine several tools - machine learning, pandas, plotting
etc. Some will be focused on specific tools. 




