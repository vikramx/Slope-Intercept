import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Slope-Intercept App 📈")

x1=st.number_input("Enter first x coordinate here:")
y1=st.number_input("Enter first y coordinate here:")
x2=st.number_input("Enter second x coordinate here:")
y2=st.number_input("Enter second y coordinate here:")
val=""


def slope(x1,y1,x2,y2):
    if x1==x2:
        return "Undefined"
    m=(y2-y1)/(x2-x1)
    return m


def y_ic(x1,y1,m):
    if(m != "Undefined"):
        c=y1-m*x1
        return c

def graph(m,c,val):
    fig=plt.figure(figsize=(8,8))

    x=np.linspace(-10,10,100)
    y=m*x+c
    plt.axhline(y=0, color='k', linewidth=2)
    plt.axvline(x=0, color='k', linewidth=2)
    plt.plot(x,y,color='r')
    # ax.set_xlabel("X-axis")
    # plt.ylabel("Y-axis")
    plt.title(f"Random graph with {val}")
    plt.grid()
    st.pyplot(fig)


m=slope(x1,y1,x2,y2)
c=y_ic(x1,y1,m)

if st.button("Show information"):
    st.write(f"The slope of the line passing through ({x1},{y1}) and ({x2},{y2}) is : {slope(x1, y1, x2, y2)}")
    st.write(f"The y-intercept value is {c}")


    if(m != "Undefined"):
        if m<0:
            val="Negative Slope"
        elif m>0:
            val="Positive Slope"
        else:
            val="Undefined"

    graph(m,c,val)
