# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        g = [-1]* len(nums2)
        stack = []
        res = [0]*len(nums1)
        for i in range(len(nums2)):
            while stack and nums2[stack[-1]] < nums2[i]:
                g[stack.pop()] = i
            stack.append(i)
        i = 0
        print(g)
        for num in nums1:
            if g[nums2.index(num)] != -1:
                res[i] =  nums2[g[nums2.index(num)]]
            else:
                res[i] = -1
            i+=1
        return res

        