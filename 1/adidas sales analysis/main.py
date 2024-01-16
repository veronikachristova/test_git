import pandas as pd #data manipulation
import numpy as np #pre numericke operacie
import matplotlib.pyplot as plt #vizualizacia
import seaborn as sns #vizualizacia
import calendar #na pracu s datumami
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima.model import ARIMA #moving average na time series forecasting

file_path = r'C:\Users\OperationsManager\OneDrive\Dokumenty\Analysis projects\adidas_sales_dataset.csv'
adidas = pd.read_csv(file_path)
print(adidas.head())