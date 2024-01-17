# extras:
# how can you force the date format?
# how can you ensure the float is 
# formattedcorrectly by German or US strandards?
# use RegEx to check

transactions =[
    {'type':'purchase','amount': 50,'date':'2024-01-14'},
    {'type':'sale','amount': 30.5,'date':'2024-01-15'},

]

transaction_type = transactions[0]['type']
transaction_amount = transactions[0]['amount']
transaction_date = transactions[0]['date']

# using list comprehension:

def list_of(my_key):
    amount_values = [transaction[my_key] for transaction in transactions]
print(list_of('amount'))

#What If you want to make sure the dates and amounts are properly formatted?

def find_all(my_key,my_value):
    values = [transaction for transaction in transactions if
              transaction[my_key] ==my_value]
    return(values)

my_transactions = find_all('date','2024-01-14')
print(my_transactions)
print(len(my_transactions))




import re

def is_valid_date_format(date_string):
    date_pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')
    #this doesnt check for month/day order
    return bool(date_pattern.match(date_string))


my_date = my_transactions[0]['date']
print(my_transactions[0]['date'])
print(type(my_date))
print(is_valid_date_format(my_date))