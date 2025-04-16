import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker", page_icon="🔒",)

st.title("🔒Password Strength Checker")
st.markdown("""
## Welcome to the ultimate password strength checker!
use this simple tool to the check the strength of your password and get suggestions on how to make it stronger.
        we will give you helpful tips to create a  Strong Password 🔒""")

password = st.text_input("Enter your password", type="password")

feedback = []

score = 0

if password : 
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌Password should conatain both upper and lower case characters.") 

    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("❌Password should conatin at least one digit.")   

    if re.search(r'[!@#$%&*]' , password):
        score += 1
    else:
         feedback.append("❌Password should conatin at least one speical characters(!@#$%&*).")   

    if score == 4:
        feedback.append("✅Your password is Strong!")
    elif score == 3:
        feedback.append("Your password is medium strength. It could be stronger.")
    else:
        feedback.append("Your password is weak.Please make it stronger.")

    if feedback:
        st.markdown("## Improvement Suggestions")
        for tip in feedback:
            st.write(tip)
    else:
        st.info("Please Enter your password to get started. ")