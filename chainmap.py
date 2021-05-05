from collections import ChainMap
import argparse

def argument_parser(parser):
    parser.add_argument('-n','--name')
    parser.add_argument('-ln','--lastName')
    parser.add_argument('-a','--age')
    parser.add_argument('-s','--salary')
    args=parser.parse_args()
    #convevrting the argument Parser object into dictionary
    
    args_dict= {k:v for k,v in vars(args).items() if v}
    return args_dict

def sample_example(new_employee):
    
    #existing employee information
    employee1= {'name':'mridul','lastName':'pant','age':23,'salary':'19000'}
    employee2= {'name':'shubham','lastName':'bhatt','age':25,'salary':'34000'}
    employee3= {'name':'ashish','lastName':'goswami','age':27,'salary':'29000'}
    
    print(new_employee)
    #adding new employee informations
    chainObject= ChainMap(new_employee,employee1,employee2,employee3)
    print(chainObject.get('name'))
    
    #chaining arrangement also follows an important criteria
    chainObject2= ChainMap(employee2,employee3,employee1)
    print(chainObject2.get('name'))
    
    
    

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='enter the employee details')
    args_dict= argument_parser(parser)


    sample_example(args_dict)