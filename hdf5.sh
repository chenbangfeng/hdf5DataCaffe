#!/usr/bin/env bash

FILE=$1

MAX=500

NUM_LINES=$(cat $FILE | wc -l)

echo $NUM_LINES

K=$(echo "print int($NUM_LINES)//int($MAX)" | python)

M=$(echo $FILE | awk -F'/' '{print NF}')

FILE_NAME=$(echo $FILE | cut -d'/' -f$M)

if [ "$K" -eq "0" ]
then
     python create_hdf5_file_image_data.py $FILE
else
    for ((i=0 ; i<K ; i++))
    do
        awk "NR%$K==$i" $FILE > $FILE.$i
        python create_hdf5_file_image_data.py $FILE.$i
        rm $FILE.$i
    done
fi




