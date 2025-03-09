# Problem: Sum of Subarray Minimums - https://leetcode.com/problems/sum-of-subarray-minimums/

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        
        # Previous Smaller Element (PSE)
        prev = [-1] * n
        # Next Smaller Element (NSE)
        next_ = [n] * n
        
        # Monotonic stack for previous smaller element
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                prev[i] = stack[-1]
            stack.append(i)
        
        # Monotonic stack for next smaller element
        stack = []
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack:
                next_[i] = stack[-1]
            stack.append(i)
        
        # Calculate the result using the contributions of each element
        result = 0
        for i in range(n):
            # The number of subarrays where arr[i] is the minimum is (i - prev[i]) * (next_[i] - i)
            result += arr[i] * (i - prev[i]) * (next_[i] - i)
            result %= MOD
        
        return result
