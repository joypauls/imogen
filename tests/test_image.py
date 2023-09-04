import pytest

from imogen.image import Image

TEST_IMAGES_PATH = "./tests/resources/images/"
JT_CASES = ["jt_png_16bit.png", "jt_tiff_16bit.tif", "jt_jpeg.jpg"]

# @pytest.fixture
# def response():
#     """Sample pytest fixture.

#     See more at: http://doc.pytest.org/en/latest/fixture.html
#     """
#     # import requests
#     # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


@pytest.mark.parametrize("file", JT_CASES)
def test_read(file):
    img = Image()
    img.read(TEST_IMAGES_PATH + file)
    assert img.data.shape[0:2] == (600, 800)
    assert img.num_channels == 3
