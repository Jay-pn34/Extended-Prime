import pandas as pd

# Initialize an empty list to store results
data = []

start_1 = 2
end_1 = 100
end_2 = 500

# Loop through start values from 2 to 100
for start in range(start_1, end_1):
    primes = []

    # Find prime numbers from start to 100
    for i in range(start, end_2):
    #for i in range(start, end_1):
        for j in range(start, i):
            if i % j == 0:
                break
        else:
            primes.append(i)

    # Append the primes list and the start value to the data list
    data.append([start] + primes)

# Convert the data list into a DataFrame
# Create column names dynamically based on the maximum number of primes
max_primes = max(len(primes[1:]) for primes in data)  # We exclude the start value itself
columns = ['Start'] + [f"Prime_{i+1}" for i in range(max_primes)]

# Create DataFrame from data list
result_df = pd.DataFrame(data, columns=columns)

result_df.set_index('Start', inplace=True)

# Print the result DataFrame
result_df
