# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def pancakeFlip(arr, right):
            left = 0
            while(left < right):
                arr[left], arr[right] = arr[right], arr[left]
                left+=1
                right-=1



        n = len(arr)
        unsorted = n-1
        ans = []
        while(unsorted):
            index = arr.index(max(arr[:unsorted+1]))
            pancakeFlip(arr, index)
            ans.append(index+1)
            ans.append(unsorted+1)
            pancakeFlip(arr, unsorted)
            unsorted-=1
        return ans

        