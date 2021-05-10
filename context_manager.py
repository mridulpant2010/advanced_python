#with statement provides an efficient way to open and close the file operations, wear and tear down automatically.
#we can write our own context managers using the __exit__ and the __enter__ methods .
#so, we don't have to do it explicitly everytime


#contextmanagers are required for opening and closing automatically.
#how can we create contextmanger of our own
from contextlib import contextmanager,redirect_stdout
from psycopg2 import connect
#suppose i can create one for a dbconnection

#reading the basic from educative website and then the official documentation for python

@contextmanager
def open_database(): 
    try:
        con = connect(dbname='postgres',user='postgres',password='mridul')
        yield con.cursor()
    except Exception as e:
        print(e)
    finally:
        con.close()
        

'''
from contextlib import contextmanager,suppress,closing
with closing(open('chainmap.py','r')) as rf:
    print(rf.read())
'''

if __name__ == '__main__':
    
    with open_database() as cur:
        print('PostgreSQL database version:')
        cur.execute('select * from student')
        print(cur.fetchone())
#       print(db_version)

    #can we use redirect_stdout to work as logger.
    with open('counter.py','w') as cur:
        with redirect_stdout(cur):
            print('writing to sedoutput')
            