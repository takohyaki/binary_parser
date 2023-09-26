# binary_file_parser

The `binary_file_parser` package provides tools to parse proprietary binary seismic data into pandas DataFrames. Additionally, it offers visualisation utilities to analyse the parsed data.

## In this README

- [Key Features](#key-features)
- [Directory Structure](#directory-structure)
- [Usage](#usage)
  - [Data Parsing](#data-parsing)
  - [Visualisation](#visualisation)
- [Installation](#installation)

## Key Features

- **Binary Data Parsing**: Transform proprietary binary formatted files into pandas DataFrames
- **Visualisation Tools**: Generate colour-mapped scatterplots and histograms from the parsed data

## Directory Structure

```
binary_file_parser/
│
├── binary_file_parser/
│   ├── __init__.py
│   ├── file_parser.py      # Contains function to parse binary files
│   └── utils.py            # Contains utility functions for data visualisation
│
├── data/
│   └── <1997-AK-MCE-R1a.rnd>   # Seismic dataset
│
├── README.md               # This file
├── setup.py                # Setup script for the package
└── visualisation.py        # Main script to run
```


## Usage

### Data Parsing

To parse binary data, use the `read_file` function from the `file_parser` module:

```python
from binary_file_parser.file_parser import read_file
df = read_file("<path_to_binary_file>")
```

### Visualisation

To visualise the parsed data, utilities from the `utils` module can be employed:

```python
from binary_file_parser.utils import plot_scatterplot, plot_histogram
plot_scatterplot(df, 'longitude', 'latitude', color_column='SS', title='Geospatial Distribution (Coloured by SS values)', xlabel='Longitude', ylabel='Latitude')
plot_histogram(df, 'SS', title='Histogram of SS Values', xlabel='SS Value', bins=30)
```

## Installation

1. **Download and Extract the ZIP File**
2. **Open Anaconda Prompt**
3. **Navigate to the Directory**:
   Use the command to navigate to the directory where you extracted the ZIP file:
   ```bash
   cd path_to_extracted_binary_file_parser_directory
   ```
4. **Install the Package**:
   Run the following command to install the package:
   ```bash
   pip install .
   ```
5. **Usage**:
   Once installed, you can run the visualisation.py file to parse the binary file and view the proposed graphs using the following command:
   ```bash
   python visualisation.py
   ```