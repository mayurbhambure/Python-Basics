
from unittest import result


def addition(x,y):
    '''
    This Funaction take two number as a input and reteun sum of Number  
    '''
    return x+y

def userInput():
    try:
        a = int(input("Enter First Number"))
        b = int(input("Enter Second Number"))
        return a,b
    except Exception:
        print(" Please Enter Number Only")
    

if __name__ == '__main__':
    try:
        a,b = userInput()
        result = addition(a,b)
        if result is not None:
            print("Addtion Of Two Numbers : - ",result)
    except Exception as e:
        print("Something went wrong with User inputs")
    
    