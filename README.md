# Face Mask Detection using OpenCV and Deep Learning

This project implements a real-time Face Mask Detection system using Computer Vision and Deep Learning. The application captures video from the webcam, detects human faces using OpenCV, and predicts whether the detected person is wearing a mask or not using a trained Convolutional Neural Network (CNN) model.

The project is useful for demonstrating how deep learning models can be integrated with real-time video processing systems. It can be applied in safety monitoring environments such as public places, workplaces, or educational demonstrations.

---

## Project Overview

The system performs the following tasks:

1. Captures real-time video from the webcam.
2. Detects faces in the video frame using OpenCV's Haar Cascade classifier.
3. Extracts the face region from the frame.
4. Preprocesses the image to match the CNN model input format.
5. Uses a trained TensorFlow model to predict mask or no mask.
6. Displays the prediction result with a bounding box around the face.

**Output visualization:**

- Green bounding box → Mask detected  
- Red bounding box → No Mask detected  

---

## Technologies Used

- Python  
- OpenCV  
- TensorFlow  
- NumPy  
- Haar Cascade Face Detection  

---

## Project Structure

```
Face-Mask-Detection/
│
├── main.py              # Main script for real-time detection
├── mask_detector.h5    # Trained CNN model
├── requirements.txt    # Required Python libraries
├── reference.ipynb     # OpenCV experiments / notes
└── README.md           # Project documentation
```

---

## Installation

### 1. Clone the repository

```
git clone https://github.com/Anjan-taty/Face-Mask-Detection-using-Ultalytics-and-OpenCV.git
cd face-mask-detection
```

---

### 2. Create a virtual environment (optional but recommended)

**Windows**

```
python -m venv myenv
myenv\Scripts\activate
```

**Linux / Mac**

```
python -m venv myenv
source myenv/bin/activate
```

---

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

## Requirements

The project depends on the following Python libraries:

- opencv-python  
- tensorflow  
- numpy  

Example `requirements.txt`:

```
opencv-python
tensorflow
numpy
```

---

## Running the Application

Run the program using:

```
python main.py
```

Your webcam will start automatically and the system will begin detecting faces and predicting mask status.

Press **Q** to exit the application.

---

## Model Details

The project uses a Convolutional Neural Network (CNN) trained to classify two categories:

- with_mask  
- without_mask  

**Input preprocessing:**

- Resize image to 128 × 128  
- Normalize pixel values (divide by 255)  
- Convert BGR → RGB  

**Prediction logic:**

- If prediction > 0.5 → No Mask  
- If prediction ≤ 0.5 → Mask  

---

## Face Detection

Face detection is performed using OpenCV's Haar Cascade:

```
haarcascade_frontalface_default.xml
```

---

## Example Output

```
Mask (0.92)
No Mask (0.87)
```

---

## Future Improvements

- Use YOLO or RetinaFace for better detection  
- Train with a larger dataset  
- Deploy using Flask or Streamlit  
- Add image upload support  
- Improve model with MobileNetV2 or EfficientNet  

---

## Author

This project was developed as a Computer Vision demonstration of real-time face mask detection using OpenCV and Deep Learning.