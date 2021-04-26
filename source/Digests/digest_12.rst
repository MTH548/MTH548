Weekly Digest 12
================

**Guozheng asks:**

    In this code, ``words = re.findall(r"[a-z']+", text)``   It keep showing error said
    the text is not define. I have no idea what is going on.

You need to define a variable ``text`` with a string first. If this does not help, you
can show me your notebook after class and I will see what is wrong.



**Amena asks:**

    how can we calculate our grades so far?

80% of your final grade is based on the project report grades. The way to compute
the overall project report grade is described on the course website:

1. Convert the letter grade for each report into credits (A = 4.0, A- = 3.67 etc.);
2. Multiply credits for each report by the report weight and add all these products;
3. Divide the resulting number by the sum of weights for all reports.

10% of the grade is based on completion of weekly digests. If you miss at most
one digest you will get an A for this part (i.e. 4.0 credits). For each subsequent
missed weekly digest the grade will go down by 20% (e.g. to 3.2 credits for
the seconds missed digest and so on).

The final 10% is based on the class attendance, and the procedure for computing this
part is the same as in the case of weekly digests.


**Sean asks:**

    Do you know what the SQL project is going to look like? I have only used SQL
    in the context of website development.

I am still working on it.


**Makenzie asks:**

    Are there other places where people use Laplace smoothing or does this refer exclusively
    to what we did with adding 1 to all the counts in a data set?

Laplace smoothing is often used with naive Bayes classifiers - not necessarily
related to text classification.


**Waleed asks:**

    Is the text classification due this Friday or next Friday?

Friday, May 7.


**Miguel asks:**

    Are we not allowed to use the Naive Bayes Classifier from sklearn for
    the upcoming project?

No. You can use ``pandas``, ``re``, ``numpy``, standard Python libraries
(e.g. ``collections`` which provides ``Counter``), plotting libraries
(``matplotlib``, ``seaborn`` etc), but not machine learning libraries which have
naive Bayes already implemented. The goal is to get a better understanding how
the naive Bayes classification works by building it from scratch.


**Sindy asks:**

    In LaTex, why can't we use \\article or \\paragraph? It seems like a lot of LaTex codes online
    resources are not applicable for Anaconda.

Jupyter notebook uses MathJax JavaScript library to render LaTeX. MathJax implements
only a subset of LaTeX commands.

**Matthew asks:**

    For the text classification project, I am thinking of attempting to use word clouds
    (i.e. graphics where the size of words is proportional to their frequency) to visualize the most
    frequent words appearing in positive or negative reviews. Would this be considered a good method
    for data visualization or is it too informal for work in data analytics?

It certainly would be interesting. It is not the most precise way of visualizing data, but it
can give an quick idea what a texts is about.
`Here <https://www.datacamp.com/community/tutorials/wordcloud-python>`_ is a tutorial how you can do it.

**Temitope asks:**

    Is Jupyter notebook used in real time by most organization for relational database management.

Probably not for database management, but it is used by data analysts working with such databases
since it provides tools for retrieving and analyzing data.


**Darren asks:**

    What are some topics that we can look into after completing this course?

The is much more you can learn about machine learning (neural networks, PCA,
support vector machines etc.). Data analysis requires also a good knowledge
of statistics and various mathematics optimization techniques. Other possible
areas are data visualization, natural language processing, databases and so on.

**Sai asks:**

    Is there any extra credit or grade replacing assignment coming ? When is it ?

As I said at the end of the class last Thursday there will be an extra credit assignment
on SQL. I will have it ready in a few days.


**Houlin asks:**

    It's there any research opportunities related to this course that I can applied?

Possibly, as there are many project involving data analysis at UB. You may be able to
find something of interest on the
`UB Experiential Learning Network website <https://www.buffalo.edu/eln/students/project-portal.html>`_.


**Zhongyang asks:**

    We know we can use python to solve data related problems. Can we use python to do math research?
    Like explore more about Bayes theorem.

Sure. You can use Python for mathematical modeling, statistics, symbolic computations etc.


**Souleymane asks:**

    Is the upcoming project our last one?

The naive Bayes project is the last project that is required. There will be one more project
on SQL, but it will be for extra credit.

**Peter asks:**

    Will the extra credit project be worth 10 points?

I will use the extra credit project grade to replace the lowest grade from all other projects,
regardless if the lowest grade was for a 10 point project or one with a lower weight.


**Jonathan asks:**

    What are some different kernels that can be used in KDEs and in what situations
    would you want to apply them?

There are several kernels one can use. For example, ``sklearn.neighbors.KernelDensity``
`has 6 kernel choices <https://scikit-learn.org/stable/modules/density.html#kernel-density-estimation>`_.
There are specific situations when one kernel is more suitable than other ones. However,
the gaussian kernel is used most often, since it gives a smooth KDE function, and because
in many cases the choice of the kernel is not as important as the choice of its bandwidth.


**Elita asks:**

    Will the extra assignment be coding only?

I am still working on it.


**Justin asks:**

    Will there be a curve??

Course grades will be assigned as described in the `syllabus <https://www.mth548.org/#grading>`_.

**Makhtar asks:**

    Would you consider dropping lowest grade and/or excusing more absences or missed
    weekly digests?

I will assign an extra credit project the grade from which will replace the
lowest project grade. 
