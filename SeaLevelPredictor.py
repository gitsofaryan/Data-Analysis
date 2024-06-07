import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# 1. Use Pandas to import the data from epa-sea-level.csv.
df = pd.read_csv('epa-sea-level.csv')

# 2. Use matplotlib to create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', alpha=0.6)

# 3. Use the linregress function to get the slope and y-intercept of the line of best fit
slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

# Plot the line of best fit through 2050
plt.plot(range(1880, 2051), slope * range(1880, 2051) + intercept, color='red', label='Best Fit Line (1880-2050)')

# 4. Plot a new line of best fit using data from year 2000 through the most recent year in the dataset
df_recent = df[df['Year'] >= 2000]
slope_recent, intercept_recent, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
plt.plot(range(2000, 2051), slope_recent * range(2000, 2051) + intercept_recent, color='green', label='Best Fit Line (2000-2050)')

# 5. Set labels and title
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')

# Add legend
plt.legend()

# 6. Save and return the image
plt.savefig('sea_level_plot.png')
plt.show()
