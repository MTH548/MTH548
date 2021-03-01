Weekly Digest 4
===============

**Makenzie asks:**

    What kinds of data types can Pandas fit in a data frame? For example, could one of the
    columns have numpy arrays as entries?

You can store any Python object (e.g. a numpy array) in a pandas DataFrame or Series.

**Waleed asks:**

    Could we get the answers to the project questions to see where we went wrong?

I am available to discuss what went wrong in a report. I will not provide answers,
since most projects are open-ended and there are various ways in which they can be developed.

**Sean asks:**

    Will we continue to learn more about specific python packages that are used in data analytics
    throughout the course? Or will we focus on our own implementations as we go forward?

We will be implementing some tools ourselves when it will help to understand how they work.
At other times we will be using existing Python libraries.

**Mohammedanas asks:**

    Are the final grades for the project curved in anyway, relative to how the
    entire class did?

No, but I am trying to be reasonable. The average of grades for project 1 was just below B+.


**Jeffrey asks:**

    Are there any other benefits to using pandas, other than creating dataframes?
    Is there a way to iterate through pandas dataframe?

The main benefit of pandas is that dataframes provide a lot of tools for manipulating 
data organized in tables.

In most cases iterating over a dataframe is not a good practice. Pandas tools are
designed to avoid explicit iterations. However, iterations are possible. For example
the following code will iterate over rows of a dataframe :code:`df` and print each row:

.. code:: python

  for i in range(len(df)):
      print(df.iloc[i])


**Renjie asks:**

    Will you giving us the average grade for the first project?

The average of grades for report 1 was just below B+.


**Alex asks:**

    What do you think is the most common reason for losing points in projects?

I don't think there was one prevalent reason. Some reports had correct
code, but just a few words of narrative, some had significant coding issues,
and some did not develop the project significantly beyond coding
the :code:`knn()` function. And then there were reports which were just good
in every respect. It there was something amiss, I pointed it out in comments
in the graded reports.

**Temitope asks:**

    How do one know the exact code to use when looking up the code on
    Scikit-learn e.g the right accuracy metric.

I am mot sure if I understand the question. In general how you measure
accuracy will depend on what you are trying to accomplish.

**Guozheng asks:**

    Is there any possible chance that inertia will going up?

With optimal clustering, inertia will go down as the number of clusters increases.
In practice inertia may occasionally go up, since the k-means algorithm is not
guaranteed to find optimal clusters.

**Sai asks:**

    Can we use PCA (Principal component analysis) for dimensionality reduction?

If you are asking if you can use it in general for analyzing data then sure,
it is a very useful tool. If you want to use it for project 2 then talk to me
beforehand so I can check if it is reasonable. PCA is certainly not required
for this project.

**Matthew asks:**

    How do you suggest we keep track of time when we're comparing the speed
    with and without clustering for project #2?

I was showing you the :code:`%%timeit` magic during the first week of classes.
If you would like to use some other way of timing code you can use it too.

**Darren asks:**

    In the pandas function, there was a code to add new columns to our dataframe,
    is there a code to remove columns of our dataframes?

Sure, if :code:`df` if a dataframe, then you can use
:code:`df.drop("column_name", axis=1)`. Using this function with
an index of a row and :code:`axis=0` will remove the row.

**Souleymane asks:**

    How many more projects are left and how much do they ramp up in difficulty?

The future projects should have the same level of difficulty as the
first two. I plan to assign them more or less every two week.


**Houlin asks:**

    Will algorithms like KNN be often used in practical work? Or we only need to know how it work?  

In general, k-NN and k-means are both used very often in data analysis. In this 
course we may encounter them again, but we will be moving to different topics.

**Makhtar asks:**

    Do not you think that sometimes you go a bit fast ?

It is possible. If this happens let me know, say by posting a message in Zoom chat and
I will go slower. 

**Miguel asks:**

    How many total projects will there be?

I plan to assign one every other week (more or less), so around 7. 


**Max asks:**

    Will we ever discuss applying the concepts we learn using other programming languages, or only Python?

We are using Python only in this course. 

**Jonathan asks:**

    How does the k-means algorithm separate each data point into the different clusters? What does the 
    inertia value mean?

If data is subdivided into clusters, then inertia of this subdivision is the sum of squares of distances
from each data point to the center of the cluster to which the point belongs. Smaller inertia means that 
clusters are more tightly packed. k-means algorithm is trying to find subdivision of data into a given 
number of clusters which minimizes the inertia.  

**Justin asks:**

    What was the project average?

The average of project 1 grades was slightly below B+. 





