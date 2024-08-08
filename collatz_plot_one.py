import matplotlib.pyplot as plt
import collatz_plot as cp

def plot_collatz(sequence):
    steps = list(range(len(sequence)))
    max_value = max(sequence)
    
    plt.figure(figsize=(10, 6))
    plt.plot(steps, sequence, marker='o')
    plt.title(f"Collatz Conjecture Sequence for n = {sequence[0]}")
    plt.xlabel("Steps")
    plt.ylabel("Values")
    plt.ylim(0, max_value + 10)
    plt.grid(True)
    plt.show()

# Example usage
n = 10  # Change this value to test with different starting numbers
sequence = cp.collatz_sequence(n)
plot_collatz(sequence)