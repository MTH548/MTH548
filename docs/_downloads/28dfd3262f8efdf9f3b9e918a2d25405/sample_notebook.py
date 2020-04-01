# # Sample notebook
#
# This notebook serves as an illustration of the process of exporting a Jupyter notebook `.ipynb` file to a Python `.py` file.
#
# After the export, content of markdown cells - like this one - should be transformed into commented text in the Python file. Content of code cells should be transformed into raw Python code.
#
# Here is an example of a code cell:

# In[1]:


def welcome(s):
    return f"Welcome {s}!"

for name in ["Martha", "Bob", "Alice"]:
    print(welcome(name))


# **Note.** The export process should discard the output of code cells. Only the content of markdown and code cells and code cell numbers should be preserved.
#
# Here is another code cell:

# In[28]:


# code cells may contain code comments
import string

for x in [x for x in dir(string) if not x.startswith("__")]:
    y = getattr(string, x)
    if type(y) == str:
        print(f"{x}: {y}")


# The content below looks like Python code, but it is a part of a markdown cell, so it should be treated as text:
#
# ```
# N = 100
# for i in range(N):
#     print(5*i)
# ```
#
# One more code cell:

# In[29]:


1+1
