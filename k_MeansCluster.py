import matplotlib.pyplot as plt
import numpy as np
import pandas as ps


dataset=ps.read_csv("Mall_Customers.csv")
X=dataset.iloc[:,[3,4]].values # it gas only features of salary and time spend



from sklearn.cluster import KMeans

"""Need to find elbow pattern for the particular model"""

elbow_Value=[]


for a in range(1,11):
    kmeans=KMeans(init="k-means++",n_clusters=a,random_state=23)
    kmeans.fit(X)
    elbow_Value.append(kmeans.inertia_)

"""plotting elbow value"""

# plt.plot(range(1,11),elbow_Value)
# plt.title("Elbow method")
# plt.xlabel(" range")
# plt.ylabel("elbow value")
# plt.legend()
# plt.show()
"""Elbow value 5 is correct coorelation value"""


kmeans=KMeans(n_clusters=5,init="k-means++",random_state=21)
ymeans=kmeans.fit_predict(X)


"""plotting vlaue for clustering KMeans"""


plt.scatter(X[:,0],X[:,1],c=ymeans,cmap="rainbow",s=10)
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],marker="s",s=20)
plt.ylabel("Time Spending ",fontsize=16)
plt.xlabel("Salary in K ",fontsize=16)
plt.title("K-Means Clustering")
plt.show()




print(elbow_Value)