import pandas as pd
from sqlalchemy import create_engine

# 1. Load the raw data
df = pd.read_csv('bank_statement.csv')
df['Date'] = pd.to_datetime(df['Date'])

# 2. The Categorization Logic (Rule-based)
def categorize(description):
    description = description.lower()
    if any(x in description for x in ['swiggy', 'zomato', 'grocery']):
        return 'Food'
    elif any(x in description for x in ['uber', 'bus']):
        return 'Transport'
    elif any(x in description for x in ['amazon']):
        return 'Shopping'
    elif any(x in description for x in ['bill', 'netflix']):
        return 'Bills'
    else:
        return 'Other'

df['Category'] = df['Description'].apply(categorize)

# 3. Save to Database
engine = create_engine('sqlite:///finance.db')
df.to_sql('transactions', engine, if_exists='replace', index=False)

print(f"Processed {len(df)} transactions and saved to finance.db")
print(df.head())
