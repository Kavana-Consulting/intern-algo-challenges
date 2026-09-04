"""
LeetCode - Group Anagrams

Let n = number of strings in strs and k = max length of a string

Time complexity is O(n*k log(k)) because each n string is sorted by k characters which costs O(k log(k))

Space complexity is O(n*k) because every input string is stored once in all groups O(n). Then O(k) is for each key of the sorted tuples. 

Brute force approach would compare each string to an example string from every group. Then it would either append to a matching group, or create a new group if no match was presented. This would create a time complexity of O(n^2 k). The optimized approach used here is more efficient because it avoids scanning every group. The time complexity gets better as n grows. 
"""
class Solution(object):
    def groupAnagrams(self, strs):
        seen = {}
        for i in strs:
            key = tuple(sorted(i))
            if key not in seen:
                seen[key] = []
            seen[key].append(i)
        return list(seen.values())


def _normalize(list_of_groups):
    """Sort each group and sort the groups themselves so comparison
    doesn't depend on insertion/output order."""
    return sorted(sorted(group) for group in list_of_groups)


if __name__ == "__main__":
    sol = Solution()

    result = sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    expected = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    assert _normalize(result) == _normalize(expected)

    result = sol.groupAnagrams(["abc", "bca", "cab", "acb"])
    assert _normalize(result) == _normalize([["abc", "bca", "cab", "acb"]])

    result = sol.groupAnagrams(["listen", "silent", "enlist", "google", "gogole", "cat"])
    expected = [["listen", "silent", "enlist"], ["google", "gogole"], ["cat"]]
    assert _normalize(result) == _normalize(expected)

    print("Passed")