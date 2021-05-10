#demonstrate the code for the argparse 
import argparse

def get_args():
    parser=argparse.ArgumentParser(
        description='A simple argument parser',
        epilog='this is where you might'
    )
    
    group = parser.add_mutually_exclusive_group()
    
    #required argument
    group.add_argument('-x','--execute',action='store',required=True,help='help text for option x')

    #optional arguments
    group.add_argument('-y',help='help text for option Y',default=False)
    parser.add_argument('-z',help='help text for option Z',type=int)
    
    print(parser.print_help())

if __name__ == '__main__':
    get_args()