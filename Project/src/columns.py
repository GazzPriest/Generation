database_labels = ["customer_name", "customer_address", "customer_phone", "courier_id", "items"]

for row in database_labels:
    database_labels.append((
        Row1['customer_name']
        Row2['customer_address']
        Row3['customer_phone']
        Row4['courier_id']
        Row5['items']
    ))

fields = ("Customer Name or Reference", "Customer Address", "Customer Phone", "Delivery Courier", "Ordered Menu Items")

sql = "UPDATE orders (customer_name, customer_address. customer_phone, courier_id, items) VALUES (%s, %s, %s, %s, %s)"
for columns in fields:
    new_info = input("Enter new information for " + str(columns) + ": ")
    orderlist[user_input][i] = new_info 



    #sql = "INSERT INTO products (product_name, product_price) VALUES (%s, %s)"
    #val = (product_name, product_price)
    #cursor.execute(sql, val)


    q = INSERT INTO TABLE1 (Item_Name, Item_Price, Item_In_Stock, Item_Max, Observation_Date ) 
        values (%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE Item_Price = VALUES(Item_Price), Item_In_Stock = VALUES(Item_In_Stock), Item_Max = VALUES(Item_Max), 
        Observation_Date = VALUES(Observation_Date) 

itemBank = [] 
for row in rows:
    itemBank.append((
        tempRow2['Item_Name'],
        tempRow1['Item_Price'],
        tempRow3['Item_In_Stock'],
        tempRow4['Item_Max'], 
        getTimeExtra
        )) #append data


q = insert ignore into TABLE1 (
        Item_Name, Item_Price, Item_In_Stock, Item_Max, Observation_Date ) 
        values (%s,%s,%s,%s,%s)           
    

try:
    x.executemany(q, itemBank)
    conn.commit()
except:
    conn.rollback()