Weekly Digest 3
===============

**Houlin asks:**

    Will our future projects have similar degree of difficulty to project 1?

Yes, more or less.

**Sindy asks:**

    Why is python so hard?  Every time I googled for a question, they gave me
    a command that doesn't work in Anaconda. So I have to keep searching until
    I find a usable one. Does Anaconda/Jupiter notebook not have all the commands
    that's usually supported in python?

Getting started with programming may be hard, but Python is considered to be one of
the most user-friendly programming languages. If you ever try programming in PHP
you will understand...

You can run almost any Python code in Jupyter notebook. There are exceptions
but we will not get anywhere close to them in this course.

**amena asks:**

    If our code doesn't run properly do we fail the assignment completely?

Coding errors are a serious flaw of a report. How serious depends on the code.
If in the first report the k-NN implementation does not work correctly, it is
a major problem since the whole project depends on it and you may fail the assignment.
It there is an issue with some fairly insignificant function, it will have lesser
impact. In any case though, test your code so it is correct.

**Mohammedanas asks:**

    Are the weekly exercises always/usually related to the upcoming projects?

Yes, this is the plan.


**Sean asks:**

    Is there such this as overfitting for a supervised learning problem? For instance,
    can we feed enough data to knn to make it less accurate on new data?

In general overfitting is a problem. It happens when predictions made by a machine
learning model become too dependent on the choice of data samples used as training data.
That is, with overfitting replacing one training set of data by another may significantly
change prediction results.

In the case of k-NN choosing too few neighbors (e.g. only one) may lead to overfitting,
since then a choice of a single training sample may skew the outcome.



**Makenzie asks:**

    Suppose we have some set of unlabeled data and we apply k-means to it. If we obtain new
    data afterward, is it better to rerun k-means or could we simply apply k-nn?

This will depend on what you are trying to accomplish. If your goal is clustering, then
it would be sensible to rerun k-means on the data set including new data, but to take
centroids computed with the original data as the starting point. K-means should converge
faster in this way. If you want to use k-means for classification, then you can cluster
the original data, and then assign new data points to clusters depending on which centroid
is the closest.


**waleed asks:**

    Are we allowed to post our projects on GitHub?

Yes, but please do not say that they come from this course. I may want to reuse some projects
in the next iteration of the course and I would prefer if students cannot find report from
this semester by searching the web for MTH 448 or MTH 548.


**Mohammedanas asks:**

    Are project solutions too be posted after deadline. How long can it take to get our grades back?

I will not post solutions primarily because there is no one correct way to write a report.
In each project there is a degree of freedom as to how you can explore it. I hope that I can
grade the reports in about a week. They will be returned by email.

**Darren asks:**

    What is the difference between k-Means and k-NN? I know that k-Means is for unsupervised and k-NN
    is supervised but is it possible to do a task that uses k-NN with k-Means instead and vice versa?

It is possible to combine these algorithms for some purposes. The next project will explore
one such possible application.


**Miguel asks:**

    Would it be possible for you to explain potential input parameters for functions that you import?
    You could press shift-tab-tab to bring up its documentation.

I may try to do it from time to time, but functions frequently have too many parameters to explain
in a reasonable time. Most of the time I will explain how a function works in some basic configuration,
and leave it to you to check the documentation for additional options.

**Hannah asks:**

    The syllabus stated that the project was due 10am on Friday, but both UBLearns and the current
    tasks said midnight. I submitted it before midnight but after 10am, and I would like to make sure
    it will be accepted. For future projects, what time will they be due? Also, how much class time can
    we expect for the projects?

I moved the submission deadline to give you more time for the report, and talked about it in class
on Tuesday. I plan to keep the Friday midnight deadline in the future. I am not sure if I understand
the second question. For each project I plan to schedule some class time so you can work on the project
on Discord while I am available to help you.



**Justin asks:**

    When will we receive grades back?

I should be done with grading by the next weekend.

