# UCSDx-ALGS200x
My solutions to University of California San Diego's Algorithmic Design and Techniques' programming assignments

## Programming Assignments

### 1. [Fibonacci Numbers](https://github.com/KennethSee/UCSDx-ALGS200x/blob/master/fibonacci.py)

#### Problem Introduction
Recall the definition of Fibonacci sequence: 𝐹<sub>0</sub> = 0, 𝐹<sub>1</sub> = 1, and 𝐹<sub>𝑖</sub> = 𝐹<sub>𝑖</sub>−1 +𝐹<sub>𝑖</sub>−2 for 𝑖 ≥ 2. Your goal in this problem is to implement an efficient algorithm for computing Fibonacci numbers. The starter files for this problem contain an implementation of the following naive recursive algorithm for computing Fibonacci numbers in C++, Java, and Python3:
<pre><code>
Fibonacci(𝑛):
if 𝑛 ≤ 1:
  return 𝑛
return Fibonacci(𝑛 − 1) + Fibonacci(𝑛 − 2)
</pre></code>
Try compiling and running a starter solution on your machine. You will see that computing, say, 𝐹<sub>40</sub> already takes noticeable time. Another way to appreciate the dramatic difference between an exponential time algorithm and a polynomial time algorithm is to use the following visualization by David Galles: http://www.cs.usfca.edu/~galles/visualization/DPFib.html. Try computing 𝐹<sub>20</sub> by a recursive algorithm by entering “20” and pressing the “Fibonacci Recursive” button. You will see an endless number of recursive calls. Now, press “Skip Forward” to stop the current algorithm and call the iterative algorithm by pressing “Fibonacci Table”. This will compute 𝐹20 very quickly. (Note that the visualization uses a slightly different definition of Fibonacci numbers: 𝐹<sub>0</sub> = 1 instead of 𝐹<sub>0</sub> = 0. This of course has almost no influence on the running time.)

#### Problem Description
**Task.** Given an integer 𝑛, find the 𝑛th Fibonacci number 𝐹<sub>𝑛</sub>.

**Input Format.** The input consists of a single integer 𝑛.

**Constraints.** 0 ≤ 𝑛 ≤ 45.

**Output Format.** Output 𝐹<sub>𝑛</sub>.

### 2. [Last Digit of a Large Fibonacci Number](https://github.com/KennethSee/UCSDx-ALGS200x/blob/master/fibonacci_last_digit.py)

#### Problem Introduction
Your goal in this problem is to find the last digit of 𝑛<sup>th</sup> Fibonacci number. Recall that Fibonacci numbers grow exponentially fast. For example, <p align="center">𝐹<sub>200</sub> = 280 571 172 992 510 140 037 611 932 413 038 677 189 525 .</p>
Therefore, a solution like
<pre><code>
𝐹[0] ← 0
𝐹[1] ← 1
for 𝑖 from 2 to 𝑛:
  𝐹[𝑖] ← 𝐹[𝑖 − 1] + 𝐹[𝑖 − 2]
print(𝐹[𝑛] mod 10)
</pre></code>
will turn out to be too slow, because as 𝑖 grows the 𝑖<sup>th</sup> iteration of the loop computes the sum of longer and longer numbers. Also, for example, 𝐹<sub>1000</sub> does not fit into the standard C++ int type. To overcome this difficulty, you may want to store in 𝐹[𝑖] not the 𝑖<sup>th</sup> Fibonacci number itself, but just its last digit (that is, 𝐹<sub>𝑖</sub> mod 10). Computing the last digit of 𝐹𝑖 is easy: it is just the last digit of the sum of the last digits of 𝐹<sub>𝑖</sub>−1 and 𝐹<sub>𝑖</sub>−2:
𝐹[𝑖] ← (𝐹[𝑖 − 1] + 𝐹[𝑖 − 2]) mod 10
This way, all 𝐹[𝑖]’s are just digits, so they fit perfectly into any standard integer type, and computing a sum of 𝐹[𝑖 − 1] and 𝐹[𝑖 − 2] is performed very quickly.

