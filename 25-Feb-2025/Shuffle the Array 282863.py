# Problem: Shuffle the Array - https://leetcode.com/problems/shuffle-the-array/

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr1 = nums[:n]
        arr2 = nums[n:]
        ans = []
        res = list(zip(arr1, arr2))
        for right, left in res:
            ans.append(right)
            ans.append(left)
        return ans

    


        