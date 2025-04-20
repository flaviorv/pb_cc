from random import choices
import string
def longest_common_substring(string1, string2):
    # the time complexity is O(len1xlen2)
    len1, len2 = len(string1), len(string2)
    dp_table = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    longest_length = 0
    substring_end_index = 0

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if string1[i - 1] == string2[j - 1]:  
                dp_table[i][j] = dp_table[i - 1][j - 1] + 1
                if dp_table[i][j] > longest_length:
                    longest_length = dp_table[i][j]
                    substring_end_index = i
            else:
                dp_table[i][j] = 0

    start_index = substring_end_index - longest_length
    return string1[start_index:substring_end_index], longest_length

len1 = 100
len2 = 100
string1 = ''.join(choices(string.ascii_lowercase, k=len1))
string2 = ''.join(choices(string.ascii_lowercase, k=len2))

lcs, len = longest_common_substring(string1, string2)
print(f"\33[34mLongest Common Substring: {lcs}")
print(f"Length: {len}\33[0m")
print(string1.replace(lcs, f"\33[31m{lcs}\33[0m"))
print(string2.replace(lcs, f"\33[31m{lcs}\33[0m"))
