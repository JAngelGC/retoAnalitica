
# %%
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
from kneed import KneeLocator

sns.set_theme(style="white")
df = pd.read_csv("ulabox.csv")

# sns.heatmap(df.corr(), annot=True)


# df.describe()
# df.corr()


dfp = df[["Home%", "Fresh%"]]
# sns.scatterplot(data=df, x="Food%", y="Drinks%")



# # Realizar gráfico de caja
# sns.set_theme(style="white")
# plt.figure(figsize=(10, 4))
# sns.boxplot(x="Pets%",
#                 data=df,
#                 showmeans=True,
#                 meanprops={"marker":"o",
#                        "markerfacecolor":"white", 
#                        "markeredgecolor":"black",
#                       "markersize":"10"})



# %%

ssd = []
ks = range(1,11)
for k in range(1,11):
    km = KMeans(n_clusters=k)
    km = km.fit(dfp)
    ssd.append(km.inertia_)

kneedle = KneeLocator(ks, ssd, S=1.0, curve="convex", direction="decreasing")
kneedle.plot_knee()
plt.show()

k = round(kneedle.knee)

print(f"Number of clusters suggested by knee method: {k}")



# %%

kmeans = KMeans(n_clusters=k).fit(df[["Food%", "Drinks%"]])
sns.scatterplot(data=df, x="Food%", y="Drinks%", hue=kmeans.labels_)
plt.show()

# sns.boxplot(data=df[['Food%','Fresh%','Drinks%',
# 'Home%','Beauty%','Health%','Baby%','Pets%']])
# plt.show()

# cluster1=df[kmeans.labels_==1]
# cluster1.describe()

# sns.histplot(data=df, x= 'hour')
# plt.show()





# from sklearn.tree import DecisionTreeClassifier, export_text

# tree = DecisionTreeClassifier()
# tree.fit(df[["Age", "Food%", "total_items"]], kmeans.labels_)
# print(export_text(tree, feature_names=["Age", "Food%", "total_items"]))
# %%
