from binary_file_parser.file_parser import read_file
from binary_file_parser.utils import plot_scatterplot, plot_histogram
import pandas as pd

data_path = 'data/1997-AK-MCE-R1a.rnd'
df = read_file(data_path)

print(df)

# For scatterplot
plot_scatterplot(df, 'longitude', 'latitude', title='Geographical Distribution Seismic Data Point Locations', xlabel='Longitude', ylabel='Latitude')

# For histogram
plot_histogram(df, 'SS', title='Histogram of SS Values', xlabel='SS Value', bins=30)
plot_histogram(df, 'S1', title='Histogram of S1 Values', xlabel='S1 Value', bins=30)