class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        length = len(s)
        lines = []
        result = ''
        for n in range(numRows):
            lines.append('')
        if numRows == 1:
            return s
        grouplen = numRows + (numRows-2)
        if length%grouplen:
            groupnum = length//grouplen + 1
        else:
            groupnum = length//grouplen
        for j in range(groupnum):
            m = 2
            group = s[j*grouplen:(j+1)*grouplen]
            for i in range(len(group)):
                if i < numRows:
                    lines[i] += group[i]
                else:
                    lines[i-m] += group[i]
                    m += 2

        for t in lines:
            result += t
        return result

if __name__ == '__main__':
    s = input('Please input your string you want to conver: ')
    numRows = int(input('Please input lines number: '))
    N_change = Solution()
    print(N_change.convert(s, numRows))