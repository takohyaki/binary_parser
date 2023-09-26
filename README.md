# binary_file_parser

The `binary_file_parser` package provides tools to parse proprietary binary seismic data into pandas DataFrames. Additionally, it offers visualisation utilities to analyse the parsed data.

## In this README :point_down:

- [Key Features](#key-features)
- [Directory Structure](#directory-structure)
- [Usage](#usage)
  - [Data Parsing](#data-parsing)
  - [Visualisation](#visualisation)
- [Installation](#installation)
- [Assignment Prompt](#assignment-prompt)

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

## Assignment Prompt

1.1  Linda's email

Hi there,

I heard you joined the team recently, I am sorry to ask you for things so soon,

but we need some data points for the seismologists — there is an emergency (already...).

The data is stored in a proprietary format, but the software to parse it does not exist anymore.

I need you to write a python package, or at least a script, that can read the files and generate a pandas.DataFrame object.

I have given you a sample of the data files attached.

To help, I've done some research:

even though the software is not available, the people in the previous team happened to keep some records about the format. I hope this helps you.

> Design Ground Motions
>
>These files contain SS and S1 ground motion data (corresponding to the 0.2 second and 1.0 second periods respectively). 
The basic format of the binary file is as follows:
>
>&lt;recnum&gt;&lt;latitude&gt;&lt;longitude&gt;&lt;numvals&gt;&lt;SS&gt;&lt;S1&gt;

>Where
>
>>recnum : 4-Byte Integer Just an index identifying the record number in the file.
>
>>latitude : 4-Byte Floating Point Number Specifies the geographic latitude of the location.
>
>>longitude : 4-Byte Floating Point Number Specifies the geographic longitude of the location.
>
>>numvals : 2-Byte Short Integer Specifies the number of valid values in this record.
>>>Generally for this file type there are always two (2) values. Names, the SS and S1.
>
>>SS : 4-Byte Floating Point Number The value of the short period (0.2 second) ground motion at this location.
>
>>S1 : 4-Byte Floating Point Number The value of the 1.0 second ground motion at this location.

Oh I also found this somewhere, it might be useful to know:

>Some files contain binary “short” values which are two bytes long. 
After finishing reading a particular record from the binary file, 
you must then skip two bytes in order to be on the proper “word boundary” to start reading data for the next record. 

If you can only produce the DataFrame on time that's fine, but honestly the team would appreciate it if you could perform an initial analysis on the data and propose a few graphs to visualize it.

Attachements: [1997-AK-MCE-R1a.rnd](https://github.com/tammiekoh1518/binary_parser/blob/main/data/1997-AK-MCE-R1a.rnd)