#### Problem Description
**Task.** Given an integer 𝑛, find the last digit of the 𝑛<sup>th</sup> Fibonacci number 𝐹<sub>𝑛</sub> (that is, 𝐹<sub>𝑛</sub> mod 10).

**Input Format.** The input consists of a single integer 𝑛.

**Constraints.** 0 ≤ 𝑛 ≤ 107.

**Output Format.** Output the last digit of 𝐹<sub>𝑛</sub>.

### 3. [Greatest Common Divisor](https://github.com/KennethSee/UCSDx-ALGS200x/blob/master/gcd.py)

#### Problem Introduction
The greatest common divisor GCD(𝑎, 𝑏) of two non-negative integers 𝑎 and 𝑏 (which are not both equal to 0) is the greatest integer 𝑑 that divides both 𝑎 and 𝑏. Your goal in this problem is to implement the Euclidean algorithm for computing the greatest common divisor. Efficient algorithm for computing the greatest common divisor is an important basic primitive of commonly used cryptographic algorithms like RSA.
<pre>
GCD(1344, 217)
=GCD(217, 42)
=GCD(42, 7)
=GCD(7, 0)
=7
</pre>

#### Problem Description
**Task.** Given two integers 𝑎 and 𝑏, find their greatest common divisor.

**Input Format.** The two integers 𝑎, 𝑏 are given in the same line separated by space.

**Constraints.** 1 ≤ 𝑎, 𝑏 ≤ 2 · 109.

**Output Format.** Output GCD(𝑎, 𝑏).

### 4. [Money Change](https://github.com/KennethSee/UCSDx-ALGS200x/blob/master/change.py)

#### Problem Introduction
In this problem, you will design and implement an elementary greedy algorithm used by cashiers all over the world millions of times per day.

#### Problem Description
**Task.** The goal in this problem is to find the minimum number of coins needed to change the input value (an integer) into coins with denominations 1, 5, and 10.

**Input Format.** The input consists of a single integer 𝑚.

**Constraints.** 1 ≤ 𝑚 ≤ 103.

**Output Format.** Output the minimum number of coins with denominations 1, 5, 10 that changes 𝑚.

### 5. [Maximum Value of the Loot](https://github.com/KennethSee/UCSDx-ALGS200x/blob/master/fractional_knapsack.py)

#### Problem Introduction
A thief finds much more loot than his bag can fit. Help him to find the most valuable combination of items assuming that any fraction of a loot item can be put into his bag.

#### Problem Description
**Task.** The goal of this code problem is to implement an algorithm for the fractional knapsack problem.

**Input Format.** The first line of the input contains the number 𝑛 of items and the capacity 𝑊 of a knapsack. The next 𝑛 lines define the values and weights of the items. The 𝑖<sup>th</sup> line contains integers 𝑣<sub>𝑖</sub> and 𝑤<sub>𝑖</sub>—the value and the weight of 𝑖<sup>th</sup> item, respectively.

**Constraints.** 1 ≤ 𝑛 ≤ 10<sup>3</sup>, 0 ≤ 𝑊 ≤ 2 · 10<sup>6</sup>; 0 ≤ 𝑣<sub>𝑖</sub> ≤ 2 · 10<sup>6</sup>, 0 < 𝑤<sub>𝑖</sub> ≤ 2 · 10<sup>6</sup>
for all 1 ≤ 𝑖 ≤ 𝑛. All the numbers are integers.

**Output Format.** Output the maximal value of fractions of items that fit into the knapsack. The absolute value of the difference between the answer of your program and the optimal value should be at most 10<sup>−3</sup>. To ensure this, output your answer with at least four digits after the decimal point (otherwise your answer, while being computed correctly, can turn out to be wrong because of rounding issues).

### 6. [Maximum Advertisement Revenue](https://github.com/KennethSee/UCSDx-ALGS200x/blob/master/dot_product.py)

