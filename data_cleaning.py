import pandas as pd
import matplotlib
from sqlalchemy import create_engine
import sales_project.queries as queries


df=pd.read_csv("Sample_Superstore.csv", encoding="windows-1252")
print(df)
print(df.head())

print(df.info())
print(df.isnull().sum())

print(df.dtypes)
print(type(df['Order Date'][0]))

print(df.describe())## gives mean median min and 25%, 50%, 75%, max

print("---------------------analysing----------------")
total_sales=df['Sales'].sum()
print(total_sales)

print("-----total sum of all the numerical columns----- ")
print(df.sum(numeric_only=True))


# converting datte type --> by default it is string converting to date format
df['Order Date'] = pd.to_datetime(df['Order Date'])
print(df['Order Date'])
print(type(df['Order Date']))


# creating separete columns named year and month so that it will be easy to create dashboard moth wise year wise

df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month

# year wise sales

sales_trend= df.groupby('Year')['Sales'].sum()
print(sales_trend)
print(sales_trend.plot())

# monthly sales

monthly=df.groupby('Month')['Sales'].sum()
print(monthly)

#category wise sales

category_sales=df.groupby('Category')['Sales'].sum()
print(category_sales)

#finding duplicates

print("duplicated rows or columns are",df.duplicated().sum())

# to know all column name sin dataset
print (df.info())

# converting all data to lower case and unserscore real time industry frormat
df.columns = df.columns.str.lower().str.replace(" ", "_")

# convert shipdate to object  type to date type

df['ship_date'] = pd.to_datetime(df['ship_date'])
print(type(df['ship_date']))

# saving cleaned dataset
df.to_csv("cleaned_superstore.csv", index=False)
print("data saved successfully")

#        ---------MYSQL CONNECTION---------

# Connect to MySQL
engine = create_engine(
    "mysql+pymysql://root:Anil%4012345@localhost:3306/sales"
)

# Insert data into MySQL
df.to_sql("superstore", con=engine, if_exists="replace", index=False)

print(" Data inserted successfully!")


print("----performing queries in python---")

engine = create_engine(
    "mysql+pymysql://root:Anil%4012345@localhost:3306/sales"
)

# Run query and convert to dataframe
df_region = pd.read_sql(queries.region_performance, engine)
print(df_region)

df_customers = pd.read_sql(queries.top_customers, engine)
print(df_customers)

#category wise profits and sales

df_category = pd.read_sql(queries.category_sales, engine)
print(df_category)

# yearly wise sale
print("year wise sales")
df_yearly = pd.read_sql(queries.yearly_sales,engine)
print(df_yearly)


print("monthly sales")

df_monthly = pd.read_sql(queries.monthly_sales,engine)
print(df_monthly)

#year wise category wise sales
print("yearwise category wise sales")

yearwise_category=pd.read_sql(queries.category_yearly_performance,engine)
print(yearwise_category)

#total sales
print("total sales")
print("      ")
total_saless=pd.read_sql(queries.total_sales,engine )
print(total_saless)

# names of customers

print("name sof customers")
print("   ")
names=pd.read_sql(queries.names_customers,engine)
print(names)







