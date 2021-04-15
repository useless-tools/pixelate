import hashlib
from pixelate import pixelate
import pytest


def test_run():
    pixelate('test/data/bps.jpg', 'test/data/bps.png', 10)
    
    with open('test/data/bps.png', 'rb') as pic:
        md5_hash = hashlib.md5(pic.read())
        assert md5_hash.hexdigest() == '265371e1a3e2bbe17049357856fa859e'


def test_no_file():
    with pytest.raises(FileNotFoundError):
        pixelate('test/data/nofile.jpg', 'test/data/bps.png', 10)


def test_bad_pixel_size():
    with pytest.raises(TypeError):
        pixelate('test/data/bps.jpg', 'test/data/bps.png', 'qwe')


def test_neg_pixel_size():
    with pytest.raises(ValueError):
        pixelate('test/data/bps.jpg', 'test/data/bps.png', -10)

