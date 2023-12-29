import matplotlib.pyplot as plt

def draw(func, start, end, step=0.1):
    x_values = []
    y_values = []

    x = start

    while x < end:
        x_values.append(x)
        y_values.append(func(x))
        x += step


    plt.plot(x_values, y_values)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('График функции')
    plt.grid(True)
    plt.savefig('my_plot.png')
