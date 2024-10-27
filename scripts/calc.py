# inline calculator
# should take 5+33-2*4 and return 30
# do again after DSA

def calc():

    opers = ['+', '-', '*', '/', '**']
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    flag = True

    a = input()

    for i in a:
        if i not in opers and i not in digits:
            flag = False
            break

    if flag:
        print(eval(a))
