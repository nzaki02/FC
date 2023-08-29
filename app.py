import streamlit as st

def fahrenheit_to_celsius(fahrenheit):
    return round((fahrenheit - 32) / 1.8, 2)

def celsius_to_fahrenheit(celsius):
    return round((celsius * 1.8) + 32, 2)

def fahrenheit_to_kelvin(fahrenheit):
    return round((fahrenheit - 32) * 5/9 + 273.15, 2)

# Streamlit UI
st.title('Temperature Converter')

conversion_type = st.selectbox(
    'Choose conversion type:',
    ['Fahrenheit to Celsius', 'Celsius to Fahrenheit', 'Fahrenheit to Kelvin']
)

temperature = st.number_input('Enter temperature:', value=0.0)

if st.button('Convert'):
    if conversion_type == 'Fahrenheit to Celsius':
        converted_temp = fahrenheit_to_celsius(temperature)
        st.write(f'The temperature in Celsius is: {converted_temp:.2f}')
    elif conversion_type == 'Celsius to Fahrenheit':
        converted_temp = celsius_to_fahrenheit(temperature)
        st.write(f'The temperature in Fahrenheit is: {converted_temp:.2f}')
    elif conversion_type == 'Fahrenheit to Kelvin':
        converted_temp = fahrenheit_to_kelvin(temperature)
        st.write(f'The temperature in Kelvin is: {converted_temp:.2f}')
