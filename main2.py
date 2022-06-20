# Imports
# -----------------------------------------------------------
...
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from sklearn import datasets
import numpy as np
from IPython.display import Image
from sklearn.cluster import KMeans
import pandas as pd

st.title("Kmeans Assignment")

st.write(""""Explore the different numbers of k clusters Which one is the best""")

dataset_name = st.sidebar.selectbox("Select Dataset", ("Iris", "Breast Cancer", "Wine dataset"))
# SIDEBAR
# -----------------------------------------------------------
sidebar = st.sidebar
n_clusters = sidebar.slider(
    "Select Number of Clusters",
    min_value=2,
    max_value=10,
)

#CHOOSE DATASET MENU
#-----------------------------------------------------------------------------------------------------------------------

def get_dataset(dataset_name):
    #IRIS DATASET-----------------------------------------------------------------------------------|

    if dataset_name == "Iris":
        data = datasets.load_iris()
        # turn dataloaded to dataframe ------------------------------------------------------------|

        df = pd.DataFrame(data=data.data, columns=data.feature_names)
        df["target"] = data.target

    # st.write(df.info)

        sns. pairplot(df)

        x = df.iloc[:, [0,1,2,3]].values
        from sklearn.cluster import KMeans
        wcss = []

        for i in range (1, 11):
            kmeans = KMeans(n_clusters = i, init = 'k-means++', max_iter = 300, n_init = 10,random_state = 0)
            kmeans.fit(x)
            wcss.append(kmeans.inertia_)

        plt.plot(range(1,11), wcss)
        plt.title('The elbow method')
        plt.xlabel('Number of clusters')
        plt.ylabel('WCSS')
        plt.show()


        #Image of the flowers
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