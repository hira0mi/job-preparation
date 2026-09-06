class Solution:
    def searchRange_linear(self, nums: List[int], target: int) -> List[int]:
        #задача осложняется тем, что мы имеем повторы, от которых просто так избавиться нельзя
        #Пожалуй, первая идея - найти бинпоиском какой-то таргет, а затем идти 
        #влево и вправо, пока на нащупаем границы(уже линейный поиск?)
        #К сожалению, это будет выполняться за O(n) в худшем случае
        left = 0
        right = len(nums) - 1

        while left<=right:
            mid = (left+right)//2
            if nums[mid] > target:
                right = mid - 1
            if nums[mid] < target:
                left = mid + 1
                #как-то плохо выглядит с этими ифами, надо реализацию получше чекнуть
            if nums[mid] == target:
                left_target, right_target = mid, mid
                while nums[left_target] == target:
                    left_target-=1
                while nums[right_target] == target:
                    right_target+=1
                return [left_target, right_target]
                #нас спалили. Не знал что они могут отдетектить лин поиск. Если что это Restrictions Failed, а не проёб по времени
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        #задача осложняется тем, что мы имеем повторы, от которых просто так избавиться нельзя
        #Пожалуй, первая идея - найти бинпоиском какой-то таргет, а затем идти 
        #влево и вправо, пока на нащупаем границы(уже линейный поиск?)
        #К сожалению, это будет выполняться за O(n)
        left = 0
        right = len(nums) - 1

        while left<=right:
            mid = (left+right)//2
            if nums[mid] > target:
                right = mid - 1
            if nums[mid] < target:
                left = mid + 1
                #Нас спалили. А значит, будем искать левые и правые границы бинпоиском
            if nums[mid] == target:
                search_left, search_right = 0, mid
                while search_left<=search_right:
                    mid_target = (search_left + search_right) // 2
                    if nums[mid_target] == target:
                        search_right = mid_target 
                    if nums[mid_target] < target:
                        search_left = mid_target + 1
                    if nums[mid_target] > target:
                        search_right = mid_target - 1
                if search_left>=len(nums):
                    return [-1, -1]
                if nums[search_left] != target:
                    return [-1, -1]
                search_left, search_right = mid, len(nums) - 1
                while search_left<=search_right:
                    mid_target = (search_left + search_right) // 2
                    if nums[mid_target] == target:
                        search_left = mid_target
                    if nums[mid_target] < target:
                        search_left = mid_target + 1
                    if nums[mid_target] > target:
                        search_right = mid_target - 1

        return [-1, -1]




                