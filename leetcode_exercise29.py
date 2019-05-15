class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        t = 1
        m = 0
        for i in [dividend,divisor]:
            if i < 0:
                m += 1
            if i > 0:
                m -= 1
        a = abs(dividend)
        b = abs(divisor)
        add = b
        if a < b:
            return 0
        def square(a, b, t, add):
            while(b + add <= a):
                c = add
                add += c
                n = t
                t += n
                print(c,n,add,t)
            # square(a, b, n, c)
            return t
        square(a, b, t, add)

if __name__ == '__main__':
    divided = Solution()
    dividend = 10
    divisor = 3
    result = divided.divide(dividend,divisor)
    print(result)