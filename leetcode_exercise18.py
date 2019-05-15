class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res =[]
        for i in range(len(nums)-3):
            if i > 0 and nums[i-1]==nums[i]:
                continue
            for j in range(i+1,len(nums)-2):
                if j > i+1 and nums[j-1]==nums[j]:
                    continue
                l = j+1
                r = len(nums)-1
                while l < r:
                    s = nums[i] + nums[j] + nums[l] +nums[r]
                    if s==target:
                        res.append([nums[i],nums[j],nums[l],nums[r]])
                        l +=1
                        r -=1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        while r > l and nums[r] == nums[r+1]:
                            r -= 1
                    elif s>target:
                        r -=1
                    else :
                        l +=1
        return res

if __name__ == '__main__':
    sumer = Solution()
    nums = [-3, -1, 0, 2, 4, 5]
    target = 1
    print(sumer.fourSum(nums,target))