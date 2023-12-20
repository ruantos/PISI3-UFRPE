import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Load Parquet file
file_path = 'C:\\Users\\eu7eu\\Desktop\\Projetos\\parquet'
df = pd.read_parquet(file_path)

# Filter out rows with score equal to 0
new_df = df[df['score'] != 0]

column_name = 'score'

# Main content
st.title("Analise de notas")

# KDE plot using Plotly Express
fig = px.histogram(new_df, x=column_name, marginal="kde", nbins=30, title=f"KDE Plot dos {column_name}s")
st.plotly_chart(fig)

# Additional information or analysis (optional)
st.write("Additional Information:")
st.write(f"Mean {column_name}: {new_df[column_name].mean()}")
st.write(f"Median {column_name}: {new_df[column_name].median()}")