# Hierarchical Clustering for Invoice Data

This project demonstrates the use of **Hierarchical Clustering** to categorize invoice data based on features such as `StockCode`, `Quantity`, `UnitPrice`, and `CustomerID`. The goal is to perform unsupervised learning to segment the data and analyze the groupings formed by the clustering algorithm.

## Table of Contents

- [Project Overview](#project-overview)
- [Data Description](#data-description)
- [Dataset Source](#dataset-source)
- [Libraries Used](#libraries-used)
- [Project Workflow](#project-workflow)
- [Results](#results)
- [Conclusion](#conclusion)
- [License](#license)

## Project Overview

In this project, we utilize the **Agglomerative Clustering** algorithm from the `sklearn` library to group invoice records based on various features. The primary goal is to discover hidden patterns in the data and use them for further analysis, such as identifying product types with similar characteristics, customer buying behaviors, etc.

## Data Description

The dataset contains invoice information for an online retailer. The columns used for clustering are:

- **InvoiceNo**: The invoice number for the transaction.
- **StockCode**: A unique identifier for each product sold.
- **Description**: The name/description of the product.
- **Quantity**: The number of items purchased in each transaction.
- **InvoiceDate**: The date and time when the invoice was created.
- **UnitPrice**: The price of a single unit of the product.
- **CustomerID**: A unique identifier for each customer.
- **Country**: The country where the transaction took place.

Sample data from the dataset looks like this:

| InvoiceNo | StockCode | Description                         | Quantity | InvoiceDate           | UnitPrice | CustomerID | Country      |
|-----------|-----------|-------------------------------------|----------|-----------------------|-----------|------------|--------------|
| 536365    | 85123A    | WHITE HANGING HEART T-LIGHT HOLDER  | 6        | 2010-12-01 08:26:00   | 2.55      | 17850.0    | United Kingdom |
| 536365    | 71053     | WHITE METAL LANTERN                 | 6        | 2010-12-01 08:26:00   | 3.39      | 17850.0    | United Kingdom |
| 536365    | 84406B    | CREAM CUPID HEARTS COAT HANGER      | 8        | 2010-12-01 08:26:00   | 2.75      | 17850.0    | United Kingdom |
| ...       | ...       | ...                                 | ...      | ...                   | ...       | ...        | ...          |

## Dataset Source

The dataset used in this project is the **Customer Segmentation Dataset** available on **Kaggle**. It contains customer data for an e-commerce company, which includes transactional data for segmentation and clustering.

You can access the dataset at the following link:  
[Customer Segmentation Dataset - Kaggle](https://www.kaggle.com/datasets/yasserh/customer-segmentation-dataset)

## Libraries Used

This project requires the following Python libraries:

- `pandas` - For data manipulation and analysis.
- `numpy` - For numerical operations.
- `matplotlib` - For plotting visualizations.
- `sklearn` - For machine learning algorithms, specifically **Agglomerative Clustering**.

To install the required libraries, use the following command:

```bash
pip install pandas numpy matplotlib scikit-learn
```

## Project Workflow

### 1. Data Loading and Preprocessing

The dataset is loaded into a Pandas DataFrame. We perform necessary preprocessing steps such as handling missing values, converting data types, and selecting relevant features for clustering.

### 2. Feature Selection

We focus on specific features that are most relevant for clustering, such as `Quantity`, `UnitPrice`, and `CustomerID`.

### 3. Data Normalization

Since Hierarchical Clustering does not require the data to be scaled, we can proceed without scaling the data. However, if scaling were needed, we would use `StandardScaler` to normalize the features.

### 4. Hierarchical Clustering

**Agglomerative Clustering** (a type of hierarchical clustering) is applied to the preprocessed data to find clusters. The number of clusters is initially set to 5.


### 5. Analyzing the Cluster Labels

The cluster labels are appended to the original DataFrame, and the results are analyzed to understand the characteristics of each cluster.

### 6. Visualizing the Results

Visualizations are created using `matplotlib` to better understand the clustering results.

## Results

After applying **Agglomerative Clustering** (Hierarchical Clustering), the dataset was grouped into several clusters. Below are some key insights based on the cluster labels:

- **Cluster 0**: Products that tend to be bought in bulk or have low price points.
- **Cluster 1**: High-ticket items that have fewer transactions.
- **Cluster 4**: Products with higher unit prices and higher quantities.
- (Other clusters are similarly described based on the analysis)

### Cluster Visualization

To visualize the clustering results, here is a plot showing how the data points were grouped based on their `Quantity` and `UnitPrice`:

![Cluster Plot](C:\Users\Dnyanesh's Asus\Desktop\IdeaProjects\Data Science\Hierarchial-Clustering-Project\images\Cluster Plot.png)

This plot shows the different clusters as distinct colors, and you can observe the separation of products with similar characteristics.

### Dendrogram

If you applied hierarchical clustering, here's a **dendrogram** that visually represents how the clusters were merged:

![Dendrogram](C:\Users\Dnyanesh's Asus\Desktop\IdeaProjects\Data Science\Hierarchial-Clustering-Project\Dendrogram.png)

The dendrogram helps to understand the hierarchical relationships between clusters and provides insight into the distance at which they were merged.

### Cluster Distribution by Features

To further analyze the clusters, below is a histogram showing the distribution of the `UnitPrice` for each cluster:


This histogram illustrates the range of `UnitPrice` values for each cluster, highlighting how prices vary across different product groups.

### Cluster Labels Example

The cluster labels for the first few records are as follows:

```
Cluster Labels: [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 1 0 0 4 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
```

These labels indicate which cluster each invoice record belongs to.

## Conclusion

This project demonstrated the use of **Agglomerative Clustering** (Hierarchical Clustering) to segment invoice data into distinct groups. The cluster labels provide insight into potential patterns in customer purchases, product types, and transactional behaviors. Further analysis could help identify marketing strategies or improve inventory management for businesses.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
