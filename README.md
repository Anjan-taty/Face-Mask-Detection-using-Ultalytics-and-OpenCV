# Face Mask Detection using OpenCV and Deep Learning

This project implements a real-time Face Mask Detection system using Computer Vision and Deep Learning. The application captures video from the webcam, detects human faces using OpenCV, and predicts whether the detected person is wearing a mask or not using a trained Convolutional Neural Network (CNN) model.

The project is useful for demonstrating how deep learning models can be integrated with real-time video processing systems. It can be applied in safety monitoring environments such as public places, workplaces, or educational demonstrations.

---------------------------------------

## Project Overview

The system performs the following tasks:

1. Captures real-time video from the webcam.
2. Detects faces in the video frame using OpenCV's Haar Cascade classifier.
3. Extracts the face region from the frame.
4. Preprocesses the image to match the CNN model input format.
5. Uses a trained TensorFlow model to predict mask or no mask.
6. Displays the prediction result with a bounding box around the face.

The output visualization is:

Green bounding box → Mask detected  
Red bounding box → No Mask detected

---------------------------------------

## Technologies Used

Python  
OpenCV  
TensorFlow
NumPy  
Haar Cascade Face Detection  

---------------------------------------

## Project Structure

Face-Mask-Detection
│
├── main.py                # Main script for real-time detection
├── mask_detector.h5      # Trained CNN model
├── requirements.txt      # Required Python libraries
├── reference.ipynb       # This contains some basics of Opencv and other libraries used here
└── README.md             # Project documentation

---------------------------------------

## Installation

### 1. Clone the repository

git clone https://github.com/Anjan-taty/Face-Mask-Detection-using-Ultalytics-and-OpenCV.git

cd face-mask-detection

---------------------------------------

### 2. Create a virtual environment (optional but recommended)

Windows

python -m venv myenv
myenv\Scripts\activate

Linux / Mac

python -m venv myenv
source myenv/bin/activate

---------------------------------------

### 3. Install dependencies

pip install -r requirements.txt

---------------------------------------

## Requirements

The project depends on the following Python libraries:

opencv-python  
tensorflow  
numpy  

Example requirements.txt file:

opencv-python
tensorflow
numpy

---------------------------------------

## Running the Application

Run the program using the following command:

python main.py

Your webcam will start automatically and the program will begin detecting faces and predicting mask status.

Press **Q** on the keyboard to exit the application.

---------------------------------------

## Model Details

The project uses a Convolutional Neural Network (CNN) trained to classify two categories:

with_mask  
without_mask  

Input preprocessing used before prediction:

• Face image resized to 128 × 128  
• Pixel values normalized by dividing by 255  
• Color conversion from BGR (OpenCV format) to RGB  

Prediction logic:

If prediction > 0.5 → No Mask  
If prediction ≤ 0.5 → Mask  

---------------------------------------

## Face Detection

Face detection is performed using OpenCV's built-in Haar Cascade model:

haarcascade_frontalface_default.xml

This classifier is included with OpenCV and automatically detects faces in grayscale images.

---------------------------------------

## Example Output

The system displays predictions directly on the video feed.

Example labels displayed on the screen:

Mask (0.92)  
No Mask (0.87)

The number represents the model's prediction confidence.

---------------------------------------

## Future Improvements

Possible improvements for the project include:

• Using YOLO or RetinaFace for better face detection  
• Training the CNN model on a larger dataset  
• Deploying the model as a web application using Flask or Streamlit  
• Adding support for image upload detection  
• Improving performance using MobileNetV2 or EfficientNet  

---------------------------------------

## Author

This project was developed as a Computer Vision demonstration of real-time face mask detection using OpenCV and Deep Learning.

---------------------------------------