import pandas as pd
from StatCharts import StatCharts

df = pd.read_csv('sp500yr.csv')
df.head()
df.tail()
df.info()
charts = StatCharts(df)
charts.histogram('returns')
charts.scatterplot('year','returns')
charts.scatterplot('year','inflation')
charts.scatterplot('returns','unemployment')
charts.boxplot('returns')
charts.boxplot('inflation')
charts.boxplot('unemployment')
charts.correlation_heatmap()