#### Problem Introduction
You have 𝑛 ads to place on a popular Internet page. For each ad, you know how much is the advertiser willing to pay for one click on this ad. You have set up 𝑛 slots on your page and estimated the expected number of clicks per day for each slot. Now, your goal is to distribute the ads among the slots to maximize the total revenue.

#### Problem Description
**Task.** Given two sequences 𝑎<sub>1</sub>, 𝑎<sub>2</sub>, . . . , 𝑎<sub>𝑛</sub> (𝑎<sub>𝑖</sub> is the profit per click of the 𝑖<sup>th</sup> ad) and 𝑏<sub>1</sub>, 𝑏<sub>2</sub>, . . . , 𝑏<sub>𝑛</sub> (𝑏<sub>𝑖</sub> is the average number of clicks per day of the 𝑖<sup>th</sup> slot), we need to partition them into 𝑛 pairs (𝑎<sub>𝑖</sub>, 𝑏<sub>𝑗</sub>) such that the sum of their products is maximized.

**Input Format.** The first line contains an integer 𝑛, the second one contains a sequence of integers 𝑎<sub>1</sub>, 𝑎<sub>2</sub>, . . . , 𝑎<sub>𝑛</sub>, the third one contains a sequence of integers 𝑏<sub>1</sub>, 𝑏<sub>2</sub>, . . . , 𝑏<sub>𝑛</sub>.

**Constraints.** 1 ≤ 𝑛 ≤ 10<sup>3</sup>; −10<sup>5</sup> ≤ 𝑎<sub>𝑖</sub>, 𝑏<sub>𝑖</sub> ≤ 10<sup>5</sup> for all 1 ≤ 𝑖 ≤ 𝑛.

**Output Format.** Output the maximum value of ∑︀𝑎<sub>𝑖</sub>𝑐<sub>𝑖</sub>, where 𝑐<sub>1</sub>, 𝑐<sub>2</sub>, . . . , 𝑐<sub>𝑛</sub> is a permutation of
𝑏<sub>1</sub>, 𝑏<sub>2</sub>, . . . , 𝑏<sub>𝑛</sub>.

### 7. [Binary Search](https://github.com/KennethSee/UCSDx-ALGS200x/blob/master/binary_search.py)

#### Problem Introduction
In this problem, you will implement the binary search algorithm that allows searching very efficiently (even huge) lists, provided that the list is sorted.

#### Problem Description
**Task.** The goal in this code problem is to implement the binary search algorithm.

**Input Format.** The first line of the input contains an integer 𝑛 and a sequence 𝑎<sub>0</sub> < 𝑎<sub>1</sub> < . . . < 𝑎<sub>𝑛−1</sub> of 𝑛 pairwise distinct positive integers in increasing order. The next line contains an integer 𝑘 and 𝑘 positive integers 𝑏<sub>0</sub>, 𝑏<sub>1</sub>, . . . , 𝑏<sub>𝑘−1</sub>.

**Constraints.** 1 ≤ 𝑛, 𝑘 ≤ 10<sup>4</sup>; 1 ≤ 𝑎<sub>𝑖</sub> ≤ 10<sup>9</sup> for all 0 ≤ 𝑖 < 𝑛; 1 ≤ 𝑏<sub>𝑗</sub> ≤ 10<sup>9</sup> for all 0 ≤ 𝑗 < 𝑘;

**Output Format.** For all 𝑖 from 0 to 𝑘 − 1, output an index 0 ≤ 𝑗 ≤ 𝑛 − 1 such that 𝑎<sub>𝑗</sub> = 𝑏<sub>𝑖</sub> or −1 if there is no such index.

### 8. [Majority Element](https://github.com/KennethSee/UCSDx-ALGS200x/blob/master/majority_element.py)

