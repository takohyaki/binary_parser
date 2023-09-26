from binary_file_parser.file_parser import read_file
from binary_file_parser.utils.visualization import plot_scatterplot, plot_histogram
import pandas as pd

data_path = "data/1997-AK-MCE-R1a.rnd"
df = read_file(data_path)

# For scatterplot
plot_scatterplot(df, 'longitude', 'latitude', title="Seismic Data", xlabel="Longitude", ylabel="Latitude")

# For histogram
plot_histogram(df, 'S1', title="Histogram of S1 Values", xlabel="S1 Value", bins=30)