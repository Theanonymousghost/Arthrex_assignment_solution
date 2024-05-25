# Arthrex_assignment_solution
This is the proposed solution for the problem statement given in the assignment.

**The given code performs a breadth-first search (BFS) to find and record all the connected candidates starting from a given input character. Here's a detailed explanation of its approach:**

**Data Structures:**
- Candidates: A dictionary where each key is a candidate (node) and the corresponding value is a list of other candidates (nodes) they are connected to.
* Contacted: A list to keep track of candidates that have already been processed.
+ Current: A deque (double-ended queue) used for the BFS process, storing candidates to be processed.

**Function Definition:**

1. The function contacted_candidates(char) is defined to take an input character (char) and perform the BFS from this character.
Initial Check and Setup:

2. If the input char is a key in the candidates dictionary, it is appended to current, and its connected candidates are also appended.

3. If the input char is not a key but is found in the values of the dictionary, the function identifies the key(s) (parent node) and appends both the parent node(s) and their connected candidates to current.

**Handling the Initial Input**
1. If char is a key in candidates:
  - Append char and its connections to the current deque.

2. If char is not a key but is in the values:
  - Identify the parent node(s) that have char as a connected node.
  + Append both the parent node(s) and their connected nodes to current.

**Breadth-First Search (BFS) Loop:**
The BFS loop runs while there are elements in the current deque.
For each iteration, the leftmost element (candidate) is popped from current.
If this candidate has already been processed (exists in contacted), the loop continues to the next iteration.
If the candidate has not been processed, it is added to the contacted list.
If this candidate is a key in the candidates dictionary, its connected candidates are appended to current.

**Execution:**
The user is prompted to input a character.
The function contacted_candidates(ins) is called with this input.
Finally, the list of contacted candidates is printed.

**Example Execution:**
Consider the input A:

A is found in the candidates dictionary, so A and its connections **['B', 'C', 'J']** are appended to current.
The BFS loop starts:
A is processed, added to contacted, and its connections are appended to current.
B and C are processed next (individually), added to contacted but have no further connections.
J is processed, added to contacted, and its connection ['V'] is appended to current.
V is processed, added to contacted, and its connections ['W', 'X', 'Y', 'Z'] are appended to current.
W, X, Y, and Z are processed individually and added to contacted.
The final contacted list would be: ['A', 'B', 'C', 'J', 'V', 'W', 'X', 'Y', 'Z'].

**Example with input from the problem statement:**
- **Input:** 'M'
+ **output:** ['L', 'M', 'N', 'A', 'K', 'B', 'C', 'J', 'V', 'W', 'X', 'Y', 'Z']

**Testing of Code:**
- Testing is automated using **unittest** python library.
+ Some test cases are already mentioned with their expected outputs.
+ For manual testing of code insert the **"class TestContactedCandidates(unittest.TestCase):"** in docstrings and remove the manual testing code snippet from docstrings.
