import csv

#with open("ford_escort.csv") as file:
    #reader = csv.reader(file, delimiter=',')
    #for row in reader:
        #print(row)

##################################################################

'''import csv
with open("ford_escort.csv", 'r') as file:
    csv_file = csv.DictReader(file, delimiter=)
    for row in csv_file:
        print(row)

##################################################################

with open('people.csv', 'w') as file1:
    fieldnames = ['first_name', 'last_name', 'age']
    writer = csv.DictWriter(file1, fieldnames = fieldnames)

writer.writeheader()
writer.writerow({
    'first_name': 'Joe',
    'last_name': 'Bloggs',
    'age': 40 
})'''

#############################################################

with open('people.csv', mode='w') as file: 
    fieldnames = ['first_name', 'last_name', 'age'] 
    writer = csv.DictWriter(file, fieldnames=fieldnames) 
    writer.writeheader()
    writer.writerow({ 
    'first_name': 'Joe', 
    'last_name': 'Bloggs', 
    'age': 40 
}) 
    writer.writerow({ 
    'first_name': 'Jane', 
    'last_name': 'Smith', 
    'age': 50 
}) 