class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        n = []
        num = 0
        y = x
        if x < 0:
            return False
        if x == 0:
            return True
        while(y):
            n.append(y%10)
            y //= 10
        n.reverse()
        for i in range(len(n)):
            num += n[i]*pow(10,i)
        if num == x:
            return True
        else:
            return False
if __name__ == '__main__':
    palind = Solution()
    x = 12345654321
    print(palind.isPalindrome(x))