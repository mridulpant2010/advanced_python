#creating a pyspark dataframe from the dataset
'''
a. lists
b. tuples
c. dicitonary
d. using ROW
e. pandas dataframe
f. using rdd 
'''


'''
name,age,subject
list_a=[['mridul',12,'history'],['lata',10,'hindi'],['lata',10,'sanskrit'],['kushagra',9,'biochemistry']]
df=spark.createDataFrame(list_a,['name','age','subject'])
'''

list_a=[['mridul',12,'history'],['lata',10,'hindi'],['lata',10,'sanskrit'],['kushagra',9,'biochemistry']]
df=spark.createDataFrame(list_a,['name','age','subject'])

tuple_a=[('mridul',12,'history'),('lata',10,'hindi'),('lata',10,'sanskrit'),('kushagra',9,'biochemistry')]
df=spark.createDataFrame(tuple_a,['name','age','subject'])

dict_a = [{'name':'mridul','age':12,'subject':'history'},{'name':'lata','age':10,'subject':'hindi'}]
df=spark.createDataFrame(dict_a)

from pyspark.sql import Row
list_row=[
    Row(name='mridul',age=12,subject='history'),
    Row(name='kushagra',age=9,subject='biochemistry')
]
df_a= spark.createDataFrame(list_row)


#creating a sparkContext from the sparkSession(spark)
sc = spark.sparkContext
rdd=sc.parallelize(tuple_a)
df= spark.createDataFrame(rdd,schema=['name','age','subject'])


from pyspark.sql.functions import upper
#in order to avoid throwing an out-of-memory exception , use:
df.take(1)
#to assign a new column 
df.withColumn('upper_name',upper(df.name)).show()
#to convert pyspark dataframe into a pandas df.


#how and when to use the udf?