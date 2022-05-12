import csv

def createorder():
    products = {}
    file = open("Project\data\products.csv", 'a', newline="")
    writer = csv.writer(file)
    dictvalue = 0
    print(len(products)) #test
    print(dictvalue) #test
    user_input = input("What is the name of the new product?: ")
    product_tuple = (dictvalue, user_input)
    writer.writerow(product_tuple)
    file.close()

createorder()


#file = open("Project\data\products.csv", 'a', newline="")
#tupl = ("bob", 19)
#writer = csv.writer(file)
#writer.writerow(tupl)
#file.close()