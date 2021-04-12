Weekly Digest 10
================

**Makenzie asks:**

    Is there a generalization of KDE to partitions of unity?

In partition of unity functions add up to 1. In KDE integrals add up to one.
These are different concepts with different applications.

**Renjie asks:**

    I saw you mentioned that you are measuring voice channel participation.
    But I didn't really joined the voice channel every time. For the most times,
    I just stayed in the text channel.  Will this be affect the participation  
    grade a lot? Also, should we stayed in the channel all the time or just when 
    you ask us to go to discord?

I expect students on Discord during class time when I say that we will be moving
to work on Discord. There is no way to see if someone is on a text channel - no way 
to see what they are doing, collaborate with them etc. - so this does not count. 
You should be on a voice channel. As for grading, I will think how to factor Discord 
presence in.

**zhongyang asks:**

    Which part of math knowledge is more helpful to data analyze? For example,
    I think geometry is not that helpful, but statistics and probability can be very helpful.

For data analysis and machine learning the most frequently used areas of mathematics
are probability and statistics, linear algebra, calculus, some differential equations.
However, other fields of mathematics are used too. For example, geometry does come 
into play in the topological data analysis.

**Guozheng asks:**

    How many project left in the remain week?

Either 2 or 3.

**Sean asks:**

    What other kernels does python provide other than gaussian? And where are they most useful?

Gaussian kernel is used most frequently. In many applications the shape of the kernel
is not as important as the choice of the bandwidth of the kernel. Machine learning libraries
usually implement several kernel shapes. For example, ``sklearn.neighbors.KernelDensity``
`has 6 kernel choices <https://scikit-learn.org/stable/modules/density.html#kernel-density-estimation>`_.
As a side note, ``sklearn.neighbors.KernelDensity`` has some peculiarities (e.g. it computes
logarithms of probabilities rather than probabilities themselves) which is why I decided
to use ``scipy.stats.gaussian_kde`` in this course - it has fewer features but it
is easier for simple applications.


**Jeffrey asks:**

    Would KDE be better to analyze data than utilizing k-NN and k-Means? 

k-Means is a clustering algorithm, so it serves a different purpose, but k-NN and KDE are similar 
in some respects. For example, both can be used to classify data. Which one will work better 
depends on a particular problem. One of the tasks of the next project is to compare accuracy
of k-NN and KDE in predicting if a marathon runner was a male or female.  


**Amena asks:**

    How many more projects are left until the semester is over?

We should have time for 2-3 more projects (counting the one on KDE and marathon results).


**Mohammedanas asks:**

    Can we have a small project that would count as extra credit to help us improve our grade?

I will think about it. No promises though. 


**Matthew asks:**

    Is it possible to do a KDE with more than 2-dimensions? (e.g., if we used time, age, and a third 
    statistic like height or body weight on the marathon runner KDE.

Sure, you can compute KDE for data with any number of dimensions. 


**Max asks:**

    Machine learning seems to be a useful tool when knowing what it is that you're looking for. Is the reason 
    why even with its advances it is still difficult to use the fact that there is so much data and too many 
    possible answers?

I guess one reason boils down to what you wrote yourself: in order to find good answers you need to know 
first what you are looking for, and figuring it out is not easy.  

**Darren asks:**

    In the Jupyter notebook, if we accidentally delete a cell, is there a way to bring back the cell?

Yes, the Edit menu of the notebook has an option "Undo delete cells". Or you can use escape-z keyboard 
shortcut. 

**Peter asks:**

    Can you work through Part II of the fifth project? I think I was mainly tripped up on finding the differences 
    between the join/leave logs. 

I don't want to spend time on it in class, but I can show you how this can be done after class 
or during office hours, just ask.  

**Sai asks:**

    Can we effectively use types of plates I mean colour variations in graphs to make it effective? 

I am not sure if this is what you are asking, but if you search online, you will find a lot of 
resources discussing which color combinations or color maps are effective in data visualization. 
This is an interesting topic. 


**Makhtar asks:**

    Since we are doing machine learning, are we going to do any regression model ?

I wold like to do it, but at this point I don't think we will have time. There is only so much 
we can do in a single semester. 


**Seungmin asks:**

    When it comes to analyzing information what kind of questions should come into mind?

In the greatest generality, what kind of story you can tell using data. Good data analysts 
should be able to provide narrative explaining what given data means. 


**Justin asks:**

    No question

Asking a question is a part of this assignment. 


**Elita asks:**

    Is Jupyter Notebook used in any professional settings?

Sure, it is commonly used for data analysis and scientific computing. 


**Alexander asks:**

    Are there any places you recommend to look at for entry level data analysts? Or even 
    before that any more things to learn before searching?

Locally, M&T Bank used to hire several students each year for data analyst/financial analyst 
positions. I don't know if this has changed due to the COVID situation. In any case, you 
can just look what jobs are advertised and apply. Building a portfolio of projects 
on Kaggle or GitHub may help.