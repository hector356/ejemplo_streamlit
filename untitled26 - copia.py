# -*- coding: utf-8 -*-
"""Untitled26.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1yYXJgtruiDPDU_vC77dh93zRLggxsw6n
"""

# ejemplo :
import streamlit as st
import pandas as pd
import matplñotlib.pyplot as plt

# caragr el archivo csv ' database_titanic.cvs' en un dataframe de pandas.
df = pd.read_csv('database_titanic.csv')

# muetra  un titulo y una descripcion en la aplicacion streamlit.
st.write (''''''
# mi primera aplicacion interactiva
## graficos usando la base de datos del titanic
'''''')

# usando la notacion 'with' para crear una barra lateral en la aplicacion streamlit.
with st.sidebar :
    # titulo para la seccion de opciones en la barra lateral.
    st.write('# opciones')

    # crea un contrl deslizante (slider) que permite al usario seleccionar un numero de bins
    # en el rango de 0 a 10, con un valor predeterminado de 2.
    div = st.slider('numero de bins :', 0, 10, 2)

    # muestra el valor actual del slider en la barra lateral.
    st.write('bins=', div)

# desplegamos un histograma con los datos del eje x
fig, ax = plt.subplots(1, 2, figsiza=(10, 3))
ax[0].hist.(df['age'], bins=div)
ax[0].set_xlabel('edad')
ax[0].set_ylabel('frecuencia')
ax[0].set_title('histograma de edad')

# tomando datos para hombres y contando la cantidad
df_male = df[df['sex'] == 'male']
cant_male = len(df_male)

# tomando datos para mujeres y contando la cantidad
df_female = df[df['sex'] == 'female']
cant_female = len(df_female)

ax[1].bar(['masculino', 'femenino'], [cant_male, cant_female], color = 'red')
ax[1].set_xlabel('sexo')
ax[1].set_ylabel('cantidad')
ax[1].set_title('distribucion de hombres y mujeres')


# desplegamos el grafico
st.pyplot(fig)

st.write(''''''
## muestra de datos cargados
'''''')
#graficamos una tabla
st.table(df.head())