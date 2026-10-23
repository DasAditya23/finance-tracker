from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker, Session
import pandas as pd

app = FastAPI(title="Finance Tracker API")
engine = create_engine('sqlite:///finance.db', connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/summary")
def get_summary(db: Session = Depends(get_db)):
    """Returns total spending per category."""
    query = "SELECT Category, SUM(Amount) as Total FROM transactions GROUP BY Category ORDER BY Total DESC"
    df = pd.read_sql(query, engine)
    return df.to_dict(orient="records")

@app.get("/transactions")
def get_transactions(db: Session = Depends(get_db)):
    """Returns all raw transactions."""
    df = pd.read_sql("SELECT * FROM transactions", engine)
    return df.to_dict(orient="records")
