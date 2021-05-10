#how can i by default make my visual code always indented with the
#correct formatting .. suppose all the code should have the comment and signature by default
#write a code to input username and password from the user
from collections import namedtuple
import argparse


def arg_parse(parser): 
    
    parser.add_argument('-n','--name',help='name of the employee',required=True,type=str)
    parser.add_argument('-a','--age',type=int)
    
    args=parser.parse_args()
    dict_args={k:v for k,v in vars(args).items() if v}
    return dict_args
    


if __name__ == '__main__':
    parser=argparse.ArgumentParser(description="input name and age")
    dict_args=arg_parse(parser)
    emp=namedtuple('Employee',dict_args.keys())
    input_argument=emp(**dict_args)
    print(input_argument)