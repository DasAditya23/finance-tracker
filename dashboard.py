import streamlit as st
import pandas as pd
import sqlite3

st.set_page_config(page_title="Finance Tracker", page_icon="💰")
st.title("💰 Personal Finance Tracker")

# Connect to DB
conn = sqlite3.connect('finance.db')
df = pd.read_sql("SELECT * FROM transactions", conn)

# Sidebar filter
st.sidebar.header("Filter")
category_filter = st.sidebar.multiselect("Select Category", df['Category'].unique(), default=df['Category'].unique())
filtered_df = df[df['Category'].isin(category_filter)]

# Show KPIs
col1, col2 = st.columns(2)
col1.metric("Total Spent", f"₹ {filtered_df['Amount'].sum():,.2f}")
col2.metric("Transactions", len(filtered_df))

# Chart
st.subheader("Spending by Category")
category_spend = filtered_df.groupby('Category')['Amount'].sum().reset_index()
st.bar_chart(category_spend.set_index('Category'))

# Raw Data
st.subheader("Raw Transactions")
st.dataframe(filtered_df)
