import streamlit as st
import pandas as pd
import numpy as np


a = [1,2,3,4,5,6,7,8]
n = np.array(a)
nd = n.reshape((2,4))
dic = {
    "name":["harsh","Gupta"],
    "age":[21,32],
    "city":["noida","delhi"]
}

data = pd.read_csv("data//salary_data.csv")

st.dataframe(data, width=500, height= 500)
st.table(dic)
st.json(dic)
st.write(dic)



#Download csv file
df2 = pd.DataFrame(
    np.random.randn(10 , 2) ,
    columns = ["col1" , "col2"]
)
data2 = df2.to_csv().encode("utf-8")

st.download_button(
    label = "Download this" ,
    data = data2 ,
    file_name = "new_data_file.csv" ,
    mime = "text/csv"
)

#Download text file
text_contents = "This is some text"
st.download_button("Please download" , text_contents)

#Download image file
file = open("data//sal.jpg" , "rb")
btn = st.download_button(
    label = "Download the image" ,
    data = file ,
    file_name = "the_dog_image.jpg" ,
    mime = "image/jpg"
)


