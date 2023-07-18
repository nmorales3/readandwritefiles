import csv

customers= open('customers.csv','r')

customer_file=csv.reader(customers)

outfile = open('customer_country.csv','w')

outfile.write('Full Name,Country\n')

next(customer_file)

counter=0

for rec in customer_file:
    
    outfile.write(rec[1] + ',' + rec[2] + ','+rec[4] '\n')
    counter +=1

outfile.close()

print(f'Total Number of customers: {counter}')