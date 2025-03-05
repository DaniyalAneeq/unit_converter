import streamlit as st

st.title('🧮 Unit Converter')
st.markdown("### Converts Length, Weight, Temperature and Time units")
st.write("Welcome to the Unit Converter! Select the type of conversion you'd like to perform")

category = st.selectbox("Select a category", ["Length", "Weight", "Time", "Temperature"])

def converts_units(category, value, unit):
    if category == "Length":
        if unit == "kilometers to miles":
            return value * 0.621371
        elif unit == "miles to kilometers":
            return value / 0.621371
        elif unit == "kilometers to meters":
            return value * 1000
        elif unit == "meters to kilometers":
            return value / 1000
    elif category == "Temperature":
        if unit == "celsius to kelvin":
            return value + 273
        elif unit == "kelvin to celsius":
            return value - 273
        elif unit == "celcius to fahrenheit":
            return value * 1.8 + 32
        elif unit == "fahrenheit to celsius":
            return value - 17.78          
    elif category == "Weight":
        if unit == "kilograms to pounds":
            return value * 2.20462
        elif unit == "pounds to kilograms":
            return value / 2.20462
        elif unit == "kilograms to grams":
            return value * 1000
        elif unit == "grams to kilograms":
            return value / 1000
    elif category == "Time":
        if unit == "seconds to minutes":
            return value / 60
        elif unit == "minutes to seconds":
            return value * 60
        elif unit == "minutes to hours":
            return value / 60
        elif unit == "hours to minutes":
            return value * 60
        elif unit == "hours to days":
            return value / 24
        elif unit == "days to hours":
            return value * 24
    return 0
    
if category == "Length":
    unit = st.selectbox("Select a unit", ["miles to kilometers", "kilometers to miles", "kilometers to meters", "meters to kilometers"])
elif category == "Temperature":
    unit = st.selectbox("Select a unit", ["celsius to kelvin", "kelvin to celsius", "celcius to fahrenheit", "fahrenheit to celsius"])
elif category == "Weight":
    unit = st.selectbox("Select a unit", ["kilograms to pounds", "pounds to kilograms", "kilograms to grams", "grams to kilograms"])
elif category == "Time":
    unit = st.selectbox("Select a unit", ["seconds to minutes", "minutes to seconds", "minutes to hours", "hours to minutes", "hours to days", "days to hours"])
    
value = st.number_input(f"Enter the value to convert")
if st.button("Convert"):
    result = converts_units(category, value, unit)
    st.success(f"The result is {round(result, 2)}")
    
        
