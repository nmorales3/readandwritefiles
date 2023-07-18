import csv

sales= open('sales.csv','r')

sales_file=csv.reader(sales)

outfile = open('salesreport.csv','w')

outfile.write('Customer,Total\n')

next(sales_file)
counter = 249


for rec in sales_file:
    rec[3]=float(rec[3])
    rec[4]=float(rec[4])
    rec[5]=float(rec[5])
    total= rec[3]+rec[4]+rec[5]
    total=str(total)
    print(total)

    outfile.write(rec[0]+','+total+'\n')
    counter +=1
outfile.close()