import re
import time
import streamlit as st

st.set_page_config("Registration", layout='centered', page_icon=":clipboard:")
st.title("Application Form")
st.sidebar.title("Navigation")
st.sidebar.image("data//sidebar.png", use_column_width=True)
side_bar = st.sidebar.radio("Select an option", ["Home", "Fill Form"])

if side_bar == "Home":
    st.image("data//application_form.png", width=800, caption="Welcome to our application form!")

if side_bar == "Fill Form":
    st.header("Please Fill The Application Form")
    tabs = st.tabs((['Instruction', 'Fill Form']))

    with tabs[0]:
        st.subheader("Instructions")
        with st.expander("Carefully Read All Instructions", expanded=True):
            st.markdown(r"""
                Follow these instructions to fill the form:
                - Complete all the mandatory fields.
                - Ensure that your first and last names have a minimum of 4 characters.
                - Provide a valid email address and phone number.
                - The address should be at least 10 characters long.
                - Click the 'Submit Application' button to submit the form.
                """)

    with tabs[1]:
        st.info("Please provide the required information below. Fields marked with * are mandatory.")
        with st.form("application_form"):
            st.subheader("Personal Information")

            with st.expander("Fill Personal Information", expanded=True):
                first_name = st.text_input("First Name*", max_chars=15)
                if len(first_name) < 4:
                    st.warning("Please enter a valid first name with a minimum of 4 characters.")

                last_name = st.text_input("Last Name*", max_chars=15)
                if len(last_name) < 4:
                    st.warning("Please enter a valid last name with a minimum of 4 characters.")

                age = st.slider("age", min_value=18, max_value=80, value=20)

            st.subheader("Contact Information")

            with st.expander("Fill Contact Information", expanded=True):
                email = st.text_input("Email*", help="example@example.com")
                if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
                    st.warning("Please enter a valid email address.")

                country_code = st.selectbox("Select Country Code", ["+91", "+1", "+44"])
                phone_input = st.text_input("Phone Number*", max_chars=13)
                if not re.match(r'^[0-9]{8,13}$', phone_input):
                    st.warning("Please enter a valid phone number with 8 to 13 digits.")

                address = st.text_area("Address*", max_chars=200)
                if len(address) < 10:
                    st.warning("Please enter a valid address with a minimum of 10 characters.")


            def validate_form():
                """
                Validate form input using JavaScript-like validations.
                """
                if len(first_name) < 4 or len(last_name) < 4 or not is_valid_email(email) or not is_valid_phone(
                        phone_input) or len(address) < 10:
                    st.error('Please fill in all required fields correctly.')
                    return False

                return True

            def is_valid_email(email):
                """
                Validate email using a regular expression.
                """
                email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
                return bool(re.match(email_regex, email))

            def is_valid_phone(phone_input):
                """
                Validate phone using a regular expression.
                """
                phone_regex = r"^[0-9]{8,13}$"
                return bool(re.match(phone_regex, phone_input))

            submit_button = st.form_submit_button("Submit Application")

            if submit_button and validate_form():
                progress = st.progress(0)
                for i in range(100):
                    time.sleep(0.01)
                    progress.progress(i + 1)
                st.success("Thank you for submitting your application!")
                st.balloons()
                st.write('First Name:', first_name)
                st.write('Last Name:', last_name)
                st.write('Age:', age)
                st.write('Email:', email)
                st.write('Phone Number:', f"{country_code} {phone_input}")
                st.write('Address:', address)

st.markdown("---")
st.markdown("© 2023. All rights reserved.")
