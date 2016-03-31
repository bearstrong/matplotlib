import matplotlib
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1)
x = [0.500000001, 0.500000002]
y = [1e64, 1.1e64]
ax.plot(x, y)
plt.show()