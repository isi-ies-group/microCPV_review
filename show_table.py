# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 18:01:43 2021

@author: Ruben
"""
import pandas as pd
import streamlit as st
import plotly.express as px

table = pd.read_excel('OverviewTable_v1.3.xlsx', na_values='-')

# table_cpv = table[table['Group'] == 'cpv']

st.title('HIPERION Workshop')
st.header('Micro-concentrator photovoltaics, a review of key technologies')

x_axis = st.sidebar.radio('X axis', table.columns)
y_axis = st.sidebar.radio('Y axis', table.columns)

fig = px.scatter(table, x=x_axis, y=y_axis,
	         size='X (suns)', color='Group',
                 hover_name='Reference')

st.plotly_chart(fig, use_container_width=True)

st.write(table)