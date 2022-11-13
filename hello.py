""" from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(random_state=0) """
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()
