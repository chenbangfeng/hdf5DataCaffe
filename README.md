## Python code to create HDF5 files for multilabel classification with caffe

Simply run :

```
python create_hdf5_image_data.py train.labels
```

train.labels contains images paths and corresponding labels, for instance :

path/to/images/im1.jpg 0 0 1
path/to/images/im2.jpg 0 1 0

Resize shape, means and number of labels should be specified in ```create_hdf5_image_data.py```

If you have to many images to process, the script ```hdf5.sh``` splits you training data in multiple files

Usage :

```
./hdf5.sh train.labels
```
The maximum number of images to process per HDF5 file should be precised in hdf5.sh (now 500)