class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        t = nums[0]+nums[1]+nums[2]
        for i in range(len(nums)):
            if i == 0 or nums[i] > nums[i-1]:
                l = i + 1
                r = len(nums) - 1
                while r > l:
                    s = nums[i]+nums[l]+nums[r]
                    if s == target:
                        return s
                    elif s > target:
                        r -= 1
                    else:
                        l += 1
                    if abs(t-target) > abs(s-target):
                        t = s
                print(nums, s, t)
        return t

if __name__ == '__main__':
    closet = Solution()
    nums = [1,2,5,10,11]
    target = 12
    print(closet.threeSumClosest(nums, target))
