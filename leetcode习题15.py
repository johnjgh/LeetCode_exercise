class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        lists = []
        for i in range(len(nums)-2):
            a = 1
            while(i+a<len(nums)-1):
                b = 1
                while(i+a+b<len(nums)):
                    if not nums[i]+nums[i+a]+nums[i+a+b]:
                        n = [nums[i],nums[i+a],nums[i+a+b]]
                        if set(n) not in [set(x) for x in lists]:
                            lists.append(n)
                    b += 1
                a += 1
        return lists

if __name__ == '__main__':
    sumer = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    print(sumer.threeSum(nums))