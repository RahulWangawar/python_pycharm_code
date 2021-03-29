# This is a faulty calculator program for a Exercise given by Harry from Code with Harry Youtube Channel
# Coder - Rahul Wangawar :)
# 45 * 3 = 555, 56+9=77, 56/6=4 faulty calculate have to calculate this else right calculation
i = 0
while i<10:
    print("------------------------------------------------------------------------------")
    print("Enter number=")
    n1=int(input())
    print("Enter number=")
    n2=int(input())
    print('What you want to perform?' + '+,-,*,/,**')
    sign = input()

    if n1==56 and n2==9 and sign=='+':
        print(f'Result for"[{n1}{sign}{n2}]" = 77')
    elif n1==45 and n2==3 and sign=='*':
        print(f'Result for"[{n1}{sign}{n2}]" = 555')
    elif n1==56 and n2==6 and sign=='/':
        print(f'Result for"[{n1}{sign}{n2}]" = 4')
    elif sign=='+':
        plus=n1+n2
        print(f'Result for"[{n1}{sign}{n2}]" = ',plus)
    elif sign=='-':
        sub=n1-n2
        print(f'Result for"[{n1}{sign}{n2}]" = ',sub)
    elif sign=='*':
        mul=n1*n2
        print(f'Result for"[{n1}{sign}{n2}]" = ',mul)
    elif sign=='/':
        div=n1/n2
        print(f'Result for"[{n1}{sign}{n2}]" = ',div)
    else:
        print("Error,please check your input")
i += 1


