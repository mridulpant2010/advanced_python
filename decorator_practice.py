from functools import wraps

def handle_division(func):
    
    @wraps(func) #after adding wraps i am able to see the correct function name and the document for it.
    def wrapper(a,b):
        ''' divide 2 numbers '''
        #handle the base case
        if b==0:
            return '0 is not possible'
        return func(a,b)
    return wrapper

@handle_division
def division(x,y):
    ''' divide 2 numbers '''
    #function to divide 2 numbers
    return x/y

ans= division(3,0)
print(ans)



if __name__ =='__main__':
    print(division.__name__)
    print(division.__doc__)