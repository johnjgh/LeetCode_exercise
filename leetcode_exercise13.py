class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        t = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i in range(len(s)):
            if i != len(s)-1:
                if s[i]+s[i+1] in ['IV','IX','XL','XC','CD','CM']:
                    result += t.get(s[i+1])-t.get(s[i])
                    continue
            if i != 0:
                if s[i-1]+s[i] in ['IV','IX','XL','XC','CD','CM']:
                    continue
            result += t.get(s[i])
        return result
if __name__ == '__main__':
    inter = Solution()
    roman = 'IX'
    print(inter.romanToInt(roman))