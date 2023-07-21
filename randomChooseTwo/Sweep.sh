#!/bin/bash

for i in 1 2 3 4 5 6 7 8 9 10 20 30 40 50 60 70 80 90 100; do
  MAXIMUM_SIZE=$((10 * $i))
  export MAXIMUM_SIZE
  echo $MAXIMUM_SIZE
  python3 RandomChooseTwo.py > random_choose_output_$i.csv
done
