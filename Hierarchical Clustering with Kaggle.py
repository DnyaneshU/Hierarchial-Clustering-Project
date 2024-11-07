import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering

# Step 1: Load and preprocess the dataset
def load_data():
    file_path = r"C:\Users\Dnyanesh's Asus\Desktop\IdeaProjects\Data Science\Hierarchial-Clustering-Project\Dataset\Online Retail.xlsx"
    df = pd.read_excel(file_path)
    print(df.head())  # Display the first few rows to understand the data structure
    df.dropna(subset=['CustomerID'], inplace=True)  # Drop rows with missing CustomerID
    df = df[['Quantity', 'UnitPrice']]  # Select relevant columns for clustering
    df.fillna(df.mean(), inplace=True)  # Handle missing values by filling with the mean
    df = df.sample(n=1000, random_state=42)  # Optional: Reduce the dataset size for testing
    return df

# Step 2: Preprocess the data (Standardization)
def preprocess_data(df):
    scaler = StandardScaler()
    df_scaled = scaler.fit_transform(df)  # Standardize the data
    return df_scaled

# Step 3: Hierarchical Clustering - Create the Dendrogram
def plot_dendrogram(df_scaled):
    Z = linkage(df_scaled, method='ward')
    plt.figure(figsize=(10, 7))
    dendrogram(Z)
    plt.title("Dendrogram for Hierarchical Clustering")
    plt.xlabel("Samples")
    plt.ylabel("Distance")
    plt.show()

# Step 4: Fit the Agglomerative Clustering model to the data
def apply_hierarchical_clustering(df_scaled, num_clusters=5):
    hc = AgglomerativeClustering(n_clusters=num_clusters, linkage='ward')
    y_hc = hc.fit_predict(df_scaled)  # Apply clustering and get cluster labels
    return y_hc

# Step 5: Visualize the clusters
def visualize_clusters(df_scaled, y_hc):
    plt.figure(figsize=(10, 7))
    plt.scatter(df_scaled[:, 0], df_scaled[:, 1], c=y_hc, cmap='rainbow')  # Scatter plot with color coding based on clusters
    plt.title("Hierarchical Clustering of Customers")
    plt.xlabel("Scaled Quantity")
    plt.ylabel("Scaled UnitPrice")
    plt.show()

if __name__ == "__main__":
    # Step 1: Load the data
    df = load_data()

    # Step 2: Preprocess the data (standardize)
    df_scaled = preprocess_data(df)

    # Step 3: Plot the Dendrogram
    plot_dendrogram(df_scaled)

    # Step 4: Apply hierarchical clustering and get cluster labels
    y_hc = apply_hierarchical_clustering(df_scaled, num_clusters=5)

    # **Print the Cluster Labels** (this part was missing in the previous code)
    print(f"Cluster Labels: {y_hc}")  # Print the cluster labels for each data point

    # Step 5: Visualize the clusters
    visualize_clusters(df_scaled, y_hc)
