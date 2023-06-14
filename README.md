Lossy Preservation
==================

Examining the affects of applying cache eviction policies to data storage.


Disk access trace data is fed into a framework that applies a given eviction policy,
and saves the result to another file.
The result consists of the evolution of the total size occupied by the files, and the number of
times a deleted file was asked for.

_Trace data_ is a file that tells for time period which files were created or modified.
It also includes information on each file's size.

_Eviction policy_ decides which files to remove after each time period, given a list of every file. For each file it has
1. a file identifier
2. the file size at the end of the time period
3. the last access date (in terms of the time period)

A _time period_ is a fixed length interval.
All time periods are non-overlapping and form a linear order with respect to "before than", and each interval identified by an integer, with later time periods having a larger identifier.


## Input File Format

The input trace file is a line-oriented file with the first line a list of field names.
The fields are separated with a comma.

Each line consists of:
* A timestamp in unix time (seconds since epoch Jan 1 1970)
* a file identifier
* The size of the file (in bytes)
* The file created date
* The file's current access time
* The file owner
* The file's parent folder

In the trace file, each line represents an access to a file. The lines should be in chronological order from oldest to newest.


## Intermediate file format

The intermediate file records the results of performing an input trace pattern with a given Deletion Algorithm

The file consist of XXX header rows followed by a chronological list of ...

The headers are:
* The date the intermediate file was created
* The deletion policy used
* The input file name

A sample header looks like:

```
Created: 2023-06-14T10:45:36
Policy: LRU
Input: test_data.csv
%%
```
The header section ends with a double percent `%%`.

The rest of the lines consist of a sequence of values, separated by commas, of
* The current simulation time
* The information on this line (H or M or D) see below
* The file id

The "information on this line" is one of the following letters:

    H = A file access found the file on the storage system
    M = A file access did not find the file on the storage system because it had been prevously deleted.
    D = The Policy decied to delete the specified file at this time step.

For every line in the input file there will be a corresponding H or M line in the output file.
In addition there will be lines with a "D".
This means the output file will have at least as many lines as the input file.

Example output file:

```
Created: 2023-06-14T10:45:36
Policy: LRU
Input: test_data.csv
%%
1686267606.828879,H,0feeed21-72df-421d-b2bf-b4e03358f9ed
1686267606.829548,H,6608c68c-80ff-435d-9a0d-77f86071c820
1686267606.829894,H,ddb4ee09-cb41-45c1-982f-63ec39f608e2
1686267606.829894,D,6608c68c-80ff-435d-9a0d-77f86071c820
1686267606.829894,D,0feeed21-72df-421d-b2bf-b4e03358f9ed
1686267606.830228,H,274b410c-9045-4f3a-b87c-bdb68b09f91c
1686267606.849548,M,6608c68c-80ff-435d-9a0d-77f86071c820
```







## Todo

1. Define data access file format
1. Write the code that applies an eviction policy to a trace data file
1. Code to anaylize result file to evaulate performace of each eviction policy.







