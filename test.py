import streamlit as st

# Title
st.title("Greatest Number Calculator")

# Input fields for two numbers
num1 = st.number_input("Enter the first number:")
num2 = st.number_input("Enter the second number:")
num3= st.number_input("Enter the third number")

# Calculate the sum
result=max(num1,num2,num3)

# Display the sum
# st.write(f"The sum of {num1} and {num2} is: {sum_result}")
st.write(f"Greatest number is: {result}")
