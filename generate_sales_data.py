from faker import Faker
import random
import pandas as pd

# Initialize Faker generator
fake = Faker()

# Generate synthetic sales data
def generate_sales_data(num_records):
    data = []
    for _ in range(num_records):
        date = fake.date_between(start_date='-1y', end_date='today')
        product = random.choice(['A', 'B', 'C'])
        quantity = random.randint(50, 200)
        unit_price = round(random.uniform(10, 50), 2)
        revenue = round(quantity * unit_price, 2)
        data.append([date, product, quantity, unit_price, revenue])
    return data

# Generate 1000 records of sales data
sales_data = generate_sales_data(1000)

# Convert data to DataFrame
df = pd.DataFrame(sales_data, columns=['Date', 'Product', 'Quantity', 'Unit Price', 'Revenue'])

# Save DataFrame to CSV
df.to_csv('big_sales_data.csv', index=False)
