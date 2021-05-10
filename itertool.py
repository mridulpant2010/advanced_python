from itertools import count,islice,cycle,repeat
#use of count
for i in count(0,step=2):
    if i>20:
        break
    print(i)
    
#islice submodule is used to stop the elements after a certain range
#islice is used to limit the count(as it is an infinite ) when to stop iterating, stop when we have reached x iterations

for i in islice(count(10),5):
    print(i)
    
    
#use of cycle:
#cycle is used to create an infinite iterator 
a=cycle('mridul')
for _ in islice(count(10),13):
    print(next(a))


iterr=repeat(5,4)
print(next(iterr))
print(next(iterr))
print(next(iterr))
print(next(iterr))


from itertools import chain

a=[1,2,3,4,5]
b=['a', 'b', 'c', 'd', 'e', 'f']
c=chain(a,b)
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

#chain.from_iterable(iterable)
numbers=list(range(5))
cmd=['ls','/some/dir']

ch=chain.from_iterable([numbers,cmd,[3,4,5]])
print(next(ch))
print(next(ch))

#compress(data,selectors)
#useful for filtering first iterable with the another.

from itertools import compress
letters='mrid'
an=compress(letters,[True,False,False,True])
print(list(an))

#dropwhile(predicate,iterable)
#how is it different from the filter clause?
from itertools import dropwhile
a=list(dropwhile(lambda x: x%2,[1,2,3,4,5]))
print(a)



#the combinatoric generator
from itertools import combinations
#combinations(iterable,r)
#
print(list(combinations('mridul',3)))

from itertools import combinations_with_replacement
a=combinations_with_replacement('wxyz',2)
for el in a:
    print(''.join(el))



#cartesian product from a series of input iterables
from itertools import product
arrays =[1,2,3,4,5] 
#[(-1,1), (-3,3), (-5,5)]
ans=product(arrays)
print(list(ans))


arrays=[(-1,1), (-3,3), (-5,5)]
ans=product(*arrays) #* , exploded or applied to the product function in sequence
print(list(ans))


from itertools import permutations
a=permutations('mridul',2)
print(list(a))


