class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        p=''
        if not strs:
            return p
        lengths = [len(x) for x in strs]
        for j in range(min(lengths)):
            for i in range(len(strs)-1):
                if strs[i][j] != strs[i+1][j]:
                    return p
            p = strs[0][:j + 1]
        return p
if __name__ == '__main__':
    longestpre = Solution()
    strs = ['a']
    print(longestpre.longestCommonPrefix(strs))