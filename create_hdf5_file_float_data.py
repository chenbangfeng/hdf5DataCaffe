import h5py, sys
import numpy as np

SIZE = 4096
NUM_LABELS = 100


# *******************************************************************************************


lines = open(sys.argv[1], 'r').readlines()
data = np.zeros((len(lines), SIZE), dtype='f4')
labels = np.zeros((len(lines), NUM_LABELS), dtype='f4')
num_data = len(lines)
for i, line in enumerate(lines):
    line = line.rstrip().split(' ')
    vgg = line[:SIZE]
    lab = line[SIZE:]
    labels[i] = [float(x) for x in lab]
    data[i] = [float(x) for x in vgg]

with h5py.File(sys.argv[1]+'.h5', 'w') as H:
    H.create_dataset('data', data=data)
    H.create_dataset('label', data=labels)

# *******************************************************************************************
