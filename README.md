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



## Todo

1. Define data access file format
1. Write the code that applies an eviction policy to a trace data file
1. Code to anaylize result file to evaulate performace of each eviction policy.
