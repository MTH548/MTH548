
Functions
=========

Functions basics
----------------

Functions are a basic tool for organizing programs in Python (and in
other programming languages). A function is essentially a block a code
with a name. It we want to use a function then we can simply call it by
its name. The syntax for defining functions is as follows:

.. parsed-literal::

    def <function name>(<function arguments>):
   	<code>

**Example.** The following function multiplies two numbers and prints
the result:

.. nbinput::

    def multiply(a, b):
        c = a*b
        print('{0}*{1} = {2}'.format(a, b, c))

.. nbinput::

    multiply(3,2)


.. nboutput::
    3*2 = 6


.. nbinput::

    multiply(12,13)


.. nboutput::

    12*13 = 156


A function can return one or more values using the ``return`` statement.
This statement is optional since in general a function does not need to
return anything. However, a function will stop executing as soon as the
``return`` statement is encountered.

**Example.** The following function takes as its argument a string, and returns
the first vowel in the string:

.. nbinput::

    def first_vowel(s):
        for letter in s:
            if letter in ['a', 'e', 'i', 'o', 'u']:
                return letter
        return 0

.. nbinput::

    first_vowel('scratches')


.. nboutput::
    .. parsed-literal::

        [1, 2, 3]
        [1, 2, 3]
        [1, 2, 3]
        [1, 2, 3]
        [1, 2, 3]
        [1, 2, 3]
        [1, 2, 3]
        [1, 2, 3]
        [1, 2, 3]
        [1, 2, 3]
        [1, 2, 3]
        [1, 2, 3]
        [1, 2, 3]
        [1, 2, 3]
        [1, 2, 3]
        [1, 2, 3]
        [1, 2, 3]
        [1, 2, 3]
        [1, 2, 3]
        [1, 2, 3]
        [1, 2, 3]
        [1, 2, 3]
        [1, 2, 3]
        [1, 2, 3]
        [1, 2, 3]
        [1, 2, 3]
        [1, 2, 3]
        [1, 2, 3]
        [1, 2, 3]
        [1, 2, 3]
        [1, 2, 3]
        [1, 2, 3]
        [1, 2, 3]
        [1, 2, 3]
        [1, 2, 3]
        [1, 2, 3]
        [1, 2, 3]
        [1, 2, 3]
        [1, 2, 3]
        [1, 2, 3]
        [1, 2, 3]
        [1, 2, 3]
        [1, 2, 3]
        [1, 2, 3]
        [1, 2, 3]
        [1, 2, 3]
        [1, 2, 3]
        [1, 2, 3]
        [1, 2, 3]
        [1, 2, 3]
        [1, 2, 3]
        [1, 2, 3]
        [1, 2, 3]
        [1, 2, 3]
        [1, 2, 3]
        [1, 2, 3]
