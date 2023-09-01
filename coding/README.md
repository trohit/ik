# Basics
## Soft skill qs
- Ask for clarification with examples and boundary conditions
- Keep thinking aloud
  - If I understand properly, I am supposed to..
  - If input is X output should be Y
  - I am not seeing how to optimize it, so will use brute firce algo first.
  - Talk in terms of Big O notation viz. nlogn is a faster soln but needs twice as much mem
    - ![image](https://github.com/trohit/ik/assets/466385/08dd46c0-7d13-4c89-b00f-4a7c2b2375c5)
    - O(1) < O(log n) < O(n) < O(n^2) < O(2^n) < O(n!)
      - 10! > 2^10 > 10^2 so factorial > exponent > polynomial
      - Exponentials have greater complexity than polynomials
      - Factorials have greater complexity than exponentials
    - https://www.freecodecamp.org/news/big-o-notation-why-it-matters-and-why-it-doesnt-1674cfa8a23c/
    - https://www.geeksforgeeks.org/analysis-algorithms-big-o-analysis/
    - 
 
### Qs to ask at end

## Basic Data structures and Algos
- Arrays 
  - +ves: O(1) access by index
  - -ves: Insert/ Del :O(n)* unless sorted, needs contiguous mem
- Linked Lists
- Hash
- Tree
- Binary Search
- Sorting
- Heap, Tree, Trie , Skip List
- Regexp
- Bit Manipulation
  - set bit : |
  - clear bit : &
  - toggle | flip bit : ^
  - shift left
  - shift right
  - get n'th bit 
- Recursion
- Dynamic Programming
- 
  
## Basic Interview qs
- Reverse Linked List
- Implement a Cache
- Given an int n, retutn nth elm of Fibonacci sequence
  - Simple Soln 
```
def fib(n:int)->int:
  if n < 2: return n
  return fib(n-1) + fib(n-2)
```
  - Dyn Pgm Soln
```
def init_vals(max: int):
  seq = [0, 1]
  for i in range(2, max):
    seq.append(n-1) + seq.append(n-2)

def fib(n:int):
  return seq[n] 
```
- Two Sum: https://leetcode.com/problems/two-sum/
  - Brute Force: O(n)
  - Hashmap that uses key,val
- Valid Parentheses: https://leetcode.com/problems/valid-parentheses/
- Auto Complete : https://leetcode.com/problems/design-search-autocomplete-system/ (premium)
  -  
# Refs
- [Youtube Pure How To Nail Your Next Technical Interview](https://www.youtube.com/watch?v=wOn5Dr2mAB4&t=893s)
- [Leetcode py solutions](https://dxmahata.gitbooks.io/leetcode-python-solutions/content/)
- [DS course on LC](https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/)
- [Github link Grokking Coding interview patterns](https://github.com/dipjul/Grokking-the-Coding-Interview-Patterns-for-Coding-Questions)
- [neetcode 75](bit.ly/neetcode75)

