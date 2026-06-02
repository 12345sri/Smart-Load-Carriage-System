import matplotlib.pyplot as plt

# Sample load distribution data
positions = ['Front', 'Back', 'Left', 'Right']
weights = [12, 18, 10, 15]

# Plot
plt.bar(positions, weights)

plt.title("Load Distribution Analysis")
plt.xlabel("Position")
plt.ylabel("Weight (kg)")

plt.show()
