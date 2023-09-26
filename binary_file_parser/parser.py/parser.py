import struct
import pandas as pd

def parse_binary_file(file_path):
    byte_lengths = {'recnum': 4, 'latitude': 4, 'longitude': 4, 'numvals': 2, 'SS': 4, 'S1': 4}
    unpack_formats = {'recnum': 'i', 'latitude': 'f', 'longitude': 'f', 'numvals': 'h', 'SS': 'f', 'S1': 'f'}

    recnums, latitudes, longitudes, numvals_list, SS_vals, S1_vals = [], [], [], [], [], []
    with open(file_path, "rb") as file:
        while True:
            try:
                recnum = struct.unpack(unpack_formats['recnum'], file.read(byte_lengths['recnum']))[0]
                latitude = struct.unpack(unpack_formats['latitude'], file.read(byte_lengths['latitude']))[0]
                longitude = struct.unpack(unpack_formats['longitude'], file.read(byte_lengths['longitude']))[0]
                numvals = struct.unpack(unpack_formats['numvals'], file.read(byte_lengths['numvals']))[0]
                SS = struct.unpack(unpack_formats['SS'], file.read(byte_lengths['SS']))[0]
                S1 = struct.unpack(unpack_formats['S1'], file.read(byte_lengths['S1']))[0]
            except:
                break
            recnums.append(recnum)
            latitudes.append(latitude)
            longitudes.append(longitude)
            numvals_list.append(numvals)
            SS_vals.append(SS)
            S1_vals.append(S1)
            file.seek(2, 1)  # skip 2 bytes

    df = pd.DataFrame({'recnum': recnums, 'latitude': latitudes, 'longitude': longitudes, 'numvals': numvals_list, 'SS': SS_vals, 'S1': S1_vals})
    return df
