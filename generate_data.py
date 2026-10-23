import pandas as pd
import random
from datetime import datetime, timedelta

# Generate 100 random transactions
data = []
start_date = datetime(2026, 1, 1)
categories = ['Food', 'Transport', 'Shopping', 'Bills', 'Entertainment']

for i in range(100):
    date = start_date + timedelta(days=random.randint(0, 90))
    # Random descriptions
    desc = random.choice(['Swiggy', 'Uber', 'Amazon', 'Electricity Bill', 'Netflix', 'Zomato', 'Local Bus', 'Grocery Store'])
    # Random amounts
    amount = round(random.uniform(50.0, 3000.0), 2)
    
    data.append({
        'Date': date.strftime('%Y-%m-%d'),
        'Description': desc,
        'Amount': amount
    })

df = pd.DataFrame(data)
df.to_csv('bank_statement.csv', index=False)
print("Generated bank_statement.csv with 100 messy transactions!")
