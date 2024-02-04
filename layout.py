import streamlit as st 

st.set_page_config("Registration", layout='centered',page_icon = ":clipboard:")

st.title("Registration Form")



col1 , col2 = st.columns(2)

col1.text_input("First Name",value = "Abhi")

col2.text_input("Second Name")

col3 , col4 = st.columns([3,1])

col3.text_input("Email ID")

col4.text_input("Mob number")

col5 ,col6 ,col7  = st.columns(3)

col5.text_input("Username")

a =col6.text_input("Password", type = "password")

col7.text_input("Repeat Password" , type = "password")

tab1 , tab2 = st.tabs(["Address" , "Pin"])

tab1.text_input("Address")

tab2.text_input("Pin")

but1,but2,but3 = st.columns([1,4,1])

agree  = but1.checkbox("I Agree")

if but3.button("Submit"):
    if agree:  
        st.success("Done")
    else:
        st.warning("Please Check the T&C box")


# form = st.form("Basic form")
# name = form.text_input("Name")
# age = form.slider("Age" , min_value = 18 , max_value = 100 , step = 1)
# date = form.date_input("Birthday")
# submitted = form.form_submit_button("Submit")

# if submitted:
#     st.write(name , age , date)

