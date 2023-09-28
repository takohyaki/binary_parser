import struct
import pandas as pd

def wrap_lat(latitude):
    if -90 <= latitude <= 90:
        return latitude
    return (abs(latitude) % 180) - 90 if latitude < 0 else 90 - (abs(latitude) % 180)

def wrap_long(longitude):
    if -180 <= longitude < 180:
        return longitude
    return (longitude + 180) % 360 - 180

def read_file(file_path):
    byte_lengths = {'recnum': 4, 'latitude': 4, 'longitude': 4, 'numvals': 2, 'SS': 4, 'S1': 4}
    unpack_formats = {'recnum': 'i', 'latitude': 'f', 'longitude': 'f', 'numvals': 'h', 'SS': 'f', 'S1': 'f'}

    r = []
    lat = []
    long = [] 
    nv = []
    SS_list = [] 
    S1_list = []
    with open(file_path, 'rb') as file:
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
            r.append(recnum)
            lat.append(latitude)
            long.append(longitude)
            nv.append(numvals)
            SS_list.append(SS)
            S1_list.append(S1)
            file.seek(2, 1)  # skip 2 bytes

    lat = [wrap_lat(latitude) for latitude in lat]
    long = [wrap_long(longitude) for longitude in long]

    df = pd.DataFrame({'recnum': r, 'latitude': lat, 'longitude': long, 'numvals': nv, 'SS': SS_list, 'S1': S1_list})
    return df
