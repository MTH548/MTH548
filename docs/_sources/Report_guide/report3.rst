
Example: Output formatting
__________________________

**Bad:** Code output is misaligned, there are too many decimal digits,
and variable names are unnecessarily repeated in each row.


.. raw:: html

   <a href = "../_static/report_guide/report_sample3a.html">
   <img src="../_static/report_guide/report_sample3a.png" style="padding:1px; border:2px solid #C4C4C4; display: block;">
   </a>


**Good:** Code output is arranged into an easy to read table. Insignificant digits in the decimal expansion are truncated.


.. raw:: html

   <a href = "../_static/report_guide/report_sample3b.html">
   <img src="../_static/report_guide/report_sample3b.png" style="padding:1px; border:2px solid #C4C4C4; display: block;">
   </a>


**Fancier options.** Python and Jupyter notebook provide more
sophisticated tools that can be used to format code output in various ways.
The table below was produced in a Jupyter notebook using the same data as
in the above examples, but with some extra formatting code. You don't need to
use such formatting, but this is an illustration of what is possible.




.. raw:: html


            <style  type="text/css" >
                table {
                   margin-left: 0%;
                }

                #T_2cf1831a_1651_11e7_be6f_34363bd21df6 th:first-child {

                    display: none;

                }

                #T_2cf1831a_1651_11e7_be6f_34363bd21df6 th {

                    border-radius: 3px;

                    font-size: 90%;

                    background-color: DarkSeaGreen;

                    padding-right: 7pt;
                    padding-top: 2pt;
                    padding-bottom: 2pt;

                    border-left: white solid 1px;
                    border-right: white solid 1px;

                    color: black;

                    text-align: right;

                }

                #T_2cf1831a_1651_11e7_be6f_34363bd21df6 td {

                    font-size: 90%;

                    border-radius: 3px;

                    padding-bottom: 0pt;

                    font-family: Courier;

                    padding-right: 7pt;
                    padding-top: 2pt;
                    padding-bottom: 2pt;

                    border-left: white solid 1px;
                    border-right: white solid 1px;

                    text-align: right;

                    width: 50pt;

                }

                #T_2cf1831a_1651_11e7_be6f_34363bd21df6 tr:nth-child(even) {

                    background-color: Beige;

                }

                #T_2cf1831a_1651_11e7_be6f_34363bd21df6 tr:nth-child(odd) {

                    background-color: FloralWhite;

                }

                #T_2cf1831a_1651_11e7_be6f_34363bd21df6 tr:hover {

                    color: red;

                    transition: color 0.5s;

                }


            </style>

            <table id="T_2cf1831a_1651_11e7_be6f_34363bd21df6" None>


            <thead>

                <tr>

                    <th class="blank">

                    <th class="col_heading level0 col0">t

                    <th class="col_heading level0 col1">v

                    <th class="col_heading level0 col2">h

                </tr>

            </thead>
            <tbody>

                <tr>

                    <th id="T_2cf1831a_1651_11e7_be6f_34363bd21df6" class="row_heading level2 row0">
                        0

                    <td id="T_2cf1831a_1651_11e7_be6f_34363bd21df6row0_col0" class="data row0 col0">
                         0.00

                    <td id="T_2cf1831a_1651_11e7_be6f_34363bd21df6row0_col1" class="data row0 col1">
                        10.00

                    <td id="T_2cf1831a_1651_11e7_be6f_34363bd21df6row0_col2" class="data row0 col2">
                         0.00

                </tr>

                <tr>

                    <th id="T_2cf1831a_1651_11e7_be6f_34363bd21df6" class="row_heading level2 row1">
                        1

                    <td id="T_2cf1831a_1651_11e7_be6f_34363bd21df6row1_col0" class="data row1 col0">
                         0.20

                    <td id="T_2cf1831a_1651_11e7_be6f_34363bd21df6row1_col1" class="data row1 col1">
                         8.04

                    <td id="T_2cf1831a_1651_11e7_be6f_34363bd21df6row1_col2" class="data row1 col2">
                         1.80

                </tr>

                <tr>

                    <th id="T_2cf1831a_1651_11e7_be6f_34363bd21df6" class="row_heading level2 row2">
                        2

                    <td id="T_2cf1831a_1651_11e7_be6f_34363bd21df6row2_col0" class="data row2 col0">
                         0.40

                    <td id="T_2cf1831a_1651_11e7_be6f_34363bd21df6row2_col1" class="data row2 col1">
                         6.08

                    <td id="T_2cf1831a_1651_11e7_be6f_34363bd21df6row2_col2" class="data row2 col2">
                         3.22

                </tr>

                <tr>

                    <th id="T_2cf1831a_1651_11e7_be6f_34363bd21df6" class="row_heading level2 row3">
                        3

                    <td id="T_2cf1831a_1651_11e7_be6f_34363bd21df6row3_col0" class="data row3 col0">
                         0.60

                    <td id="T_2cf1831a_1651_11e7_be6f_34363bd21df6row3_col1" class="data row3 col1">
                         4.11

                    <td id="T_2cf1831a_1651_11e7_be6f_34363bd21df6row3_col2" class="data row3 col2">
                         4.23

                </tr>

                <tr>

                    <th id="T_2cf1831a_1651_11e7_be6f_34363bd21df6" class="row_heading level2 row4">
                        4

                    <td id="T_2cf1831a_1651_11e7_be6f_34363bd21df6row4_col0" class="data row4 col0">
                         0.80

                    <td id="T_2cf1831a_1651_11e7_be6f_34363bd21df6row4_col1" class="data row4 col1">
                         2.15

                    <td id="T_2cf1831a_1651_11e7_be6f_34363bd21df6row4_col2" class="data row4 col2">
                         4.86

                </tr>

                <tr>

                    <th id="T_2cf1831a_1651_11e7_be6f_34363bd21df6" class="row_heading level2 row5">
                        5

                    <td id="T_2cf1831a_1651_11e7_be6f_34363bd21df6row5_col0" class="data row5 col0">
                         1.00

                    <td id="T_2cf1831a_1651_11e7_be6f_34363bd21df6row5_col1" class="data row5 col1">
                         0.19

                    <td id="T_2cf1831a_1651_11e7_be6f_34363bd21df6row5_col2" class="data row5 col2">
                         5.09

                </tr>

                <tr>

                    <th id="T_2cf1831a_1651_11e7_be6f_34363bd21df6" class="row_heading level2 row6">
                        6

                    <td id="T_2cf1831a_1651_11e7_be6f_34363bd21df6row6_col0" class="data row6 col0">
                         1.20

                    <td id="T_2cf1831a_1651_11e7_be6f_34363bd21df6row6_col1" class="data row6 col1">
                        -1.77

                    <td id="T_2cf1831a_1651_11e7_be6f_34363bd21df6row6_col2" class="data row6 col2">
                         4.94

                </tr>

                <tr>

                    <th id="T_2cf1831a_1651_11e7_be6f_34363bd21df6" class="row_heading level2 row7">
                        7

                    <td id="T_2cf1831a_1651_11e7_be6f_34363bd21df6row7_col0" class="data row7 col0">
                         1.40

                    <td id="T_2cf1831a_1651_11e7_be6f_34363bd21df6row7_col1" class="data row7 col1">
                        -3.73

                    <td id="T_2cf1831a_1651_11e7_be6f_34363bd21df6row7_col2" class="data row7 col2">
                         4.39

                </tr>

                <tr>

                    <th id="T_2cf1831a_1651_11e7_be6f_34363bd21df6" class="row_heading level2 row8">
                        8

                    <td id="T_2cf1831a_1651_11e7_be6f_34363bd21df6row8_col0" class="data row8 col0">
                         1.60

                    <td id="T_2cf1831a_1651_11e7_be6f_34363bd21df6row8_col1" class="data row8 col1">
                        -5.70

                    <td id="T_2cf1831a_1651_11e7_be6f_34363bd21df6row8_col2" class="data row8 col2">
                         3.44

                </tr>

                <tr>

                    <th id="T_2cf1831a_1651_11e7_be6f_34363bd21df6" class="row_heading level2 row9">
                        9

                    <td id="T_2cf1831a_1651_11e7_be6f_34363bd21df6row9_col0" class="data row9 col0">
                         1.80

                    <td id="T_2cf1831a_1651_11e7_be6f_34363bd21df6row9_col1" class="data row9 col1">
                        -7.66

                    <td id="T_2cf1831a_1651_11e7_be6f_34363bd21df6row9_col2" class="data row9 col2">
                         2.11

                </tr>

                <tr>

                    <th id="T_2cf1831a_1651_11e7_be6f_34363bd21df6" class="row_heading level2 row10">
                        10

                    <td id="T_2cf1831a_1651_11e7_be6f_34363bd21df6row10_col0" class="data row10 col0">
                         2.00

                    <td id="T_2cf1831a_1651_11e7_be6f_34363bd21df6row10_col1" class="data row10 col1">
                        -9.62

                    <td id="T_2cf1831a_1651_11e7_be6f_34363bd21df6row10_col2" class="data row10 col2">
                         0.38

                </tr>

            </tbody>
            </table>