#### Problem Introduction
Majority rule is a decision rule that selects the alternative which has a majority, that is, more than half the votes. Given a sequence of elements 𝑎<sub>1</sub>, 𝑎<sub>2</sub>, . . . , 𝑎<sub>𝑛</sub>, you would like to check whether it contains an element that appears more than 𝑛/2 times. A naive way to do this is the following.
<pre><code>
MajorityElement(𝑎<sub>1</sub>, 𝑎<sub>2</sub>, . . . , 𝑎<sub>𝑛</sub>):
for 𝑖 from 1 to 𝑛:
  currentElement ← 𝑎<sub>𝑖</sub>
  count ← 0
  for 𝑗 from 1 to 𝑛:
    if 𝑎<sub>𝑗</sub> = currentElement:
      count ← count + 1
  if count > 𝑛/2:
    return 𝑎<sub>𝑖</sub>
return “no majority element”
</pre></code>
The running time of this algorithm is quadratic. Your goal is to use the divide-and-conquer technique to design an 𝑂(𝑛 log 𝑛) algorithm.

#### Problem Description
**Task.** The goal in this code problem is to check whether an input sequence contains a majority element.

**Input Format.** The first line contains an integer 𝑛, the next one contains a sequence of 𝑛 non-negative integers 𝑎<sub>0</sub>, 𝑎<sub>1</sub>, . . . , 𝑎<sub>𝑛−1</sub>.

**Constraints.** 1 ≤ 𝑛 ≤ 10<sup>5</sup>; 0 ≤ 𝑎<sub>𝑖</sub> ≤ 10<sup>9</sup> for all 0 ≤ 𝑖 < 𝑛.

**Output Format.** Output 1 if the sequence contains an element that appears strictly more than 𝑛/2 times, and 0 otherwise.

### 9. [Finding the Closest Pair of Points](https://github.com/KennethSee/UCSDx-ALGS200x/blob/master/points_and_segments.py)

#### Problem Introduction
In this problem, your goal is to find the closest pair of points among the given 𝑛 points. This is a basic primitive in computational geometry having applications in, for example, graphics, computer vision, traffic-control systems.

#### Problem Description
**Task.** Given 𝑛 points on a plane, find the smallest distance between a pair of two (different) points. Recall that the distance between points (𝑥<sub>1</sub>, 𝑦<sub>1</sub>) and (𝑥<sub>2</sub>, 𝑦<sub>2</sub>) is equal to √︀
(𝑥<sub>1</sub> − 𝑥<sub>2</sub>)<sup>2</sup> + (𝑦<sub>1</sub> − 𝑦<sub>2</sub>)<sup>2</sup>.

**Input Format.** The first line contains the number 𝑛 of points. Each of the following 𝑛 lines defines a point (𝑥<sub>𝑖</sub>, 𝑦<sub>𝑖</sub>).

**Constraints.** 2 ≤ 𝑛 ≤ 10<sup>5</sup>; −10<sup>9</sup> ≤ 𝑥<sub>𝑖</sub>, 𝑦<sub>𝑖</sub> ≤ 10<sup>9</sup> are integers.

**Output Format.** Output the minimum distance. The absolute value of the difference between the answer of your program and the optimal value should be at most 10<sup>−3</sup>. To ensure this, output your answer with at least four digits after the decimal point (otherwise your answer, while being computed correctly, can turn out to be wrong because of rounding issues).

### 10. [Money Change Again](https://github.com/KennethSee/UCSDx-ALGS200x/blob/master/change_dp.py)

As we already know, a natural greedy strategy for the change problem does not work correctly for any set of denominations. For example, if the available denominations are 1, 3, and 4, the greedy algorithm will change 6 cents using three coins (4 + 1 + 1) while it can be changed using just two coins (3 + 3). Your goal now is to apply dynamic programming for solving the Money Change Problem for denominations 1, 3, and 4.

#### Problem Description
**Input Format.** Integer money.

**Output Format.** The minimum number of coins with denominations 1, 3, 4 that changes money.

**Constraints.** 1 ≤ money ≤ 10<sup>3</sup>.

### 11. [Primitive Calculator](https://github.com/KennethSee/UCSDx-ALGS200x/blob/master/primitive_calculator.py)

#### Problem Introduction
You are given a primitive calculator that can perform the following three operations with the current number 𝑥: multiply 𝑥 by 2, multiply 𝑥 by 3, or add 1 to 𝑥. Your goal is given a positive integer 𝑛, find the minimum number of operations needed to obtain the number 𝑛 starting from the number 1.

