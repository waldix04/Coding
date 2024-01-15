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