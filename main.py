# Imports
# ----------------------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from sklearn import datasets
import numpy as np
from sklearn.cluster import k_means
import pandas as pd

#TITLE OF THE ASSIGNMENT
#-----------------------------------------------------------------------------------------------------------------------

st.title("Kmeans Assignment")
st.write(""""Explore the different numbers of k clusters Which one is the best""")

#SIDEBAR
#-----------------------------------------------------------------------------------------------------------------------

dataset_name = st.sidebar.selectbox("Select Dataset", ("Iris", "Breast Cancer", "Wine dataset"))
sidebar = st.sidebar
n_clusters = sidebar.slider(
    "Select Number of Clusters",
    min_value=2,
    max_value=10,)

#CHOOSE DATASET MENU
#-----------------------------------------------------------------------------------------------------------------------

def get_dataset(dataset_name):
    #IRIS DATASET-----------------------------------------------------------------------------------|

    if dataset_name == "Iris":
        data = datasets.load_iris()

        # turn dataloaded to dataframe ------------------------------------------------------------|

        df=pd.DataFrame(data=data.data, columns=data.feature_names)
        df["target"] = data.target

       # st.write(df.info)

        #Image of the Iris Flowers-----------------------------------------------------------------|
        from PIL import Image
        image = Image.open('iris3.png')
        st.image(image, caption='IrisDataset')



        #show the dataset
        # Display the dataframe
        df_display = st.checkbox("Display Raw Data", value=True)

        new_title = '<p style="font-family:Boyna; color:Green; font-size: 42px;">New image</p>'
        st.markdown(new_title, unsafe_allow_html=True)

        if df_display:
            st.write(data)

    elif dataset_name == "Breast Cancer":
        data = datasets.load_breast_cancer()

        # Image of the ribbon
        from PIL import Image
        image = Image.open('breast cancer.jpg.')
        st.image(image, caption='Raise Awareness')

      #show the dataset
        # Display the dataframe
        df_display = st.checkbox("Display Raw Data", value=True)

        new_title = '<p style="font-family:Boyna; color:Green; font-size: 42px;">New image</p>'
        st.markdown(new_title, unsafe_allow_html=True)

        if df_display:
            st.write(data)
    else:
        dataset_name == "WINE DATA"
        data = datasets.load_wine()

        # Image of the ribbon
        from PIL import Image
        image = Image.open('wine.jpg.')
        st.image(image, caption='Got Cheese?')

        # show the dataset
        # Display the dataframe
        df_display = st.checkbox("Display Raw Data", value=True)

        new_title = '<p style="font-family:Boyna; color:Green; font-size: 42px;">New image</p>'
        st.markdown(new_title, unsafe_allow_html=True)

        if df_display:
            st.write(data)
    X = data.data
    y = data.target
    return X, y
X, y = get_dataset(dataset_name)
st.write("shape of dataset", X.shape)
st.write("number of classes", len(np.unique(y)))