#### Problem Description
**Task.** Given an integer 𝑛, compute the minimum number of operations needed to obtain the number 𝑛 starting from the number 1.

**Input Format.** The input consists of a single integer 1 ≤ 𝑛 ≤ 10<sup>6</sup>.

**Output Format.** In the first line, output the minimum number 𝑘 of operations needed to get 𝑛 from 1. In the second line output a sequence of intermediate numbers. That is, the second line should contain positive integers 𝑎<sub>0</sub>, 𝑎<sub>2</sub>, . . . , 𝑎<sub>𝑘−1</sub> such that 𝑎<sub>0</sub> = 1, 𝑎<sub>𝑘−1</sub> = 𝑛 and for all 0 ≤ 𝑖 < 𝑘 − 1, 𝑎<sub>𝑖+1</sub> is equal to
either 𝑎<sub>𝑖</sub> + 1, 2𝑎<sub>𝑖</sub>, or 3𝑎<sub>𝑖</sub>. If there are many such sequences, output any one of them.

### 12. [Computing the Edit Distance Between Two Strings](https://github.com/KennethSee/UCSDx-ALGS200x/blob/master/edit_distance.py)

#### Problem Introduction
The edit distance between two strings is the minimum number of operations (insertions, deletions, and substitutions of symbols) to transform one string into another. It is a measure of similarity of two strings. Edit distance has applications, for example, in computational biology, natural language processing, and spell checking. Your goal in this problem is to compute the edit distance between two strings.

#### Problem Description
**Task.** The goal of this problem is to implement the algorithm for computing the edit distance between two strings.

**Input Format.** Each of the two lines of the input contains a string consisting of lower case latin letters.

**Constraints.** The length of both strings is at least 1 and at most 100.

**Output Format.** Output the edit distance between the given two strings.

### 13. [Maximum Amount of Gold](https://github.com/KennethSee/UCSDx-ALGS200x/blob/master/knapsack.py)

#### Problem Introduction
You are given a set of bars of gold and your goal is to take as much gold as possible into your bag. There is just one copy of each bar and for each bar you can either take it or not (hence you cannot take a fraction of a bar).

#### Problem Description
**Task.** Given 𝑛 gold bars, find the maximum weight of gold that fits into a bag of capacity 𝑊.

**Input Format.** The first line of the input contains the capacity 𝑊 of a knapsack and the number 𝑛 of bars of gold. The next line contains 𝑛 integers 𝑤<sub>0</sub>, 𝑤<sub>1</sub>, . . . , 𝑤<sub>𝑛−1</sub> defining the weights of the bars of gold.

**Constraints.** 1 ≤ 𝑊 ≤ 10<sup>4</sup>; 1 ≤ 𝑛 ≤ 300; 0 ≤ 𝑤<sub>0</sub>, . . . , 𝑤<sub>𝑛−1</sub> ≤ 10<sup>5</sup>.

**Output Format.** Output the maximum weight of gold that fits into a knapsack of capacity 𝑊.

### 14. [Partitioning Souvenirs](https://github.com/KennethSee/UCSDx-ALGS200x/blob/master/partition3.py)

You and two of your friends have just returned back home after visiting various countries. Now you would like to evenly split all the souvenirs that all three of you bought.

#### Problem Description
**Input Format.** The first line contains an integer 𝑛. The second line contains integers 𝑣<sub>1</sub>, 𝑣<sub>2</sub>, . . . , 𝑣<sub>𝑛</sub> separated by spaces.

**Constraints.** 1 ≤ 𝑛 ≤ 20, 1 ≤ 𝑣<sub>𝑖</sub> ≤ 30 for all 𝑖.

**Output Format.** Output 1, if it possible to partition 𝑣<sub>1</sub>, 𝑣<sub>2</sub>, . . . , 𝑣<sub>𝑛</sub> into three subsets with equal sums, and 0 otherwise.
