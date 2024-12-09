# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 01:13:39 2024

@author: pc
"""

import pandas as pd
import matplotlib.pyplot as plt
import random

# Génération de données fictives
def generate_student_data(num_students):
    """
    Génère des données fictives de notes pour les étudiants.
    """
    data = []
    for i in range(num_students):
        math = random.randint(40, 100)  # Note en maths
        physics = random.randint(40, 100)  # Note en physique
        chemistry = random.randint(40, 100)  # Note en chimie
        data.append({'student': f'Étudiant {i + 1}', 'math': math, 'physics': physics, 'chemistry': chemistry})
    return pd.DataFrame(data)

# Générer les données
student_data = generate_student_data(20)

# Calcul des moyennes par matière
average_scores = student_data[['math', 'physics', 'chemistry']].mean()

# Visualisation des performances
plt.figure(figsize=(10, 6))
average_scores.plot(kind='bar', color=['blue', 'green', 'red'])
plt.title("Moyennes des notes par matière")
plt.xlabel("Matières")
plt.ylabel("Moyenne")
plt.grid(axis='y')
plt.tight_layout()
plt.show()