**Renjie asks:**

    There's two questions, first is I got this when I execute my code

    ``<ipython-input-4-ea4bd0a4fc3f>:13: RuntimeWarning: overflow encountered in long_scalars``
    ``<ipython-input-4-ea4bd0a4fc3f>:15: RuntimeWarning: invalid value encountered in power``
    Is it because the number that I'm calculating are too large? If it is, how to fix it?

    Second is, when you grading the project, are you gonna give a specific comment on  what
    we are doing wrong or why the points are deducted?

The first message means that some number was too large for a numpy array. The message error
can show up e.g. if you try to take a fractional power of a numpy array with negative
entries, for example ``np.array([1, -2, 3])**(1/3)``.

I will include comments in the report on what was good with them and what were the issues.

**Temitope asks:**

    Looking at the way the class is going, at the end of the semester, we should be able to work
    as Data Analyst, right? If so, are we going to work through any raw unclean data so as to go
    through the preprocessing, and feature engineering to making the data fit for analysis with us.
    Thank you.

One course is not enough to be qualified as a data analyst. The goal of this course is to
get you acquainted with some tools and methods that data analysts use, enough so that you
should be able to solve many problems on your own. After this semester you should also
have background to go deeper into data analysis if you choose.

Cleaning data is a tedious and time consuming process. We will be mostly working with clean
data, but we may encounter some raw data from time to time.


**Jeffrey asks:**

    Are there any weakness to using the k-means algorithm? Is it better to use k-NN over k-means?

k-NN is a supervised learning algorithm: you need to have labeled training data in order to use it.
k-means is useful when we have only unlabeled data.

**Makhtar asks:**

    So far it looks like this class prepares us to do data analytics. Is the content also as relevant
    for data engineering ?

If you mean tasks such as data extraction, normalization, cleaning etc. then such topics may appear
occasionally, but it is not the main focus of this course.

**Sai asks:**

    Can u explain how to write math equations in our project report? As some format is mentioned in the guide.

LaTeX is a typesetting system commonly used to produce technical texts. Jupyter notebook can render
formulas typeset in LaTeX. The formulas need to be enclosed in either $single$ or $$double dollar signs$$.
For example ``$\int_0^1 x dx = \frac{1}{2}x^2 + C$`` will be rendered as :math:`\int_0^1 x dx = \frac{1}{2}x^2 + C`.
`Here <https://www.math.ubc.ca/~pwalls/math-python/jupyter/latex/>`_ is a brief introduction to
LaTeX in Jupyter notebook.


**Matthew asks:**

    Is there a rule of thumb for the amount of training and testing data to use on ML algorithms?
    Is more training always better (as long as it doesn't take an unreasonable amount of time to compute?

More training data is better and after evaluating performance of a model (which involves putting aside
some data for testing) usually the model is trained using all available data before it is put into real
work. In the testing process we would like to keep as much data as possible for training (to get more
realistic performance) and run as many tests as possible (since more testing gives more accurate view of
how the model behaves).  This may seem as a contradiction since more training data means less testing data
and vice versa), but `there are ways around it <https://machinelearningmastery.com/k-fold-cross-validation/>`_.


**Alex asks:**

    How soon should we expect grades for our projects?

I should be done with grading by the next weekend.

**zhongyang asks:**

    What numpy version should we use? I noticed that some command can not work on low version of numpy.

The newest is 1.20.0, I have 1.19.2 installed. If you have an older version (say, below 1.15) it may
be worth to upgrade.

**Max asks:**

    Will we be studying more machine learning algorithms or is this more if a data wrangling class?

Yes, there will be more machine learning (and data wrangling too).



**Elita asks:**

    Will there be any projects where we do not have to write a report and it is graded solely on code?

Yes, there may be one or two purely coding projects.



**Jonathan asks:**

    Would it be possible to get a more well-defined criteria for grading the projects?
    Although I was confident in it, I just wasn't completely sure if my analysis portion
    of the k-NN project was sufficient to get full credit on the assignment.

I will talk about it in class before the next project will be due.
