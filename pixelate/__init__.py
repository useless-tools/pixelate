from PIL import Image


def pixelate(input_file_path: str, output_file_path: str, pixel_size: int):
    """
    Create a pixel image from the input image.
    
    Args:
        input_file_path: the path to the source image file to be processed.
        output_file_path: the path to the result file.
        pixel_size: pixel size.
        
    Raises:
        FileNotFoundError: if `input_file_path` does not exist.
        TypeError: if `pixel_size` is not int.
        ValueError: if `pixel_size` is not correct int.
    """
    with Image.open(input_file_path) as image:
        image = image.resize(
            (image.size[0] // pixel_size, image.size[1] // pixel_size),
            Image.NEAREST
        )
        image = image.resize(
            (image.size[0] * pixel_size, image.size[1] * pixel_size),
            Image.NEAREST
        )
        image.save(output_file_path)

