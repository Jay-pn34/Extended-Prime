import matplotlib.pyplot as plt

plot_size = 2.5
# Create a scatter plot
plt.figure(figsize=(12 * plot_size, 8 * 5 * plot_size))

# Plotting each start value and its corresponding primes
for start in range(start_1, end_1):
    if start in result_df.index:  # Check if 'start' exists in the DataFrame index
        primes = result_df.loc[start].dropna()  # Drop NaN values
        plt.scatter([start] * len(primes), primes, label=f"Start {start}", alpha=0.6)

# Add title and labels
plt.title('Extended Prime')
plt.xlabel('Start Value')
plt.ylabel('Prime Number')

# Show gridlines
plt.grid(True)

# Show more axis values on x and y axes
plt.xticks(range(start_1, end_1, 1))  # Adjust x-ticks step size to 2 (change as needed)
plt.yticks(range(start_1, end_2, 1))  # Adjust y-ticks step size to 2 (change as needed)

# Show the plot
plt.show()
