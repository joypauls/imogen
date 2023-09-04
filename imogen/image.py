import numpy as np
import math
from PIL import Image as PILImage


GRAYSCALE_METHODS = {
    "colorimetric": np.array([0.2126, 0.7152, 0.0722]),
    "naive": np.array([0.3333, 0.3333, 0.3333]),
}


class Image:
    """
    Container for an image. Goal is to have the data represented in a form that
    is ready to do operations on, such as a numpy array.

    For color:
    Enforce 3rd dimension in array ordered like: R, G, B, alpha (optional)
    """

    def __init__(self):
        # self.img = None
        self.data = np.array([])
        self.size = (0, 0)
        self.num_channels = 0

    def read(self, path: str):
        img = PILImage.open(path)
        self.data = np.array(img)
        shape = np.shape(self.data)
        self.size = shape[0:2]
        if len(shape) == 2:
            self.num_channels = 1
        else:
            self.num_channels = shape[2]

    def to_grayscale(self, method: str = "colorimetric") -> np.ndarray:
        if self.num_channels > 1:
            return np.dot(self.data[:, :, 0:3], GRAYSCALE_METHODS[method]).astype(
                np.uint8
            )
        else:
            return self.data

    def binarize(self, threshold: int = 127):
        gray = self.to_grayscale()
        print(self.data.dtype)
        self.data = np.where(gray > threshold, np.uint8(255), np.uint8(0))
        # TODO: not this
        # self.img = PILImage.fromarray(self.data)
