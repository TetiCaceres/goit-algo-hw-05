# Comparison of Substring Search Algorithms

## Implemented Algorithms

In this work, three substring search algorithms were implemented and tested:

- Boyer–Moore
- Knuth–Morris–Pratt (KMP)
- Rabin–Karp

The execution time of each algorithm was measured using the `timeit` module.

---

## Experimental Setup

Two text files were used in the experiment (Article 1 and Article 2).  
For each text, two different cases were tested:
- searching for a substring that exists in the text;
- searching for a substring that does not exist.

Each search operation was executed multiple times to reduce the impact of random timing fluctuations.

---

## Results for Article 1

For the first text, the Boyer–Moore algorithm showed the shortest execution time when searching for an existing substring.  
The KMP algorithm performed consistently but required slightly more time.  
The Rabin–Karp algorithm was slower, mainly due to additional hash calculations.

**Conclusion:**  
For Article 1, Boyer–Moore was the most efficient algorithm.

---

## Results for Article 2

Similar results were obtained for the second text.  
Boyer–Moore again demonstrated the best performance.  
KMP showed stable behavior, while Rabin–Karp remained the slowest among the three algorithms.

**Conclusion:**  
For Article 2, Boyer–Moore was also the fastest algorithm.

---

## Overall Conclusions

Based on the conducted experiments, the following conclusions can be drawn:

- Boyer–Moore is the fastest algorithm for both tested texts.
- KMP provides predictable and stable performance but is generally slower.
- Rabin–Karp has higher overhead and shows lower performance in this experiment.

**Overall**, Boyer–Moore can be considered the most efficient substring search algorithm for the given texts.

---
