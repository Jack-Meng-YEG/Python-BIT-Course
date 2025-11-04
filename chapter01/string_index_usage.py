# String index / slice usage examples

# s = "120F"

# 1) Single character index (0-based, positive indices from left to right)
# First character
# first_char = s[0]        # "1"
# Second character
# second_char = s[1]       # "2"

# 2) Single character index with negative indices (from right to left)
# Last character
# last_char = s[-1]        # "F"
# Second-to-last character
# second_last_char = s[-2] # "0"

# 3) Basic slice s[start:end]  (includes start, excludes end)
# Characters at index 0 and 1 (not including index 2)
# sub_0_2 = s[0:2]         # "12"
# Characters at index 1 and 2
# sub_1_3 = s[1:3]         # "20"

# 4) Slice from the beginning to a position (omit start)
# From the beginning to the character before the last one
# without_last = s[:-1]    # "120"
# From the beginning to index 2 (not including index 2)
# up_to_2 = s[:2]          # "12"

# 5) Slice from a position to the end (omit end)
# From index 1 to the end
# from_1_to_end = s[1:]    # "20F"
# From index 2 to the end
# from_2_to_end = s[2:]    # "0F"

# 6) Slice with negative indices in start or end
# Last three characters
# last_three = s[-3:]      # "20F"
# From the beginning to the character before the last two
# all_but_last_two = s[:-2]  # "12"

# 7) Copy the whole string
# copy_all = s[:]          # "120F"

# 8) Typical pattern in temperature problems: value + unit
# Unit in the last character
# unit = s[-1]             # "F"
# Numeric part is everything except the last character
# value_str = s[:-1]       # "120"
