import matplotlib.pyplot as plt

def show_func(func_values, xs=list(range(-5, 12))):
    _, ax = plt.subplots(figsize=(16, 8))
    ax.plot(xs, func_values, label="Значения функции")
    ax.plot(xs, func_values, "o")
    plt.grid(linestyle="--")
    ax.legend(loc="best")
    plt.savefig('1.png')
