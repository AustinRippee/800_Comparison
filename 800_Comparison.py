import pandas as pd

df = pd.read_excel("800_Comparison.xlsx")

# df['Indoor'] = df['Indoor'].astype(str)
# df['Outdoor'] = df['Outdoor'].astype(str)

# Function to convert "m:ss.xx" format to seconds as a float
def time_str_to_seconds(time_str):
    minutes, seconds_and_fraction = time_str.split(':')
    seconds, fraction = seconds_and_fraction.split('.')
    total_seconds = int(minutes) * 60 + int(seconds) + float(fraction) / 100
    return total_seconds

# Convert the time strings in Column1 and Column2 to seconds
df['Indoor_seconds'] = df['Indoor'].apply(time_str_to_seconds)
df['Outdoor_seconds'] = df['Outdoor'].apply(time_str_to_seconds)

# Calculate the difference and represent it as a float
df['Difference'] = (df['Outdoor_seconds'] - df['Indoor_seconds']).round(2)

# Display the DataFrame
print(df[['Name', 'Indoor', 'Outdoor', 'Difference']])

print()

count_less_than_zero = (df['Difference'] < 0).sum()

count_greater_than_zero = (df['Difference'] > 0).sum()

count = count_greater_than_zero + count_less_than_zero

print("Number of athletes that bettered their indoor time:")
print(count_less_than_zero, "/", count, " = ", (count_less_than_zero/count).round(2), "%")