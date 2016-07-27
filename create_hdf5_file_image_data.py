import argparse
import h5py
import cv2
import numpy as np

SIZE = 224
NB_LABELS = 490

MEANB = 104  # same order as in prototxt file
MEANG = 117  # cv2 reads channels BLUE - GREEN - RED
MEANR = 123


def get_hdf5_image_data(img, size, meanB, meanG, meanR):
    """
    Transforms image data into appropriate format for HDF5 data layer
    """
    img = cv2.resize(img, (size, size))
    img[:, :, 0] -= meanB
    img[:, :, 1] -= meanG
    img[:, :, 2] -= meanR
    return np.transpose(img, (2, 0, 1)).astype(np.int)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="""Script to make hdf5 files for multilabel tasks with caffe""")
    parser.add_argument("labels_path", help="File containing path to images and corresponding labels")
    args = parser.parse_args()
    with open(args.labels_path) as f:
        lines = [line.rstrip().split(' ') for line in f]
    im_data = np.zeros((2 * len(lines), 3, SIZE, SIZE), dtype='f4')  # multiply by 2 for flipped images
    label_data = np.zeros((2 * len(lines), NB_LABELS), dtype='f4')
    nb_data = len(lines)
    for i, line in enumerate(lines):
        impath, labels = line[0], line[1:]
        img = cv2.imread(impath).astype(np.float32)
        im_data[i] = get_hdf5_image_data(img, SIZE, MEANB, MEANG, MEANR)
        im_data[nb_data + i] = get_hdf5_image_data(cv2.flip(img, 1), SIZE, MEANB, MEANG, MEANR)   # add flip
        lab = [float(x) for x in labels]
        label_data[i] = lab
        label_data[nb_data + i] = lab
    with h5py.File(args.labels_path + '.h5', 'w') as H:
        H.create_dataset('data', data=im_data)
        H.create_dataset('label', data=label_data)
