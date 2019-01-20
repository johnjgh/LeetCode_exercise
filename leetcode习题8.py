class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        #bbb
        y = 0
        str = str.strip()
        if str in ['', '-', '+'] or (len(str)>2 and str[1] in ['-', '+']):
            return 0
        if str[0]=='-':
            str = str[1:]
            y = 1
        if str[0]=='+':
            str = str[1:]
        if str[0].isnumeric():
            for i in range(len(str)):
                if not str[i].isnumeric():
                    result = int(str[:i])
                    break
                if i==len(str)-1:
                    result = int(str)
        else:
            result = 0
        if y:
            result = -result
        if result > pow(2,31)-1:
            result = pow(2,31)-1
        elif result < -pow(2,31):
            result = -pow(2,31)
        return result
if __name__ == '__main__':
    string2int = Solution()
    str = '3.14'
    print(string2int.myAtoi(str))