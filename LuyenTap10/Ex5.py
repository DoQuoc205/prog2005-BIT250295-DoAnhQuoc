import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(-10, 10, 100)
y1 = x1**2

x2 = np.linspace(0, 10, 100)
y2 = np.sqrt(x2)

fig, axs = plt.subplots(1, 2, figsize=(10, 4))

axs[0].plot(x1, y1)
axs[0].set_title("Đồ thị y = x^2")
axs[0].set_xlabel("x")
axs[0].set_ylabel("y")

axs[1].plot(x2, y2)
axs[1].set_title("Đồ thị y = sqrt(x)")
axs[1].set_xlabel("x")
axs[1].set_ylabel("y")

plt.tight_layout()
plt.show()