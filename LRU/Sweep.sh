#!/bin/bash

total_size=494036113199
for i in 0.05 0.1 0.2 0.3 0.4; do
  export MAXIMUM_SIZE=$(echo "$total_size * $i / 1" | bc -q)
  python3 LRU.py > output_$i.csv
done
