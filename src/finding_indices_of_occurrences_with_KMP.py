"""Lab7"""


def find_max_prefix_suffix(needle):
    ps_table = [0] * len(needle)
    j, i = 0, 1

    while i < len(needle):
        if needle[i] == needle[j]:
            ps_table[i] = j + 1
            i, j = i + 1, j + 1

        else:
            if j == 0:
                ps_table[i] = 0
                i += 1
            elif j > 0:
                j = ps_table[j-1]
    return ps_table


def knuth_morris_pratt(needle, haystack):
    lps = find_max_prefix_suffix(needle)
    i, j = 0, 0
    indices_occurrences = set()

    while i < len(haystack):

        if haystack[i] == needle[j]:
            i, j = i + 1, j + 1
            if j == len(needle):
                indices_occurrences.add(i - j)
                j = lps[j-1]

        else:
            if j > 0:
                j = lps[j-1]
            else:
                i += 1
    return indices_occurrences
