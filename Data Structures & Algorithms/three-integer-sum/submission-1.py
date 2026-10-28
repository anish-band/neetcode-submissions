class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        since all are distinct, we can just sort the arr
        then loop through the arr:
            have a left start at i + 1, r start at end
            while l < r:
                if indexes add up to 0 add to res
                too small? left++
                too big? right--
                after match loop forward until dif numbers
        '''

        nums.sort()
        n = len(nums)
        res = []

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] > 0:
                break

            l, r = i + 1, n - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1]:
                        l += 1
                elif sum < 0:
                   l += 1
                else:
                    r -= 1                 
        
        return res
            
        