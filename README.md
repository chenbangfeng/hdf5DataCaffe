## Python code to create HDF5 files for multilabel classification with caffe


### Image Data:

Simply run :

```
python create_hdf5_image_data.py train.labels
```

train.labels contains images paths and corresponding labels, for instance :

path/to/images/im1.jpg 0 0 1 0 1 0

New shape, means and number of labels should be specified in ```create_hdf5_image_data.py```

If you have to many images to process, the script ```hdf5.sh``` splits you training data in multiple files

Usage :

```
./hdf5_image.sh train.labels
```

The maximum number of images to process per HDF5 file should be precised in hdf5.sh (currently 500)

### Float Data:

```
python create_hdf5_float_data.py train.labels
```

The train.labels must contain input float vectors and corresponding labels in the same linete   :

VGG features           labels <br />
---------------------|------------  <br />

0.2 0.4 0.9 0.5 0.1 0 0 1 0 1 <br />
0.3 0.5 0.2 0.3 0.8 1 1 0 1 1 <br />
0.7 0.4 0.1 0.4 0.9 1 0 1 0 0 