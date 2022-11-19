import streamlit as st
import pandas as pd
import sqlalchemy as sa
import pyodbc

st.title('Fundamentals Comparison')

engine = sa.create_engine('mssql+pyodbc://sqluser:password@DevSQLServer')

df = pd.read_sql('Fundamentals', engine, index_col=['symbol'])

print(df)

dropdown1 = st.selectbox('Choose your ticker', df.index.unique())

dropdown2 = st.selectbox('Choose your metric', df.columns.unique())

values = df[df.index == dropdown1][[dropdown2]]

st.bar_chart(values)