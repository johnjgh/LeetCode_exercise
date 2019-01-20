class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num not in range(1,4000):
            return False
        t = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        n = []
        result = ''
        while(num):
            n.append(num%10)
            num //= 10
        print(n)
        for i in range(len(n)):
            if n[i] == 0:
                continue
            elif n[i] in [1, 5]:
                result = t.get(n[i]*10**i)+result
            elif n[i] in [4, 9]:
                result = t.get(10**i)+t.get((n[i]+1)*10**i)+result
            elif 1<n[i]<4:
                result = t.get(10**i)*n[i]+result
            else:
                result = t.get(5*10**i)+t.get(10**i)*(n[i]-5)+result
        return result

if __name__ == '__main__':
    roman = Solution()
    num = 1994
    print(roman.intToRoman(num))
