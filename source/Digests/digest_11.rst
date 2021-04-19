Weekly Digest 11
================

**Sindy asks:**

    what's the difference between re.sub and r.sub

I guess you are referring to the code of the ``re_show`` function. In this code
``r`` is a variable assigned to a compiled regex pattern. Then ``r.sub`` is
the ``sub`` method applied to this pattern.


**Guozheng asks:**

    I still confusing about the ? and +, how are they different?

``+`` indicates that the preceeding pattern should be repetition one or more
times. ``?`` indicates that the preceding pattern should be matched in
a non-greedy manner, i.e. it should give the shortest possible match.


**Kevin asks:**

    Is it possible to compress strings to even smaller bits of data?

I depends on what you want to accomplish. If you want to store strings using less
space, then there are various data compression algorithms for this.


**Waleed asks:**

    Could we do an extra credit assignment, a suggestion would be to take a dataset
    from Kaggle and so something interesting for it, someone data analysis related could
    be worth half a project, something machine learning related could be worth 1 homework?

I will think about it.


**Zhongyang asks:**

    In data analyze, do we use 2-dimensional or 3-d plot more frequently? Is there 4-d
    plot or higher dimensional plot used in data analyze?

2-dimensional plots are more frequent, since it is usually easier and clearer to produce
them on a 2-dimensional screen or paper. It is possible to create something imitating a 4-dimensional
plot by plotting its intersections with 3-dimensional spaces. For higher dimensional data,
the usual approach is to first use dimensionality reduction to decrease the number
of dimensions while preserving as much information as possible, and then plot the data.


**Miguel asks:**

    What is the best library to implement a 3d scatter plot

Such plots can be created with a number of libraries - e.g. matplotlib, plotly or bokeh.
Which one is the best is largely a subjective opinion.


**Sean asks:**

    Will we be discussing NFAs or DFAs in this class?

No. This is an interesting topic but for a different course.

**Temitope asks:**

    What is the drawback of using KDE over other machine learning algorithms

It is difficult to answer this in such generality. Which algorithm is better
or worse depends on what you are trying to accomplish with it.

**Hannah asks:**

    The class website is very well organized and helpful, with a lot of resources
    that would be great not only for this class but future ones and research as well.
    How long do you plan on keeping this website up? If you're taking it down after
    the semester, is there a way for me to save a local copy?

The website will probably stay online until spring 2022 semester when this course
will be offered again. Source files are on `GitHub <https://github.com/MTH548/MTH548_site>`_.

**Sai asks:**

    As i see in the project obtained using the k-NN classifier, and they is even
    Add anything else that you find relevant and interesting can u give a example .

I don't understand the question.

**Matthew asks:**

    Will there be work due for this class during finals period or will all of the remaining
    projects be due before classes are over?

I have not decided on it yet. However, if there will be something due during the finals
week it will be optional, for extra credit.


**Renjie asks:**

    The points that each project weight, is that equal to how many percent of our grade?

All project taken together are worth 80% of the final grade. The number of points
indicates what weight each project has toward this 80%.

**Alexander asks:**

    What kind of things will we be learning with SQL, and with that will we be starting
    SQL soon?

We will go over creating and altering tables, SQL queries, joins etc. We should get to it
next week.


**Souleymane asks:**

    Having used different methods to solve problems over the past few months, how much more
    work would be necessary to say we have a firm grasp on libraries like numpy and sklearn?
    I know there's a huge amount of information available in both libraries but what are the
    fundamentals that we have to know to call ourselves proficient?

I am not sure how to answer it. As you will get more experience with these libraries,
you will feel more proficient and you will be able to do more with them without difficulty.
But then, there will be always something new to learn. So, it will be always work
in progress.

**Darren asks:**

    What is the difference between numpy and scipy?

Numpy provides tools for creating and manipulating arrays. Scipy adds functions for performing
more specialized mathematical computations with numpy arrays. This includes statistical
computations, linear algebra computations, Fourier transform, intergration etc.


**Max asks:**

    Can regex be used to search for emojis? If so maybe that can be an interesting way to
    understand the mood of text messages rather than by analyzing the actual text. (I had
    to verify that I'm not a robot, have people started using what you've taught us to submit
    this part of the assignment without doing the work :) )

Python ``re`` module works with unicode encoded strings, so yes, it could be used to
search for emojis. As for verifying that you are not a robot, Google forms must have gotten
suspicious for some reason, I did not change any settings myself. If someone would write
a convincing bot to complete these digests, I would have to figure out if this cheating or
an extra credit effort :). But then, for a very convincing bot I would never know.


**Justin asks:**

    None

Asking a question is a part of this assignment.


**Makhtar asks:**

    is the project about parsing strings the last one?

No, there will be one more on SQL.


**Elita asks:**

    Is there a way to find a list of shortcuts on Jupyter like for example Markdowns?

A link to a page with Markdown reference is posted on the `course website
<https://www.mth548.org/useful_links.html>`_. This reference does not cover LaTeX
(which is used to typeset math formulas), but there is another link on the same
page pointing of a list of LaTeX math symbols.

A list Jupyter notebook keyboard shortcuts is availble in the notebook itself.
Click on the Help menu and then on Keyboard Shortcuts.


**Amena asks:**

    How can we check our participation grade?

If you know how many times you missed a class or a weekly digest you can calculate it
yourself: there is no consequence of the first class and digest missed, then 2% off
for each subsequent one missed. I don't have these statistics ready, I will compute
them once the semester is finished. 


**Houlin asks:**

    Can we use Raw string method in a website to search some contents  that we want?

Sure, regular expressions are often used as one of tools for web scrapping.


**Jeffrey asks:**

    You've shown us the contour image on the XY-plane for the 3D models, is it also important
    to look at the image on the XZ-plane and YZ-plane as well or just looking at the XY-plane
    is significant  image to tell what is happening?

This may be useful in some cases, but for plots of functions of two variables x and y
the XY-plane contour plot is most meaningful, since it visualizes the values of a function.



**Jonathan asks:**

    The usage of the gaussian kernel seems obvious to me from taking probability theory but
    do you happen to know of examples where other kernels are more appropriate in data analysis?

There are theoretical results showing that the Epanechnikov kernel (whose shape is an upside down
parabola) can give better results than the gaussian kernel. However, in practice the
choice of the kernel usually does not make a lot of a difference. The choice of the bandwidth is
much more important. Since KDE obtained using the gaussian kernel is a differentiable function
and KDE coming from the Epanechnikov kernel is not, gaussian kernel is used more often.
