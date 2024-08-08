import matplotlib.pyplot as plt
import random
import collatz_plot as cp

def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

def plot_collatz_range(start, end):
    plt.figure(figsize=(12, 8))
    max_value = 0
    for n in range(start, end + 1):
        sequence = cp.collatz_sequence(n)
        steps = list(range(len(sequence)))
        max_value = max(max_value, *sequence)
        color = (random.random(), random.random(), random.random())
        plt.plot(steps, sequence, marker='o', label=f'n={n}', color=color)
    
    plt.title(f"Collatz Conjecture Sequences for n = {start} to {end}")
    plt.xlabel("Steps")
    plt.ylabel("Values")
    plt.ylim(0, max_value + 10)
    plt.legend()
    plt.grid(True)
    plt.show()

# Example usage
start = 1  # Change this value to define the start of the range
end = 25    # Change this value to define the end of the range
plot_collatz_range(start, end)
