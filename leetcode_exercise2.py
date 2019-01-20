def add(twonums):
    fir = ''
    sec = ''
    t = str(twonums).split('+')
    for i in t[0]:
        if i.isnumeric():
            fir = fir.replace(fir,i + fir)
    for j in t[1]:
        if j.isnumeric():
            sec = sec.replace(sec,j + sec)
    result = list(str(int(fir) + int(sec)))
    result.reverse()
    output = ' -> '.join(result)
    return output
twonums = '(2 -> 4 -> 3) + (5 -> 6 -> 4)'
print(add(twonums))
