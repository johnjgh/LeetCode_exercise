class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        d = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        n = []
        if digits == '':
            return n
        for m in d.get(digits[0]):
            n.append(m)
        for i in digits[1:]:
            t = []
            for j in n:
                for k in d.get(i):
                    t.append(j+k)
            n = t
        return n
if __name__ == '__main__':
    combine = Solution()
    digits = '239985'
    print(combine.letterCombinations(digits))