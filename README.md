## Python code to create HDF5 files for multilabel classification with caffe


### Image Data:

Simply run :

```
python create_hdf5_image_data.py train.labels.shuffled
```

train.labels contains images paths and corresponding labels, for instance :

path/to/images/im1.jpg 0 0 1 0 1 0

Don't forget to shuffle your data before creating hdf5 files: 

```
shuf train.labels > train.labels.shuffled
```

New shape, means and number of labels should be specified in ```create_hdf5_image_data.py```

If you have to many images to process, the script ```hdf5.sh``` splits you training data in multiple files

Usage :

```
./hdf5_image.sh train.labels.shuffled
```

The maximum number of images to process per HDF5 file should be precised in hdf5.sh (currently 500)

### Float Data:

```
python create_hdf5_float_data.py train.labels.shuffled
```

The train.labels must contain input float vectors and corresponding labels in the same line:

VGG features           labels <br />
---------------------|------------  <br />

0.2 0.4 0.9 0.5 0.1 0 0 1 0 1 <br />
0.3 0.5 0.2 0.3 0.8 1 1 0 1 1 <br />
0.7 0.4 0.1 0.4 0.9 1 0 1 0 0 