import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Télécharger les données (par exemple, pour l'or)
symbol = "GC=F"  # Or (Gold)
data = yf.download(symbol, start="2023-01-01", end="2024-06-30")

# Vérifier si les données sont bien téléchargées
if data.empty:
    raise ValueError("Impossible de télécharger les données. Vérifiez le symbole ou la connexion.")

# Ajouter des colonnes dérivées pour l'analyse
data['Day'] = data.index.day
data['Month'] = data.index.month
data['Year'] = data.index.year

# Visualisation des données
plt.figure(figsize=(10, 6))
plt.plot(data['Close'], label='Prix de clôture (Gold)')
plt.title("Prix de l'or (Clôture)")
plt.xlabel("Date")
plt.ylabel("Prix")
plt.legend()
plt.show()

# Préparation des données pour le modèle
features = ['Day', 'Month', 'Year']
target = 'Close'

# Supprimer les valeurs manquantes
data = data.dropna()

X = data[features]
y = data[target]

# Division en ensemble d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modèle de régression simple
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Prédictions et évaluation
predictions = model.predict(X_test)
rmse = mean_squared_error(y_test, predictions, squared=False)
print(f"RMSE : {rmse:.2f}")

# Visualisation des prédictions
plt.figure(figsize=(10, 6))
plt.plot(y_test.values, label='Valeurs Réelles')
plt.plot(predictions, label='Prédictions', linestyle='dashed')
plt.title("Prédictions vs Réel")
plt.xlabel("Index")
plt.ylabel("Prix")
plt.legend()
plt.show()
