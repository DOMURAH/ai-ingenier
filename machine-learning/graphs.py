arrays = [22,15,6,8,9,77,145,788]

class Solution(object):
    def findKthKLargesr(self,nums : list,k):
        copy_nums = nums[:]
        largest = None
        x = 0 
        while x < k:
            
            maximum = max(copy_nums)
            largest = maximum
            copy_nums.remove(maximum)
            x += 1
            
        return largest
s = Solution()
print(s.findKthKLargesr(arrays,5))
print(arrays)