import math

l=50
print('Friendly reminder: Enter 0 to '+ str(l) + ' only. Press q anytime to exit.')
p=input('For PI, How many decimal places would you like?')
c=1

while c:
    try:
        a=int(p)
    except ValueError:
        if p=='q':
            print('You pressed q to exit. Good bye! See you next time~')
            break
        else:
            print('Not a valid number. Enter 0 to ' + str(l) + ' only. Press q anytime to exit.')
            p=input('For PI, How many decimal places would you like?')
            c=1
    else:
        if int(p)>50 or int(p)<0:
            print('Number out of range. Enter 0 to ' + str(l) + ' only. Press q anytime to exit.')
            p=input('For PI, How many decimal places would you like?')
        else:
            b='{:.'+ str(p) +"}"
            print('PI = ' + b.format(math.pi))
            w=input('Very neat..., right? Press y to run it again. Press n or q to exit.')
            if w=='y' or w=='Y':
                c=1
                p=input('For PI, How many decimal places would you like?')
            elif w=='n' or w=='N' or w=='q' or w=='Q':
                c=0
                print('You pressed n or q to exit. Good bye! See you next time~')
            else:
                print('Not a valid entry. Auto-restarted. Enter 0 to ' + str(l) + ' only. Press q anytime to exit.')
                c=1
                p=input('For PI, How many decimal places would you like?')


def compute_pi(n):
    pi = 0.0
    k = 0
    
    while k <= n:
        pi += (1 / 16**k) * (
            (4 / (8 * k + 1)) -
            (2 / (8 * k + 4)) -
            (1 / (8 * k + 5)) -
            (1 / (8 * k + 6))
        )
        k += 1
    
    return pi

print("Calculating π using the Bailey-Borwein-Plouffe formula")
print("Enter the number of decimal places to compute (up to 15):")

while True:
    try:
        decimal_places = int(input("> "))
        if decimal_places < 0 or decimal_places > 15:
            raise ValueError
        break
    except ValueError:
        print("Invalid input. Please enter a number between 0 and 15.")

pi_value = compute_pi(decimal_places)
print("π = {0:.{1}f}".format(pi_value, decimal_places))