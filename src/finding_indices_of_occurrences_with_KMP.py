"""Lab7"""


def find_max_prefix_suffix(needle):
    prefix_suffix_table = [0] * len(needle)
    j, i = 0, 1

    while i < len(needle):
        if needle[i] == needle[j]:
            prefix_suffix_table[i] = j + 1
            i, j = i + 1, j + 1

        else:
            if j == 0:
                prefix_suffix_table[i] = 0
                i += 1
            elif j > 0:
                j = prefix_suffix_table[j-1]
    return prefix_suffix_table


def knuth_morris_pratt(needle, haystack):
    prefix_suffix_table = find_max_prefix_suffix(needle)
    i, j = 0, 0
    indices_occurrences = set()

    while i < len(haystack):
        if haystack[i] == needle[j]:
            i, j = i + 1, j + 1
            if j == len(needle):
                indices_occurrences.add(i - j)
                j = prefix_suffix_table[j-1]

        else:
            if j > 0:
                j = prefix_suffix_table[j-1]
            else:
                i += 1
    return indices_occurrences
