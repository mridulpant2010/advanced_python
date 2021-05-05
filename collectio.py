import collections
'''
python collections module has specialised container datatypes that can be used to replace Python's general 
purpose containers(dict,tuple,list and set).
1- chainmap
2- defaultdict
3- deque
4- namedtuple
5- orderedDict
6- abc or the abstract base classes
'''


#chainmap: --> converts the mapping or dictionaries into a single view
'''
1- link multiple mappings together such that they end up being a single unit.
2- it accepts **maps* which means that a ChainMap will accept any number of mappings or dictionaries and turn them into a single view that you can update.
'''

from collections import ChainMap

car_parts = {'hood': 500, 'engine': 5000, 'front_door': 750}
car_options = {'A/C': 1000, 'Turbo': 2500, 'rollbar': 300}
car_accessories = {'cover': 100, 'hood_ornament': 150, 'seat_cover': 99,'hood':550,'rollbar':350}
chainedObject= ChainMap(car_parts,car_options,car_accessories)
'''
the chainedObject  will have multiple same keys but will return the first one with which matches the key.
'''

#to convert a particular object into dictionary,


"""
parser.add_argument('')
parser = argparse.ArgumentParser(
            description='sum the integers at the command line')
        parser.add_argument(
            'integers', metavar='int', nargs='+', type=int,
            help='an integer to be summed')
        parser.add_argument(
            '--log', default=sys.stdout, type=argparse.FileType('w'),
            help='the file where the sum should be written')
        args = parser.parse_args()
        args.log.write('%s' % sum(args.integers))
        args.log.close()
        
"""

#within chainmap sequencing also plays an important role.


#understanding about the defaultdict
from collections import defaultdict
d= defaultdict(list)
my_list = [(1234, 100.23), (345, 10.45), (1234, 75.00),
           (345, 222.66), (678, 300.25), (1234, 35.67)]

for k,v in my_list:
    d[k].append(v)

print(d)


#using lambda too as our default factory
#whatever value you give in lambda becomes default value to any key, thus it won't give any KeyError.
d2= defaultdict(lambda: 0)
d2['sam'] = 'tiger'
d2['manik']='manik'
print(d2)

print(d2['mridul'])


#if you make lambda equals to None as the default factory, it will raise a value-error.
from collections import deque
#understanding the concept of deque
d=deque() 

d.append(1) #rotates t
d.appendleft(3) 
d.rotate() # it causes one item to rotate off the right end and onto the front,

#using deque to efficiently read files and it is an example of the tail 

def get_last(filename,n=5):
    try:
        with open(filename,'r') as fr:
            return deque(fr,n)
    except OSError as o:
        print("error in opening the file {}".format(filename))
        raise
    
from collections import namedtuple
emp_class = namedtuple('Employee', 'FirstName LastName age Salary dept')
em1=emp_class(FirstName='Mridul', LastName='Pant', age=24, Salary=125000, dept='IT')
em2=emp_class(FirstName='Navin', LastName='Pant', age=56, Salary=90000, dept='Education')
print(em1.FirstName, em1.LastName, em1.age, em1.Salary, em1.dept)


#better way when we can convert the python dictionary object into a namedtuple.
#which when is better namedtuple or dictionary and when to use which.

emp_dict= {'FirstName':'Mridul','LastName':'Pant','age':23,'salary':90000}
emp_class2= namedtuple('Employee2',emp_dict.keys())
em3=emp_class2(**emp_dict)
print(em3)

#normal dictionary is an unordered data collection:

#scenario when should we use an ordered dict and the normal dictionary
# suppose, dictionary is d = {'banana': 3, 'apple':4, 'pear': 1, 'orange': 2}
"""
and you want to traverse the dicitonary based on sorted ascending keys, how will you do it.
"""
from collections import OrderedDict
d = {'banana': 3, 'apple':4, 'pear': 1, 'orange': 2}
new_d = OrderedDict(sorted(d.items()))
print (new_d)

#consider using the 2 more functions in OrderedDict e.g: popitem, move_to_end.


import argparse
from collection import namedtuple

def arg_parse(parser): 
    
    parser.add_argument('-n','name')
    parser.add_argument('-a','age')
    
    args=parser.parse_args()
    dict_args={k:v for k,v in vars(args).items() if value}
    return dict_args

def main(): 
    parser=argparse.ArgumentParser(description="input name and age")
    dict_args=arg_parse(parser)
    emp=namedtuple('Employee',dict_args.keys())
    input_argument=emp(**dict_args)