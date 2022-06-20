

# Imports
# ----------------------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from sklearn import datasets #I used the Iris Dataset that was in this import
import numpy as np
from sklearn.cluster import k_means, KMeans
import pandas as pd


st.title("Kobe Assignment")
st.write(""""Explore the different numbers of k clusters Which one is the best""")

#making a sidebar to hold the min k value of 2 max of 1-
dataset_name = st.title("I USED THE IRIS DATASET")
sidebar = st.sidebar
n_clusters = sidebar.slider(
    "Select Number of Clusters",
    min_value=2,
    max_value=10,)

#CHOOSE DATASET MENU
#-----------------------------------------------------------------------------------------------------------------------

def get_dataset(dataset_name):
    #IRIS DATASET-----------------------------------------------------------------------------------|

        dataset_name == "Iris"
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


        # Display the dataframe
        df_display = st.checkbox("Display Raw Data", value=True)

        new_title = '<p style="font-family:Boyna; color:Red; font-size: 42px;">ENJOY </p>'
        st.markdown(new_title, unsafe_allow_html=True)

        if df_display:
            st.write(data)
            X = data.data
            y = data.target
            return X, y

X, y = get_dataset(dataset_name)
st.write("shape of dataset", X.shape)
st.write("number of classes", len(np.unique(y)))
