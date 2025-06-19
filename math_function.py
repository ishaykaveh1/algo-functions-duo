"""
ספרייה של פונקציות אלגוריתמיות
"""
def welcome():
    print("wolcome to my algorithems functions")
def isprime(num,i=2):
    if num == i:
        return True
    elif num%i==0:
        return False
    return isprime(num,i+1)
def factorial(num):
    """calculate num factorial"""
    if num ==1:
        return num
    return num * factorial(num-1)

if __name__=="__main__":
    welcome()
    isprime(5)
    factorial(7)
    כככמלמלמ