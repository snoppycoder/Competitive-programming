# Problem: Selection Sort - https://practice.geeksforgeeks.org/problems/selection-sort/1

class Solution: 
    def selectionSort(self, arr):
        #code here
        for i in range(len(arr)-1):
            index = i
            for j in range(i+1, len(arr)):
                if(arr[j] < arr[index]):
                    index = j
            arr[i], arr[index] = arr[index], arr[i]
        return arr
                