# BINARY-SEARCH
BINARY SEARCH Algorithm with python 

# 🔍 Binary Search in Python

This project contains a simple implementation of the **Binary Search** algorithm using recursion in Python. Binary Search is a fast and efficient algorithm for finding the position of a target value within a **sorted list**, using the **divide and conquer** technique.

---

## 📌 Features

- Pure Python implementation
- Uses recursion
- Easy to read and modify
- Works with any sorted list of comparable elements

---

##  How It Works

1. The list is sorted before searching.
2. The algorithm calculates the midpoint of the current search range.
3. It compares the midpoint value with the target:
   - If equal → returns the index.
   - If target is less → search left half.
   - If target is greater → search right half.
4. Repeats until the element is found or range is empty.

---

##  Code Example

```python
def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1
    if low > high:
        return -1

    midpoint = (high + low) // 2

    if target == l[midpoint]:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low=0, high=midpoint - 1)
    else:
        return binary_search(l, target, low=midpoint + 1, high=len(l) - 1)
