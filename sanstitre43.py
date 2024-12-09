# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 01:17:21 2024

@author: pc
"""

import pandas as pd
import matplotlib.pyplot as plt
import random

# Génération des données fictives
def generate_expense_data(categories, months):
    data = {'Month': [f'Mois {i+1}' for i in range(months)]}
    for category in categories:
        data[category] = [random.randint(200, 1000) for _ in range(months)]
    return pd.DataFrame(data)

# Générer les données
categories = ['Alimentation', 'Logement', 'Loisirs', 'Transports']
expense_data = generate_expense_data(categories, 12)

# Visualisation
expense_data.set_index('Month').plot(kind='area', stacked=True, figsize=(12, 6), alpha=0.8)
plt.title("Répartition des dépenses mensuelles")
plt.xlabel("Mois")
plt.ylabel("Dépenses (€)")
plt.legend(title="Catégories")
plt.tight_layout()
plt.show()
