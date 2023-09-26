# Solution to Challenge 1 of YSC2244 Challenge 1

## Given prompt

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

Attachements: 1997-AK-MCE-R1a.rnd

Oh I also found this somewhere, it might be useful to know:
