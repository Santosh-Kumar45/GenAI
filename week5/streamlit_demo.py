import streamlit as st

#page configuration 

st.set_page_config(
    page_title="python crash course",
    page_icon="🐍",
    layout="wide"
)

#title ,header,subheader and text  
st.title("Python Application Crash Course")
st.header("Streamlit Basics")
st.subheader("Build Simple web Applications with python")

st.write("Streamlit lets us turn python code into an interactive web application ")
st.markdown("### Markdown also works here.")
st.caption("This is a small caption.")

#code ,json, metric
st.code("print('Hello Friends!!')",language="python")
st.json({
    "Course":"Python",
    "Level":"Beginner"
})
st.metric("Students",25, "+5")


#sidebar
st.sidebar.title("Course Menu")
st.sidebar.write("choose an option below:")

topic=st.sidebar.selectbox(
    "Choose a topic",
    ["Python","Pandas","NumPy","AI Application","PowerBI"]
)
st.write(f"Selected option is : {topic}")

#Text input
name= st.text_input("What is your name?")

if name:
    st.write(f"Hello,{name}")

#number input
age=st.number_input(
    "Enter your age",
    min_value=1,
    max_value=100,
    value=18 
)
st.write(f"your age is: {age}")

confidence=st.slider(
    "Choose a confidence score.",
    min_value=0,
    max_value=100,
    value=50
)
st.write(f"Confidence score :{confidence}")


#checkbox
show_details=st.checkbox("show course details")

if show_details:
    st.info("This course prepares you to build python applications for AI.")


#radio button 
experience=st.radio(
    "Your python experience.",
    ["Beginner","Intermediate","Advanced"]
)     
st.write(f"Selected experience : {experience}")

#selectedbox and multiselect

language=st.selectbox(
    "Choose a programming language:",
    ["Python","Java","JavaScript","C++"]
)
skills=st.multiselect(
    "Choose your skills:",
    ["python","numpy","pandas","git","streamlit"]
)

st.write(f"Language : {language}")
st.write(f"skills : {skills}")


#button
if st.button("Click me"):
    st.success("Button clicked successfully!!")


#form
with st.form("Student_form"):
    st.write("Student Registation")

    student_name=st.text_input("Student Name")
    student_email=st.text_input("Email")

    submitted=st.form_submit_button("Register")
    if submitted:
        st.success(f"Registration received for {student_name}")    



#columns
col1,col2,col3=st.columns(3)

with col1:
    st.info("python")
with col2:
    st.info("pandas")
with col3:
    st.info("numpy")


#Expander
with st.expander("show more info: "):
    st.write("Expanders are useful when we want to hide details until needed.")


#status messages
st.success("success message")
st.info("information based message")
st.warning("warning message")
st.error("error message")



#progress bar
st.progress(79)


#file uploader 
uploaded_file=st.file_uploader(
    "Upload a text file.",
    type=["txt","pdf"],
    max_upload_size=10
)
if uploaded_file is not None:
    content=uploaded_file.read().decode("utf-8")
    st.text_area(f"Uploaded content", content, height=150,)



#Download button 
sample_text="Hello, thanks for connecting with me !"

st.download_button(
    label="Download sample text",
    data=sample_text,
    file_name="sample.txt",
    mime="text/plain"
)