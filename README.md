
# What is an algorithm?
* Informally an algorithm is any well-defined computational procedure that takes some value, or set of values, as **input** and produces some value, or set of values, as **output**.
* In other words and algorithm is a sequence of computational steps that transform the **input** into the **output**.
* We can also view an algorithm as a tool for solving a well-defined computational problem. In general, an **instance** of a problem consists of the **input** needed to compute a solution to the problem.
* An algorithm is said to be **correct** if, for every **input instance**, it halts with the **correct output**. We say that a **correct** algorithm solves the given computational problem.
* Contrary to what you might expect, **incorrect** algorithms can sometimes be useful, if we can control their **error rate**.
* Different algorithms devised to solve the same problem often differ dramaticallyt in their **effiency (Time|Memory)**. These differences can be much more significant than diferences due to hardware and software

# What is a data Structures?
* A data structure is a way to **store and organize data** in order to facilitate acccess and modifications.
* No single data structure works well for all purpose, and so it is important to know the strenghts and limitations of several of them


# Algorithms and other technologies
* Algorithms are truly important on contemporary computers, technologies examples:
** Advance computer architectures and fabrication technlogies
  * Easy to use, intuitive, graphical user interface (GUIs)
  * Object oriented systems
  * Integrated Web technologies
  * Fast Networking, both wired and wireless


# Problem
## Comparison of runtimes
For each function *f(n)* and time *t* in the following table, determine the largest size *n* for a problem that can be solved in time *t*, assuming that the algorithm to solve the problem takes *f(n)* microseconds

**Values to calculate the time:**
1. 1 second  = 10<sup>6</sup> *us*
2. 1 min     = 6 x 10<sup>7</sup> *us*
3. 1 hour    = 36 x 10<sup>8</sup> *us*
4. 1 day     = 864 x 10<sup>8</sup> *us*
5. 1 month   = 2.5 x 10<sup>12</sup> *us* 
6. 1 year    = 3.1 x 10<sup>13</sup> *us* 
7. 1 century = 3.1 x 10<sup>16</sup> *us* 



|                      |     1 second               |    1 minute                    |     1 hour                       |     1 day                        |     1 month                       |     1 year                       |    1 centry                       |
|----------------------|----------------------------|--------------------------------|----------------------------------|----------------------------------|-----------------------------------|----------------------------------|-----------------------------------|
| lg<sub>2</sub>(n)    | 2<sup>10<sup>6</sup></sup> | 2<sup>6 x 10<sup>7</sup></sup> | 2<sup>36 x 10 <sup>8</sup></sup> | 2<sup>864 x 10<sup>8</sup></sup> | 2<sup>2.5 x 10<sup>12</sup></sup> | 2<sup>3.1 x 10<sup>13</sup></sup>| 2<sup>3.1 x 10<sup>16</sup></sup> |
| &radic;n             | 10<sup>12</sup></sup>      | 36 x 10 <sup>14</sup>          | 1296 x 10 <sup>16</sup>          | 7.4 x 10 <sup>21</sup>           | 6.7 x 10 <sup>14</sup>            | 9.9 x 10 <sup>26</sup>           | 9.9 x 10 <sup>32</sup>            |
|   n                  | 10<sup>6</sup>             | 6 x 10<sup>7</sup>             | 36 x 10<sup>8</sup>              | 864 x 10<sup>8</sup>             | 2.5 x 10<sup>12</sup>             | 3.1 x 10<sup>13</sup>            | 3.1 x 10<sup>16</sup>             |
| nlg<sub>2</sub>(n)   | 62746                      | 2.8 x 10<sup>6</sup>           | 1.3 x 10<sup>8</sup>             | 2.7 x 10<sup>9</sup>             | 7.1 x 10<sup>10</sup>             | 7.9 x 10<sup>11</sup>            | 6.8 x 10<sup>13</sup>             |
|  n<sup>2</sup>       | 1000                       | 7745                           | 60000                            | 293938                           | 1609968                           | 56515692                         | 56175382                          |
|  n<sup>3</sup>       | 100                        | 391                            | 1532                             | 4420                             | 13736                             | 31593                            | 146677                            |
|  2<sup>n</sup>       | 19.9                       | 25.8                           | 31.74                            | 36.33                            | 41.18                             | 44.81                            | 54.78                             |
|   n!                 | 9                          | 11                             | 12                               | 13                               | 15                                | 16                               | 17                                |

# Math Extra:
1. https://www.khanacademy.org/math/cc-sixth-grade-math/cc-6th-arithmetic-operations/cc-6th-exponents/v/introduction-to-exponents
2. https://www.khanacademy.org/math/algebra2/x2ec2f6f830c9fb89:logs/x2ec2f6f830c9fb89:log-intro/a/intro-to-logarithms

# Math Symbol Codes
https://sites.psu.edu/symbolcodes/codehtml/#math

# Book solutions
ce&matchtype=b&gclid=CjwKCAiA_9r_BRBZEiwAHZ_v1y1GiOiw6x6pSeifMdRPqYqQeaJ_yEmdD22IFhuuwbGqzfSo8t2-shoCqhAQAvD_BwE&gclsrc=aw.ds
