class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        y = abs(x)
        num = []
        result = 0
        while(y):
            num.append(y%10)
            y = y//10
        num.reverse()
        for i in range(len(num)):
            result += num[i]*pow(10,i)
        if x<0:
            result = -result
        if pow(2,31)-1 > result > -pow(2,31):
            return result
        return 0

if __name__ == '__main__':
    rever = Solution()
    x = 545132356
    print(rever.reverse(x))