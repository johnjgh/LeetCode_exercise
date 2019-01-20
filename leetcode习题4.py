def midlenum(num1,num2):
    num = num1 + num2
    num.sort()
    if len(num) % 2:
        mid = float(num[(len(num)-1)//2])
        return mid
    else:
        mid = float((num[len(num)//2] + num[len(num)//2-1])/2)
        output = '(%d + %d)/2 = %.1f' % (num[len(num)//2-1],num[len(num)//2],mid)
        return output
num1 = [1,2]
num2 = [3,4]
print('中位数是%s' % midlenum(num1,num2))
