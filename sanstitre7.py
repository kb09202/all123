import yfinance as yf
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

# Téléchargement des données Yahoo Finance
data = yf.download("GC=F", start="2023-01-01", end="2024-06-30")  # Exemple pour l'or
prices = data['Close'].dropna()  # Supprime les valeurs manquantes

# Décomposer la série temporelle
result = seasonal_decompose(prices, model='multiplicative', period=30)

# Visualiser les composants
result.plot()
plt.show()
