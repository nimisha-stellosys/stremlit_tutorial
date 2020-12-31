##import streamlit as st
#import pandas as pd
#df = pd.read_csv('store_sales (1).csv')
#as= df.head()
#siteHeader = st.beta_container()
#with siteHeader:
    
   # st.title('Welcome to the Awesome project!')
#with head:
 #   st.text("Data set ")
#st.tabl
#distribution_pickup = pd.DataFrame(df['city'].value_counts()) #3 
#st.bar_chart(distribution_pickup)
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
st.title('Iris')
url = " https://bit.ly/3kXTdox" # Reading the dataset from remote link
df = pd.read_csv(url)
if st.checkbox('Show dataframe'):
    
    
    st.write(df)
    st.subheader('Scatter plot')
    #df['variety']=df['Iris-setosa','Iris-versicolor','Iris-virginica']

species = st.multiselect('Show iris per variety?', df['Species'].unique())
col1 = st.selectbox('Which feature on x?', df.columns[0:4])
col2 = st.selectbox('Which feature on y?', df.columns[0:4])
new_df = df[(df['Species'].isin(species))]
st.write(new_df)
# create figure using plotly express
fig = px.scatter(new_df, x =col1,y=col2, color='Species')
# Plot!
st.plotly_chart(fig)
st.subheader('Histogram')
feature = st.selectbox('Which feature?', df.columns[0:4])
# Filter dataframe
new_df2 = df[(df['Species'].isin(species))][feature]
fig2 = px.histogram(new_df, x=feature, color="Species", marginal="rug")
st.plotly_chart(fig)
#
st.subheader('Machine Learning models')
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
from sklearn.svm import SVC
features= df[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']].values
labels = df['Species'].values
X_train,X_test, y_train, y_test = train_test_split(features, labels, train_size=0.7, random_state=1)
alg = ['Decision Tree', 'Support Vector Machine']
classifier = st.selectbox('Which algorithm?', alg)
if classifier=='Decision Tree':
    dtc = DecisionTreeClassifier()
    dtc.fit(X_train, y_train)
    acc = dtc.score(X_test, y_test)
    st.write('Accuracy: ', acc)
    pred_dtc = dtc.predict(X_test)
    cm_dtc=confusion_matrix(y_test,pred_dtc)
    st.write('Confusion matrix: ', cm_dtc)
elif classifier == 'Support Vector Machine':
    svm=SVC()
    svm.fit(X_train, y_train)
    acc = svm.score(X_test, y_test)
    st.write('Accuracy: ', acc)
    pred_svm = svm.predict(X_test)
    cm=confusion_matrix(y_test,pred_svm)
    st.write('Confusion matrix: ', cm)
