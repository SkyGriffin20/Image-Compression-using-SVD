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
3. Place your target image in the same directory as the script, renaming it castle.jpg (or update the code to specify a different path).

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
### Input
![castle](https://github.com/user-attachments/assets/8e4b0b88-8969-415e-8c5f-6d389aad0d54)

### Compressed Images
- r = 500
  
![image](https://github.com/user-attachments/assets/a16307c6-3fe2-4c50-9fdd-08a34861f9c6)

- r = 400
  
![image](https://github.com/user-attachments/assets/183b4ea7-23e0-41b6-9d52-74410a885ef7)


- r = 300
  
![image](https://github.com/user-attachments/assets/1d007509-addc-4202-92dc-f2ffe9827998)


- r = 200
  
![image](https://github.com/user-attachments/assets/d38fc008-9d74-4b4c-a13e-b4ae256c175b)


- r = 150
  
![image](https://github.com/user-attachments/assets/4bc490a5-0d49-4961-a014-ea7f4d1c77ee)


- r = 100
  
![image](https://github.com/user-attachments/assets/ed00eccc-4800-47ca-9004-bd2c68ef6484)


- r = 75
  
![image](https://github.com/user-attachments/assets/b6dfcfb1-0da8-4987-84fe-e42afae3c368)


- r = 50
  
![image](https://github.com/user-attachments/assets/4854951c-15c5-405f-99dc-5d2a26651c13)



### Graphs
- Singular Values Graph: A plot on a logarithmic scale showing the distribution of singular values.

![image](https://github.com/user-attachments/assets/9844a16f-9cab-4a29-8863-0b0a7e3cf681)

  
- Cumulative Sum Graph: A graph displaying the cumulative percentage of singular values, useful for understanding how many singular values are needed for a given quality level.

![image](https://github.com/user-attachments/assets/b20af5fe-8e83-4516-89f3-2caefc562d60)


## Future Improvements
- Extend the project to include colour image compression.
- Implement additional metrics to evaluate the quality of compressed images (e.g., Mean Squared Error).
- Add functionality for user-specified image paths and compression levels.


