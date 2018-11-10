from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

import h5py
import argparse
import numpy as np
import itertools
import random
import matplotlib.pyplot as plt


class Generator(object):
    def __init__(self, h5_file, shuffle=True):
        self.file = h5_file
        self.shuffle = shuffle

    def __call__(self):
        with h5py.File(self.file, 'r') as hf:
            self.num_images = hf['input_image'].shape[0]
            shuffle_indices = range(self.num_images)
            if self.shuffle:
                random.shuffle(shuffle_indices)
            for index in itertools.cycle(shuffle_indices):
                yield hf['input_image'][index]

    def get_num_items(self):
        return self.num_images


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Test H5 generator')
    parser.add_argument('--h5_file', '-f', type=str, default="path to h5 file",
                        help='path to h5 file')
    args = parser.parse_args()

    generator = Generator(args.h5_file)
    gen = generator()

    plt.imshow(next(gen))
    plt.show()
