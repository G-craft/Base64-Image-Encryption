# Base64 Image Encryption

## Overview

This project is a Python application that allows you to apply a Caesar cipher transformation to images encoded in Base64 format. You can either encode or decode an image based on a user-provided seed value. The application features a graphical user interface (GUI) built with Tkinter, which enables you to select an image file, input a seed, and save the transformed or decoded image.

## Features

- **Encode Image**: Apply Caesar cipher encoding to an image based on the provided seed.
- **Decode Image**: Revert the Caesar cipher transformation from an encoded image using the same seed.
- **File Selection**: Browse and select image files from your local system.
- **Image Saving**: Save the transformed or decoded image to your local system.

## Requirements

- Python 3.x
- PIL (Pillow) library
- Tkinter (typically included with Python standard library)

## Installation

1. **Clone the repository** (if applicable) or copy the script into your working directory.

2. **Install required packages**. You can use the following command to install the necessary packages:

``` 
pip install pillow
```

## Usage

1. **Run the Script**: Execute the Python script to start the GUI application.

```
python Encoder.py
```

2. **Input Seed**: Enter a seed value in the "Seed" text box. This seed determines how the Caesar cipher will be applied.

3. **Select File**: Click the "Browse" button to select the image file you want to transform.

4. **Transform Image**:
- Click "Save Transformed Image" to apply Caesar cipher encoding based on the seed and save the result.
- Click "Save Decoded Image" to revert the encoding based on the seed and save the original image.

## Functions

### `parse_seed(seed)`

Parses the seed into a list of (position, shift) tuples for Caesar cipher transformation.

- **Parameters**:
- `seed` (str): The seed string used for generating positions and shifts.
- **Returns**:
- List of tuples representing (position, shift).

### `caesar_cipher(char, shift)`

Applies a Caesar cipher shift to a single character.

- **Parameters**:
- `char` (str): The character to be shifted.
- `shift` (int): The shift value.
- **Returns**:
- The shifted character.

### `apply_seed_to_base64(seed, base64_str, reverse=False)`

Applies or reverses Caesar cipher transformation to a Base64 encoded string.

- **Parameters**:
- `seed` (str): The seed string.
- `base64_str` (str): The Base64 encoded string.
- `reverse` (bool): Whether to reverse the transformation.
- **Returns**:
- Transformed Base64 string.

### `select_file()`

Opens a file dialog to select an image file and updates the file URL entry in the GUI.

### `save_image(content)`

Opens a save dialog to save the image data to a file.

- **Parameters**:
- `content` (bytes): The image data to be saved.

### `transform_image(encode=True)`

Transforms the image based on the provided seed and either encodes or decodes the image.

- **Parameters**:
- `encode` (bool): Whether to encode or decode the image.

## Troubleshooting

- **Error Messages**: Ensure the seed format is correct and that you have selected a valid image file. The application will show error dialogs for invalid inputs or issues during processing.

- **Dependencies**: If you encounter issues with missing packages, make sure you have installed all required libraries.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on the project's repository.

## Acknowledgements

- [Pillow](https://pillow.readthedocs.io/en/stable/) for image processing.
- [Tkinter](https://docs.python.org/3/library/tkinter.html) for the GUI framework.

---

Feel free to modify or enhance the functionality as needed for your use case.
