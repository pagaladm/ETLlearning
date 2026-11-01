import pandas as pd

#reading the csv file
df = pd.read_csv('orders.csv')

#finding out the exact duplicate rows in the dataset
exact_duplicate_rows=df[df.duplicated()]

print("Duplicate rows: ",len(exact_duplicate_rows))

#save duplicates in different file instead of losing them
exact_duplicate_rows.to_csv('duplicate_rows.csv',index=False)

#removing duplicate rows
df = df.drop_duplicates()

#more real life problem is that most of the rows are not always exactly the same. so for that we need to find the duplicate rows based on primary keys maybe

#conflicting id's 
duplicate_ids = df[df.duplicated(subset=['order_id'],keep = False)]
duplicate_ids.to_csv('conflicting_ids.csv',index=False)
df=df[~df.duplicated(subset=['order_id'],keep=False)] #keep unique rows only


#making sure that the order_dates are treated as a date
df['order_date']=pd.to_datetime(df['order_date'],errors='coerce')

#in amount column removing missing values and negative values
bad_rows = df[df['amount'].isna() | df['amount']<0 | df['order_date'].isna()]

good_rows=df[~bad_rows]
good_rows.to_csv('good_rows.csv',index=False)
bad_rows.to_csv('bad_rows.csv',index=False)

print('Good Rows: ',len(good_rows))
print('Rejected Rows: ',len(bad_rows))
