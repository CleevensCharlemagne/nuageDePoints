# Importer la bibliothèque matplotlib
import matplotlib.pyplot as plt

x = [0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2]
y = [52.12, 52.16, 52.24, 52.28, 52.32, 52.37, 52.44, 52.47]

plt.scatter(x, y)

plt.title("Nuage de points de la série statistique")
plt.xlabel("Durée en heure (xi)")
plt.ylabel("Moyenne en mm (yi)")

plt.show()
