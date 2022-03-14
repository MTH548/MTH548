Weekly Digest 6
===============

**Steven asks:**

    Is there any ways to do geo mapping using px or sns?

Yes, I will talk about one way (choropleth maps) on Monday. 
There are also several Python libraries (e.g. folium) that 
provide more tools for plotting geographical data. 

**Scott asks:**

    I know you can use Esc + M to go to a markdown cell, but is 
    there a similar mechanic to go to a code cell? Do you prefer 
    plotly or seaborn when both can be used for the same application 
    (is one computationally faster)?

You can use Esc + Y to convert a cell into a code cell. As for plotly/seaborn 
preference - it depends. Plotly interactivity can be very useful, but sometimes 
a static image is enough. Also, to provide the interactivity, plotly internally stores 
all data used to create the plot. This means that is you are plotting a lot of data
with plotly, the file with the plots (e.g. a Jupyter Notebook file) may become very 
large and even opening it may take a lot of time. This is not a problem with 
seaborn/matplotlib, since the size an image file will depend only on the resolution 
of the image, not on what is plotted. In other words, which library is better will 
depend on a particular application. 


**Griffin asks:**

    Will 3D graphing play a role in future projects?

Probably not (unless you find a way to use it).


**Linggan asks:**

    Are all projects weight 10 points?

No, there will be 1-2 shorter ones with a lower weight. 

**Carter asks:**

    Does 3-D plotting typically take more time than 3-D?

Do you mean 3-D vs 2-D plotting? This should not make a significant difference. 
On the other hand, plotting a large amount of data (in either format) can take 
more time. 


**bochun asks:**

    For the last project, I've seen the report's feedback, and I'm not sure about calculating 
    the correctness for part I. I've printed out the clusters' centroids images, and there's only 7 
    distinctive numbers instead of 10, which means the clusters are not converged correctly. 
    I think that is also the reason that makes the corrcetness drops. But the feedback says the way 
    I calculate correctness is wrong. I'm confused about this. 

Please read my comments in the body of your report, I explained it there. You calculated for what 
fraction of images the image label agreed with the number of the cluster the image was placed in. 
Numbering of clusters is created randomly by k-means, so there is no reason to expect that 
images of the digit 0 should in the cluster number 0 and so on. The best you can expect is 
that the majority of images of zero will be put together in the same cluster, but the number of 
the cluster has no meaning. The analysis you were expected to performed was to check if clusters 
created by k-means consist of images of the same digit, or if they mix different digits. In the 
second case, it is also good to have a look which digits are mixed with what other digits.      


**Mikhael asks:**

    Any other easy to code libraries like pandas and plotly for visualizing data?

You can have a look at bokeh, altait, ggplot, holoviews. Then there 
are also more specialized libraries, e.g. folium for visualizing geographical information 
etc. 


**Michael asks:**

    What are some current, relevant, real-world projects that are dependent on the use of 
    data frames?

Pandas and pandas dataframes can be useful, for example, in all cases where one would use
Excel. Since Excel is ubiquitous, thus so are potential applications of pandas. 
I am using pandas to keep track who submitted these weekly digests and 
to process them to a format that can be posted on the course website. I will also use 
pandas to compute final grades in this course based on grades from the individual project 
reports. 


**Cassandra asks:**

    For the Baby Names project, is there a specific number of facets that we should look at? 
    Or is it more based on overall length?  

I don't have specific requirements with respect to the number of topics you should pursue. 
You can work with even just one topic if you develop it in a greater depth. The report is 
supposed to contain an analysis of some facet (or facets) of the data and describe the results 
in an interesting way. I expect that it will involve several code cells with pandas 
code to process the data, and some plots to visualize the results. As usual, this should be 
accompanied by a well-developed narrative.


**Jason asks:**

    Are we going to be learning about more advanced data visualization techniques?

We may come across a few other tools for visualizing data, but it will not be the main focus. 


**Anjali asks:**

    Will you be demonstrating how to use platforms for machine learning like pytorch 
    and tensorflow?

No, there is only so much that can fit in a single course. 

**Thinh asks:**

    Is there any chance the lowest project will be dropped at the end of the semester given that 
    we are not familiar with doing the report at the beginning of the semester?

No, but if the first report grade will be much weaker than all subsequent grades, 
then I will take it into account while assigning the final course grades. 

**Ninghui asks:**

    Algorithm from Sklearn can also deal with Dataframe just like ndarray? How does 
    the algorithe know what data type it is?

Most skleans algorithms should work fine with dataframes. The data in a dataframe 
must be of a suitable type. If an algorithm expects numerical data, and you use it with 
a dataframe that contains a column of strings, then you will get an error. 

**David asks:**

    Will we be using pytorch or tensorflow in the future?

No, there is only so much that can fit in a single course. 


**Farhat asks:**

    Can you concatenate rows? 

Rows of two dataframes? You can do it using :code:`pd.concat()`. I showed an exmaple of this 
in class last week. See my notebook from week 6.

**Netra asks:**

    Is there a way you could create a private chat (allows only two) in the discord for code-sharing purposes?

Yes. Discord has private chats. To create one, you can right click on my name in Discord and select "Message"
from the menu that will pop up. Discord also supports private voice/video calls. 

**Felix asks:**

    Will we be doing more advanced machine learning stuff in this class like recursive neural networks etc?

There will be more machine learning, but I will not cover neural networks. 

**Haiyi asks:**

    How to merge data horizontally when merging data?

Merging on rows is rarely useful. If you want to do it, then you can apply the :code:`transpose()` method 
to both dataframes. This will flip the dataframes, making each row into a column. Then you can apply 
:code:`pd.merge()` to the transposed dataframes. 


**Dakota asks:**

    Can we go over our project 2 in office hours with you if we want to know what we did wrong?

Yes, of course.


**Anna asks:**

    What other imports will we be using?

We will use a few libraries that we have not used yet: requests, bs4, json etc.

**Meaghan asks:**

    With such big data sets, what is the best way to make sure we are accurately representing 
    the data we are given, graph/chart-wise and code-wise as well?

The data sets we are working with are not that large from the perspective of the modern 
data science.  How to best represent data will depend on what you want to represent. Sometimes 
a simple printout will be informative, sometimes it will be better to use a plot
of some kind. 

**Qiang asks:**

    Can we get some specific hints about the bonus? 

To get a bonus you need to prepare a very good report, and incorporate in it something 
that goes beyond the normal requirements. For example, in project 2 you were asked 
to complete either part 2a or 2b of the project. Some students wrote very good reports
in which they completed both part 2a and 2b, and I gave them a bonus for this.  

**Metin asks:**

    Is there a way to save plotly plots such that their interactive property would be preserved? 
    In details; first, is there such an image format, and second, is there a way to integrate it into 
    a pdf document through LaTeX or into a powerpoint file such that the interactive feature is preserved?

You can save plotly plots as HTML files with all intractivity preserved. I showed an example how to do it 
last week - see my notebook from week 6. Such files can be then embedded in webpages. PowerPoint has 
plug-ins that allow one to embed HTML content in slides, so it should work with plotly plots too 
(I have not used it myself though). I don't think that you can embed an interactive plotly plot in a pdf file.


