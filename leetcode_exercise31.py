class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = nums
        r = []
        o = -1
        while True:
            t = n[o]
            n.reverse()
            for i in range(len(n)):
                if t > n[i]:
                    r.append(n[i])
                    n[i] = t
                    r += n[:i]
                    f = n[i:]
                    r.sort()
                    f.reverse()
                    return f+r
            o--


if __name__ == '__main__':
    next = Solution()
    nums = [1,2,3,4,5,6,7,8,9]
    result = next.nextPermutation(nums)
    print(result)