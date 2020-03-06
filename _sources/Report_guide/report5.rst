
Example: Code sequencing
________________________

**Bad:** In the code below the function ``ball_height()`` first appears before it is defined.
This code is confusing to read since when one first sees ``ball_height()`` it is not clear what
it is and where it is coming from.

.. raw:: html

   <a href = "../_static/report_guide/report_sample5a.html">
   <img src="../_static/report_guide/report_sample5a.png" style="padding:1px; border:2px solid #C4C4C4; display: block;">
   </a>

**Also bad:** The code below will work if one executes the bottom code cell before executing
the top one, but anyone reading the report will do it in the opposite order,
from top to bottom, and this will result in an execution error:

.. raw:: html

   <a href = "../_static/report_guide/report_sample5aa.html">
   <img src="../_static/report_guide/report_sample5aa.png" style="padding:1px; border:2px solid #C4C4C4; display: block;">
   </a>


**Good:**  Code is entered sequentially and it is split into separate cells to better explain its purpose and structure.

.. raw:: html

   <a href = "../_static/report_guide/report_sample5b.html">
   <img src="../_static/report_guide/report_sample5b.png" style="padding:1px; border:2px solid #C4C4C4; display: block;">
   </a>
