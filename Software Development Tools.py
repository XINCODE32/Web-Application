#Importing packages
import streamlit as st
import pandas as pd
import plotly.express as px
#Reading the dataset and creating the 'Data Viewer' table
df = pd.read_csv('vehicles_us.csv')
    
st.header('Data viewer')
st.dataframe(df)
#Checkbox to remove or add 'Type'
checkbox = st.checkbox('Type', value=True)
if checkbox:
    type = 'type'
else:
    type = None
#Creating bar chart:'condition' is dimension, 'price' is measurment and 'type' is color
st.header('Compare price distribution between condition and type')
fig_1 = px.histogram(df, x= 'condition', y= 'price', color= type)
st.write(fig_1)
#Sorting dataset
df_sorted = df.sort_values(by=['price','model_year'])
df_loc = df_sorted[25000:26500]
#Creating the header
st.header('Compare price distribution between model year and odometer')
#Creating scatter plot chart
fig_2 = px.scatter(df_loc, x='model_year', y= 'price', color= 'odometer', marginal_x= "box", marginal_y= "violin")
st.write(fig_2)
