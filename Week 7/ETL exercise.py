import pandas as pd
import pymysql
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")
connection = pymysql.connect(
host = host,
user = user,
password = password,
database = database
)
cursor = connection.cursor()

##Extract

data = pd.read_csv("Week 7\sales_data.csv")
data.columns
frame = pd.DataFrame(data)
drop = frame.dropna(how='any',axis=0) 
#print(drop)

##Transform

engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                       .format(user="root",
                               pw="password",
                               db="ETL"))

drop.to_sql('sales_data', con = engine, if_exists='append', chunksize=1000, index=False)

##customer total spend

#INSERT INTO total_spend_stage
#SELECT customer_id, purchase_amount FROM sales_data 
#WHERE purchase_date >= '2020-12-01' 
#AND purchase_date <= '2020-12-05';

#INSERT INTO total_spend
#SELECT customer_id, SUM(purchase_amount) FROM total_spend_stage
#GROUP BY customer_id

##customer average spend

#INSERT INTO total_average_spend
#SELECT customer_id, AVG(purchase_amount) FROM total_spend_stage
#GROUP BY customer_id

##times customer purchased specific item

#INSERT INTO total_count_stage
#SELECT customer_id, product_id FROM sales_data 
#WHERE purchase_date >= '2020-12-01' 
#AND purchase_date <= '2020-12-05';

#INSERT INTO total_count
#SELECT customer_id, product_id, COUNT(product_id) as purchase_count FROM total_count_stage
#GROUP BY customer_id, product_id
