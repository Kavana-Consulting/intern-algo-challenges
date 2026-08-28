"""
LeetCode - Longest Substring Without Repeating Characters

Time complexity is O(n) because I used a hash map so only a single pass through the string

Space complexity is O(n) worst case with the worst case scenario being we store every character and their indices in seen before finding the correct match

Brute force would have looked like nested loops circling through every character in order to find the longest substring of unique characters. This would lead to redundant work since it scans every element even if it's already been ruled out. Using the sliding window is the optimized approach because it uses two pointers and stores in the dictionary seen the most recent index of each character. The brute-force approach takes O(n²), while the sliding window simplifies this to O(n). 
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = {}
        left = 0
        longest = 0

        for i, letter in enumerate(s):
            if letter in seen and seen[letter] >= left:
                left = seen[letter] + 1
            
            seen[letter] = i
            longest = max(longest, i - left + 1)

        return (longest)



if __name__ == "__main__":
	sol = Solution()

	assert sol.lengthOfLongestSubstring("abcabcbb") == 3

	assert sol.lengthOfLongestSubstring("bbbbbbb") == 1

	assert sol.lengthOfLongestSubstring("pwwkew") == 3

	print ("Passed")