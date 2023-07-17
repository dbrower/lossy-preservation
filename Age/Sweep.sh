#!/bin/bash

for i in 1 2 3 6 9 10 15 20; do
  MAXIMUM_SIZE=$((365 * $i))
  export MAXIMUM_SIZE
  python3 Age.py > output_file_$i.csv
done