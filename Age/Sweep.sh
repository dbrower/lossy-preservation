#!/bin/bash

for i in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20; do
  MAXIMUM_SIZE=$((365 * $i))
  export MAXIMUM_SIZE
  echo $MAXIMUM_SIZE
  python3 Age.py > output_file_$i.csv
done