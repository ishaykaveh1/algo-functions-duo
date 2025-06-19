"""
ספרייה של פונקציות אלגוריתמיות
"""
def welcome():
    print("wolcome to my algorithems functions")
if __name__=="__main__":
    welcome()

user_input=int(input())

def factorial(num):
    """calculate num factorial"""
    if num ==1:
        return num
    return num * factorial(num-1)
print(factorial(user_input))
