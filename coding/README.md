# Basics
## Soft skill qs
- 1
### Qs to ask at end

## Basic Data structures and Algos
- Arrays
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
