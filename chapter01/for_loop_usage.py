"""
For Loop Usage — Iterating over Iterables in Python

This note shows how `for ... in ...` works with common iterables.
An iterable is any object you can loop over, such as: strings, lists,
tuples, sets, dictionaries, ranges, and files.

Examples included:
1) String: iterate character by character
2) List: iterate element by element
3) Tuple: same as list (immutable)
4) Set: iterate elements (order not guaranteed)
5) Dict: iterate keys by default; also iterate values and key–value pairs
6) range(): iterate over a sequence of integers
7) File object: iterate line by line

Tip:
- Use `enumerate(iterable)` when you need both index and value.
- Use `dict.items()` to get (key, value) pairs.
- Use `line.strip()` to remove newline characters when reading files.
"""

# 1) String
for ch in "abc":
    print(ch)

# 2) List
for item in ["apple", "banana", "orange"]:
    print(item)

# 3) Tuple
for num in (10, 20, 30):
    print(num)

# 4) Set (order not guaranteed)
for x in {1, 3, 5}:
    print(x)

# 5) Dict
person = {"name": "Jack", "age": 25}
for k in person:               # keys
    print(k, "->", person[k])
for v in person.values():      # values
    print(v)
for k, v in person.items():    # key–value pairs
    print(k, v)

# 6) range()
for i in range(5):
    print(i)

# 7) File (uncomment to test with an actual file)
# with open("content.txt", "r", encoding="utf-8") as f:
#     for line in f:
#         print(line.strip())

# Bonus: enumerate
for i, ch in enumerate("python"):
    print(i, ch)
