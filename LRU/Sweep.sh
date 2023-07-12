#!/bin/bash

for i in 9 10 11 12 13; do
  MAXIMUM_SIZE=$(echo "10^$i" | bc -q)
  python3 LRU.py > output_$i.csv
done
