'''
functools contains the higher order functions in python.
higher-order-function: that can act on or return other functions. following are the one:
1- lru_cache
2- partials
3- singledispatch 
4- wraps
'''

import timeit
from functools import partial
from functools import lru_cache
from contextlib import contextmanager
from psycopg2 import connect

#how can i use an lru_cache?
import requests 
#setting up a connection using requests module , setting up a contextmanager with it, how it can be done?
#2- 

@lru_cache
@contextmanager
def get_webpage(module):
    webpage="https://docs.python.org/3/library/{}.html".format(module)
    try:
        req=requests.get(webpage)
        yield req
    #create your context manager 
    finally:
        req.close()

#find out what will be the challenges while using the lru_cache and contextmanager

@lru_cache
@contextmanager
def db_connectivity():
    try:
        con = connect(dbname='postgres',user='postgres',password='mridul')
        yield con.cursor()
    finally:
        con.close()    

#when can we use the lru_cache and when we shouldn't use it .
# when to use, when we can save the contents more often,

#example of using a partial in python:
from functools import partial

def add(x,y):
    return x+y



#do we have funciton overloading in python or not?
from functools import singledispatch
'''
provides partial support for function overloading.
it will transform your regular function into a single dispatch generic function.
'''

#function overloading, suppose one function is given multiple arguments and how it is going to 
#function in that case for each diff argument.
@singledispatch
def add(a,b):
    raise NotImplementedError('unsupported error')

@add.register(int)
def _(a,b):
    print("first argument is of type ",type(a))
    print(a+b)
    
    
@add.register(str)
def _(a,b):
    print("first argument is of type ",type(a))
    print(a+b)
    
    
@add.register(list)
def _(a,b):
    c=[x+y for x,y in zip(a,b)]
    print(c)


#write a sample decorator funciton to





if __name__ == "__main__":
    modules = ['functools', 'collections', 'os', 'sys']
    #before using the cache the time it made.
    start=timeit.timeit()
    for module in modules:
        with get_webpage(module) as gw:
            print(module,gw.status_code)
    end=timeit.timeit()
    print(end-start)
    
    
    start_db_time=timeit.timeit()
    with db_connectivity() as cur:
        cur.execute('select version();')
        print(cur.fetchone())
    end_db_time=timeit.timeit()
    print(end_db_time-start_db_time)
    
    
    #example of the partial module 
    ans=partial(add,2,3) #we are defaulting the x parameter
    print(ans())
    
    #think of an example where we can use the partial module 
    
    
    #example for working with the singledispatch module
    
    ans= add(2,3)
    ans2= add([3,6,4],[1,2,3])
    ans3= add('python','programming')
    ans4= add('3'+3) #it will give an error, how to handle it?
    print(ans,ans2,ans3)
    