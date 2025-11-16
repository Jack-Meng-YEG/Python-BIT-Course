"""
String segment combination

Read a string s from standard input. The string contains several parts
separated by hyphens ('-'). Split s using '-' as the delimiter, then
take the first segment and the last segment and join them with a plus
sign ('+'). Print the resulting string.

Example:
input : Alice-Bob-Charis-David-Eric-Flurry
output: Alice+Flurry
"""

# string_segment_combination.py
s = input()
lt = s.split('-')
print("{}+{}".format(lt[0],lt[-1]))