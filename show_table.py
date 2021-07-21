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

cols = table.columns.tolist()
cols2 = cols[1:] + cols[0:1]

st.title('HIPERION Workshop')
st.header('Micro-concentrator photovoltaics, a review of key technologies')
latext = r'''
$$X = \frac{\textrm{Lens aperture}}{\textrm{Solar cell area}}\\$$
$$\\ \eta_\textrm{optical} = \frac{Irradiance_\textrm{Receiver}}{Irradiance_\textrm{Lens aperture}}\\$$
$$\\ \eta_\textrm{electrical} = \frac{P_\textrm{MPP}}{Irradiance_\textrm{Lens aperture}}\\$$
$$\\ CAP = \sqrt{X} \sin(\alpha) \\$$
$$CAP - \textrm{Concentration acceptance product} \\$$
$$X - \textrm{Concentration in suns} \\$$
$$\alpha - \textrm{Acceptance angle for 90\% of max. optical efficiency}$$
$$P_\textrm{MPP} - \textrm{Electrical power at maximum power point}$$
'''
st.write(latext)

x_axis = st.sidebar.radio('X axis', table.columns)
y_axis = st.sidebar.radio('Y axis', table[cols2].columns)

fig = px.scatter(table, x=x_axis, y=y_axis,
	         size='X (suns)', color='Group',
                 hover_name='Reference')

st.plotly_chart(fig, use_container_width=True)

st.write(table)