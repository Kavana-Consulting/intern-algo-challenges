"""
LeetCode - Two Sum

Time complexity is O(n) because I used a hash map so only a single pass through the list

Space complexity is also O(n) with the worst case scenario being we store every number in seen before finding the correct match

Brute force would have looked like nested loops circling through every pair in order to find the correct complement. This would lead to redundant work since it scans every element even if it's already been ruled out. Using the hash map is the optimized approach because the algorithm remembers what has been seen and doesn't waste time on unnecessary pairs. The hash map takes a time of O(n^2) (from the brute force method) and simplifies it to a O(n). 
"""
class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i, number in enumerate(nums):
            comp = target - number
            if comp in seen: 
                return [seen[comp], i]
            seen[number] = i
        
        return []


if __name__ == "__main__":
	sol = Solution()

	assert sol.twoSum([1, 8, 3, 11, 17], 9) == [0,1]

	assert sol.twoSum([2, 4, 6, 8], 14) == [2, 3]

	assert sol.twoSum([0, 4, 3, 0], 0) == [0,3]

	print ("Passed")
