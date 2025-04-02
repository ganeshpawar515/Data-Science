from sklearn.datasets import load_iris
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

iris=load_iris()
iris_df=pd.DataFrame(iris.data,columns=iris.feature_names)
iris_df["target"]=iris.target
iris_df["target"]=iris_df["target"].map({0:"Setosa",1:"Versicolor",2:"Verginica"})
print(iris_df)

#correlation between petal length and width
sepal_length=iris_df["sepal length (cm)"]
sepal_width=iris_df["sepal width (cm)"]
petal_length=iris_df["petal length (cm)"]
petal_width=iris_df["petal width (cm)"]
plt.xlabel("petal length")
plt.ylabel("petal width")
plt.scatter(petal_length,sepal_length)
plt.show()