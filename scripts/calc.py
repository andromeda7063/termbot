# inline calculator
# should take 5+33-2*4 and return 30
# do again after DSA

def calc(a):

    opers = ['+', '-', '*', '/', '**']
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    flag = True

    if any(i not in opers and i not in digits for i in a):
        flag = False

    if flag:
        return eval(a)

a = input()
print(calc(a))