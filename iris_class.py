

# Imports
# ----------------------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from sklearn import datasets
import numpy as np
from sklearn.cluster import k_means, KMeans
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

        print(df)
        def run_kmeans(df, n_clusters=2):
            kmeans = KMeans(n_clusters, random_state=0).fit(df[["sepal length (cm)", "petal width (cm)"]])
            df.rename(columns={'sepal length (cm)': 'sl', 'sepal width (cm)': 'sw'}, inplace=True)
            fig, ax = plt.subplots(figsize=(16, 9))

            # Create scatterplot
            ax = sns.scatterplot(
                ax=ax,
                x = df.sl,
                y = df.sw,
                hue=kmeans.labels_,
                palette=sns.color_palette("colorblind", n_colors=n_clusters),
                legend=None,
            )

            return fig

        # -----------------------------------------------------------

        # MAIN APP
        # -----------------------------------------------------------
        # Show cluster scatter plot
        st.write(run_kmeans(df, n_clusters=n_clusters))

        # st.write(df.info)

        #Image of the Iris Flowers-----------------------------------------------------------------|
        from PIL import Image
        image = Image.open('iris3.png')
        st.image(image, caption='IrisDataset')

        df['target'] = pd.Series(data.target)
        df['target_names'] = pd.Series(data.target_names)
        species = []
        for i in range(len(df)):
            if df.iloc[i]['target'] == 0:
                species.append('setosa')
            elif df.iloc[i]['target'] == 1:
                species.append('versicolor')
            elif df.iloc[i]['target'] == 2:
                species.append('virginica')
        df['Species'] = species
        df
        #show the dataset
        # Display the dataframe
        df_display = st.checkbox("Display Raw Data", value=True)

        new_title = '<p style="font-family:Boyna; color:Green; font-size: 42px;">DATA MINING CSCI 350 KMEANS </p>'
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
