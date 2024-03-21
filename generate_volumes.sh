#!/bin/bash

# Define the range of directories to be created
for i in {1..4}; do
  for j in {1..2}; do
    # Create the directory and its subdirectories
    mkdir -p "data${i}-${j}/data1" "data${i}-${j}/data2"
  done
done