# Collatz Conjecture Visualizer

This project visualizes the Collatz Conjecture sequences for given ranges of numbers.

## What is the Collatz Conjecture?

The Collatz Conjecture, also known as the 3n + 1 problem, is an unsolved mathematical conjecture proposed by Lothar Collatz in 1937. The conjecture involves a sequence defined as follows:

1. Start with any positive integer `n`.
2. If `n` is even, divide it by 2.
3. If `n` is odd, multiply it by 3 and add 1.
4. Repeat the process with the resulting number.

The conjecture asserts that no matter what positive integer `n` you start with, you will always eventually reach the number 1.

## Project Structure

- `collatz_plot.py`: Contains the function to generate the Collatz sequence for a given number.
- `collatz_plot_one.py`: Plots the Collatz sequence for a single number.
- `collatz_plot_range.py`: Plots the Collatz sequences for a range of numbers, each in a different color.
- `requirements.txt`: Lists the dependencies required to run the scripts.

## How to Run This Code

1. **Clone the repository**:
   ```bash
   git clone https://github.com/aidarkezio/collatz-conjecture-visualizer.git
   cd collatz-conjecture-visualizer
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv collatz_conjecture
   # On Windows
   collatz_conjecture\Scripts\activate
   # On macOS/Linux
   source collatz_conjecture/bin/activate
   ```

3. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the scripts**:
   - To visualize the Collatz sequence for a single number:
     ```bash
     python collatz_plot_one.py
     ```
   - To visualize the Collatz sequences for a range of numbers:
     ```bash
     python collatz_plot_range.py
     ```

## Author

- Subhadra Poshitha

## License

This project is licensed under the MIT License - see the [](LICENSE) file for details.
