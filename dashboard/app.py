import streamlit as st
import pandas as pd

customers_df = pd.read_csv('../data/customers_dataset.csv')
geolocation_df = pd.read_csv('../data/geolocation_dataset.csv')

customers_geo = pd.merge(customers_df, geolocation_df,
                         left_on='customer_zip_code_prefix',
                         right_on='geolocation_zip_code_prefix',
                         how='left')

st.title("Customer Distribution Dashboard")

st.sidebar.header("Filter Data")

city_options = customers_geo['geolocation_city'].unique()
city_selection = st.sidebar.selectbox("Pilih Kota", options=city_options)

zip_options = customers_geo['customer_zip_code_prefix'].unique()
zip_selection = st.sidebar.multiselect("Pilih Kode Pos", options=zip_options)

filtered_data = customers_geo

if city_selection:
    filtered_data = filtered_data[filtered_data['geolocation_city'] == city_selection]

if zip_selection:
    filtered_data = filtered_data[filtered_data['customer_zip_code_prefix'].isin(zip_selection)]

st.header(f"Distribusi Pelanggan di {city_selection}")

st.subheader("Distribusi Pelanggan Berdasarkan Kode Pos")
top_zip_codes = filtered_data['customer_zip_code_prefix'].value_counts().head(10)
st.bar_chart(top_zip_codes)

st.subheader("Distribusi Pelanggan Berdasarkan Kota")
top_cities = filtered_data['geolocation_city'].value_counts().head(10)
st.bar_chart(top_cities)

st.write("Detail Data Pelanggan :")
st.dataframe(filtered_data)
