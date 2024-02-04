import streamlit as st

st.title("My Streamlit App")

st.header("Header")

st.subheader("Sub-Header")

st.markdown(""" # h1 tag
    ## h2 tag
    ### h3 tag

    :sunglasses:<br>
    :moon:<br>
    *Single*<br>
    **Double**<br>
    _Under_
""", True)

st.latex(r''' a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)''')
d ={
    "name":"Harsh",
    "language":"Python",
    "topic":"Streamlit"
} 
st.write(d)


def summ(a , b):
    return a + b

with st.echo():
    def mult(a , b):
        return a * b
    a = 10
    b = 20
    su = summ(a , b)
    mu = mult(a , b)
    st.write(su , mu)
st.write("This is outside")

code = '''def func():
    print(np.arange(10))'''
st.code(code , language = "python")

