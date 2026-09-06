class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid - 1
            if nums[mid] < target:
                left = mid + 1
        #Решение задачи очень похоже на 704 про бинарный поиск. Но только мы 
        #возвращаем не -1, а индекс, под которым он стоял. Очевидно, что это right+1
        #Потому что по итогам бинарного поиска мы установили, что nums[mid]<target,
        #а mid=(right+left)//2(округляется вниз)
        return right + 1