
# %%
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
from kneed import KneeLocator

sns.set_theme(style="white")
df = pd.read_csv("ulabox.csv")

dfp = df[['Food%','Fresh%','Drinks%','Home%','Beauty%','Health%','Baby%','Pets%']]


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
kmeans = KMeans(n_clusters=k).fit(df[['Food%','Fresh%','Drinks%','Home%','Beauty%','Health%','Baby%','Pets%']])
sns.scatterplot(data=df, x="Food%", y="Drinks%", hue=kmeans.labels_)
plt.show()


# %%
cluster1=df[kmeans.labels_==0]
sns.boxplot(data=cluster1[['Food%','Fresh%','Drinks%','Home%','Beauty%','Health%','Baby%','Pets%']])

sns.histplot(data=cluster1, x= 'weekday')


# %%
cluster2=df[kmeans.labels_==1]
sns.boxplot(data=cluster2[['Food%','Fresh%','Drinks%','Home%','Beauty%','Health%','Baby%','Pets%']])
sns.histplot(data=cluster2, x= 'weekday')


# %%
cluster3=df[kmeans.labels_==2]
sns.boxplot(data=cluster3[['Food%','Fresh%','Drinks%','Home%','Beauty%','Health%','Baby%','Pets%']])
sns.histplot(data=cluster3, x= 'weekday')


# %%
cluster4=df[kmeans.labels_==3]
sns.boxplot(data=cluster4[['Food%','Fresh%','Drinks%','Home%','Beauty%','Health%','Baby%','Pets%']])
sns.histplot(data=cluster4, x= 'weekday')


# %%
cluster5=df[kmeans.labels_==4]
sns.boxplot(data=cluster5[['Food%','Fresh%','Drinks%','Home%','Beauty%','Health%','Baby%','Pets%']])
sns.histplot(data=cluster5, x= 'weekday')



