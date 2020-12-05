#!/usr/bin/env python3
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import pandas as pd

pd.set_option("display.max_rows", 100, "display.max_columns", 100)

divider = "\n\n"
divider_end = "\n--------------------------------------------------------------------------------"

df = pd.read_csv("./Clothes_Ranking.csv", index_col = 0).T
df = df.drop("Pickiness (avg)", axis = 1)

print("Original Data" + divider_end)
print(df.T)

data_scaled = pd.DataFrame(preprocessing.scale(df), columns = df.columns)

print(divider + "Scaled Data" + divider_end)
print(data_scaled.T.round(2))

pca = PCA(n_components=5)

principal_components = pca.fit_transform(data_scaled)
print(divider + "New Components in Terms of Old Components" + divider_end)
print(pd.DataFrame(pca.components_,columns=data_scaled.columns,index = ['PC-' + str(k) for k in range(0, 5)]).T.round(2))
#print(pca.components_)
print(divider + "Variance Explained by Each Component" + divider_end)
print([round(100 * k, 1) for k in pca.explained_variance_ratio_])
print("Total Variance Explained: " + str(round(sum(pca.explained_variance_ratio_), 2)))
print(divider + "New Matrix for Everyone in New Components" + divider_end)
print(pd.DataFrame(data = principal_components , columns = ['PC-' + str(k) for k in range(0, 5)]).round(2))

df_orig = pca.inverse_transform(principal_components)
#print(pd.DataFrame(df_orig).T)
