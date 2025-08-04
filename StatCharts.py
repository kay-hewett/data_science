import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class StatCharts:
    def __init__(self, data: pd.DataFrame):
        self.data = data

    def histogram(self, column, bins=10):
        plt.figure(figsize=(8, 5))
        sns.histplot(self.data[column], bins=bins, kde=True)
        plt.title(f'Histogram of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.show()

    def boxplot(self, column):
        plt.figure(figsize=(8, 5))
        sns.boxplot(x=self.data[column])
        plt.title(f'Boxplot of {column}')
        plt.xlabel(column)
        plt.show()

    def scatterplot(self, x_col, y_col):
        plt.figure(figsize=(8, 5))
        sns.scatterplot(x=self.data[x_col], y=self.data[y_col])
        plt.title(f'Scatterplot: {x_col} vs {y_col}')
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.show()

    def correlation_heatmap(self):
        plt.figure(figsize=(10, 8))
        corr = self.data.corr()
        sns.heatmap(corr, annot=True, cmap='coolwarm')
        plt.title('Correlation Heatmap')
        plt.show()

# Install matplotlib if not already installed
try:
    import matplotlib
except ImportError:
    import pip
    pip.main(['install', 'matplotlib'])