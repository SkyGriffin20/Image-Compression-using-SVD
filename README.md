# Image Compression using Singular Value Decomposition (SVD)

## Overview
This project demonstrates image compression using Singular Value Decomposition (SVD) in Python. By approximating a grayscale image matrix, the code reduces both the image's storage size and quality, showing how SVD can be applied to efficiently compress images.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Working](#working)
- [Sample Output](#sample-output)
- [Future Improvements](#future-improvements)
- [Contact](#contact)

## Features
- **Image Compression**: Compresses a grayscale image to various levels based on the number of singular values retained.
- **Quality vs. Compression Level Visualization**: Plots graphs to illustrate the relationship between image quality and the level of compression.
- **Singular Value Analysis**: Displays the singular values and their cumulative sum, highlighting how compression affects image data.

## Technologies Used
- **Python**: Core programming language.
- **NumPy**: For numerical operations and matrix manipulations.
- **Matplotlib**: For displaying images and generating quality vs. size graphs.

## Installation
1. Clone or download this repository.
2. Ensure you have Python and the required libraries installed:
   ```bash
   pip install matplotlib numpy
3. Place your target image in the same directory as the script, renaming it as castle.jpg (or update the code to specify a different path).

## Working
1. Run the Python script:
   ```bash
   python image_compression_svd.py

2. The script will:
   - Convert the input image to grayscale.
   - Display compressed images at different compression levels (e.g., retaining 50, 75, 100, etc., singular values).
   - Plot two graphs showing:
       1. Singular values on a logarithmic scale.
       2. Cumulative sum of singular values as a percentage.
3. Output: You will see a series of images at different compression levels, followed by two graphs indicating how singular values contribute to image data retention.

## Sample Output
### Compressed Images
### Graphs
- Singular Values Graph: A plot on a logarithmic scale showing the distribution of singular values.
- Cumulative Sum Graph: A graph displaying the cumulative percentage of singular values, useful for understanding how many singular values are needed for a given quality level.

## Future Improvements
- Extend the project to include colour image compression.
- Implement additional metrics to evaluate the quality of compressed images (e.g., Mean Squared Error).
- Add functionality for user-specified image paths and compression levels.


