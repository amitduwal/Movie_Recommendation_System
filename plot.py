import matplotlib.pyplot as plt
import pandas as pd



def data_plot(data):

    fig = plt.figure(figsize=(15,10))
    ax = fig.add_subplot(projection='3d')

    g = ax.scatter(data["P_Genre"], data["S_Genre"], data["T_Genre"], c = data['Cluster_Id'])
    ax.set_xlabel("P_Genre")
    ax.set_ylabel("S_Genre")
    ax.set_zlabel("T_Genre")
    
    fig.savefig('clustering_plot.png', dpi=1000)
    # plt.show()

df = pd.read_csv("Dataset_to_plot.csv")

data_plot(df)
