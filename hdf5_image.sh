#!/usr/bin/env bash

FILE=$1

MAX=500
EXPE=10_cnn

#mode="test"
mode="train"

NUM_LINES=$(cat $FILE | wc -l)

echo $NUM_LINES

K=$(echo "print int($NUM_LINES)//int($MAX)" | python)

M=$(echo $FILE | awk -F'/' '{print NF}')

FILE_NAME=$(echo $FILE | cut -d'/' -f$M)

if [ "$K" -eq "0" ]
then
     python create_hdf5_file_image_data.py $FILE
     scp $FILE.h5 ines@bergamote:/scratch_global/ines/cnn_vgg_expe/$EXPE/data/hdf5/$mode
     rm $FILE.h5
     echo "/scratch_global/ines/cnn_vgg_expe/$EXPE/data/hdf5/$mode/$FILE_NAME.h5" >> $mode.h5.list.txt
else
    for ((i=0 ; i<K ; i++))
    do
        awk "NR%$K==$i" $FILE > $FILE.$i
        python create_hdf5_file_image_data.py $FILE.$i
        rm $FILE.$i
        scp $FILE.$i.h5 ines@bergamote:/scratch_global/ines/cnn_vgg_expe/$EXPE/data/hdf5/$mode
        rm $FILE.$i.h5
        echo "/scratch_ssd/ines/$EXPE/$FILE_NAME.$i.h5" >> $mode.h5.list.txt
    done
fi

scp $mode.h5.list.txt ines@bergamote:/scratch_global/ines/cnn_vgg_expe/$EXPE/data/hdf5
rm $mode.h5.list.txt



