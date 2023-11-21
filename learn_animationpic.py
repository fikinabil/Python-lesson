import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the parameters of the animation
fig, ax = plt.subplots()
x = np.arange(0, 10, 0.1)
y = np.sin(x)
line, = ax.plot(x, y)

# Define the animation function
def update(num, x, y, line):
    line.set_data(x[:num], y[:num])
    line.axes.axis([0, 10, -1, 1])
    return line,

# Create the animation
ani = animation.FuncAnimation(fig, update, len(x), fargs=[x, y, line],
                              interval=50, blit=True)

# Show the animation
plt.show()
