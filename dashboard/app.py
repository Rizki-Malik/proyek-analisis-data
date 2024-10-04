import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

customers_df = pd.read_csv('./data/customers_dataset.csv')
geolocation_df = pd.read_csv('./data/geolocation_dataset.csv')

customers_geo = pd.merge(customers_df, geolocation_df, left_on='customer_zip_code_prefix', right_on='geolocation_zip_code_prefix', how='left')

st.title("Customer Distribution Dashboard")

st.header("Distribusi Pelanggan Berdasarkan Kode Pos")
top_zip_codes = customers_df['customer_zip_code_prefix'].value_counts().head(10)
st.bar_chart(top_zip_codes)

st.header("Distribusi Pelanggan Berdasarkan Kota")
top_cities = customers_geo['geolocation_city'].value_counts().head(10)
st.bar_chart(top_cities)