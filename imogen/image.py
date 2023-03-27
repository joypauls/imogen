import numpy as np
from PIL import Image as PILImage


GRAYSCALE_METHODS = {
    "colorimetric": np.array([0.2126, 0.7152, 0.0722]),
    "naive": np.array([0.3333, 0.3333, 0.3333])
}


class Image():
    """
    Container for an image. Goal is to have the data represented in a form that 
    is ready to do operations on, such as a numpy array.

    - should we save when the first op calculates it dft?

    For color:
    Enforce 3rd dimension in array ordered like: R, G, B, alpha (optional)
    """
    def __init__(self):
        self.data = np.array([])
        self.num_channels = 0

    def read(self, path: str):
        img = PILImage.open(path)
        self.data = np.array(img)
        self.num_channels = self.data.shape[2]

    def to_grayscale(self, method: str = "colorimetric") -> np.ndarray:
        return np.dot(GRAYSCALE_METHODS[method], self.data[:,:,0:3])

