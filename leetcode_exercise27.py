class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = nums
        while True:
            try:
                n.remove(val)
            except:
                break
        for i in range(len(n)):
            nums[i] = n[i]
        return len(n)

if __name__ == '__main__':
    remove = Solution()
    nums = [3,2,2,3]
    element = remove.removeElement(nums)
    print(element)