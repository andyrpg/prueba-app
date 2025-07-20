import streamlit as st

st.title("Página de Andy")

st.header("User info form")
form_values = {
"name": None,
"height": None,
"dob": None,
#"feedback": None,
"time": None,
"choice": None,
"gender": None,
"slider_value": None,
#"notifications": None,
"toggle_value": None
}
with st.form(key='user_info_form'):
    st.subheader("Personal information") 
    #Text input
    form_values["name"] = st.text_input("Enter your name")
    form_values["gender"] = st.selectbox("Select your gender", ['Male','Female','Other'])
    form_values["height"] = st.number_input("Enter your height (cm)")
    form_values["dob"] = st.date_input("select your date of birth")
    form_values["feedback"] = st.text_area("Provide your feedback")
    #Date and time
    st.subheader("Preferred time")
    form_values["time"] = st.time_input("Choose a preferred time for lunch")
    #Selectors
    st.subheader("Preferences")
    form_values["choice"] = st.radio("What do you like the most?", ['Ice cream', 'Pancake', 'Chocolate'])
    
    form_values["slider_value"] = st.select_slider("Choose a number from 1 to 10?", options=[1,2,3,4,5,6,7,8,9,10])
    #Toggles and checkboxes
    
    form_values["toggle_value"] = st.checkbox("I have read all the terms and conditions", value=False)

    submit_button = st.form_submit_button()
    if submit_button:
        if not all(form_values.values()):
            st.warning("Please fill in all the fields")
        else:
            st.balloons()
            st.write("###Info")
            for (key, value) in form_values.items():
                st.write(f"{key}: {value}")
