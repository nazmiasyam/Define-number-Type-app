import streamlit as st

st.header('Define number Type app:smiley::sunglasses:',divider='rainbow')
st.write('INI ADALAH APLIKASI UNTUK MENENTUKAN BILANGAN GENAP ATAU GANJIL')

number1 = st.number_input('Masukkan angka pertama')
number2 = st.number_input('Masukkan angka kedua')
# Determine if number1 is even or odd
if number1 % 2 == 0:
    number1_type = 'genap'
else:
    number1_type = 'ganjil'

# Determine if number2 is even or odd
if number2 % 2 == 0:
    number2_type = 'genap'
else:
    number2_type = 'ganjil'
# Calculate the product
product = number1 * number2

st.write(f'Angka {number1} adalah bilangan {number1_type}.')
st.write(f'Angka {number2} adalah bilangan {number2_type}.')
st.write(f'Hasil perkalian {number1} dan {number2} adalah {product}.')