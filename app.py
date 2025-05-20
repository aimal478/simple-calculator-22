# Step 1: Install streamlit and pyngrok
!pip install streamlit pyngrok --quiet

# Step 2: Write the calculator app in a Python file
%%writefile app.py
import streamlit as st

st.title("🧮 Simple Calculator")

# Input fields
num1 = st.number_input("Enter first number", format="%f")
num2 = st.number_input("Enter second number", format="%f")

# Operation selection
operation = st.selectbox("Choose operation", ["Add", "Subtract", "Multiply", "Divide"])

# When user clicks "Calculate"
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Cannot divide by zero"
    
    st.success(f"Result: {result}")

# Step 3: Launch Streamlit using pyngrok tunnel
from pyngrok import ngrok
import subprocess
import time

# Open ngrok tunnel to port 8501
public_url = ngrok.connect(port=8501)
print("Streamlit app is live at:", public_url)

# Run the Streamlit app
process = subprocess.Popen(["streamlit", "run", "app.py"])

# Keep it alive for 10 minutes
time.sleep(60*10)
