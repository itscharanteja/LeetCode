from collections import defaultdict


def group_anagrams(strs):
    groups = defaultdict(list)
    for words in strs:
        keys = tuple(sorted(words))
        groups[keys].append(words)
    return groups.values()


print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
