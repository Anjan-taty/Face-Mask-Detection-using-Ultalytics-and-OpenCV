# 😷 Face Mask Detection using OpenCV & Deep Learning

A real-time **Face Mask Detection system** built using **Computer Vision and Deep Learning**.  
The application detects faces from a webcam and predicts whether a person is wearing a mask using a trained **CNN model**.

---

## 🔍 Overview

This project demonstrates how deep learning integrates with **real-time video pipelines**.

### 🎯 Use Cases

- 🏥 Public safety monitoring  
- 🏢 Workplace compliance  
- 🎓 Learning computer vision  

---

## ⚙️ How It Works

```
Webcam → Face Detection → Preprocessing → CNN Model → Prediction → Display
```

### Step-by-step:

1. 🎥 Capture video stream  
2. 🧑 Detect faces (Haar Cascade)  
3. ✂️ Extract face region  
4. 🧠 Preprocess image  
5. 🤖 Predict mask / no mask  
6. 📦 Draw bounding box  

---

## 🎯 Output Visualization

| Status | Color | Meaning |
|------|------|--------|
| ✅ Mask | 🟢 Green | Safe |
| ❌ No Mask | 🔴 Red | Not safe |

Example:

```
Mask (0.92)
No Mask (0.87)
```

---

## 🧠 Model Overview

| Property | Value |
|--------|------|
| Model Type | CNN |
| Task | Binary Classification |
| Classes | Mask / No Mask |
| Input Size | 128 × 128 |
| Framework | TensorFlow / Keras |

---

## 📊 Processing Pipeline

```
Input Image
     ↓
Resize (128×128)
     ↓
Normalize (/255)
     ↓
Convert BGR → RGB
     ↓
CNN Model
     ↓
Probability Output
```

---

## 📈 Prediction Logic (Visual)

```
Confidence Score
│
├── 0.0 ───────────── 0.5 ───────────── 1.0
│        Mask           Threshold         No Mask
```

- ≤ 0.5 → ✅ Mask  
- > 0.5 → ❌ No Mask  

---

## 🛠️ Technologies Used

| Category | Technology |
|--------|-----------|
| Language | Python |
| Vision | OpenCV |
| ML | TensorFlow / Keras |
| Data | NumPy |
| Detection | Haar Cascade |

---

## 📂 Project Structure

```
Face-Mask-Detection/
│
├── main.py              # 🚀 Real-time detection script
├── mask_detector.h5    # 🧠 Trained CNN model
├── requirements.txt    # 📦 Dependencies
├── reference.ipynb     # 📊 Experiments / notes
└── README.md           # 📘 Documentation
```

---

## ⚡ Installation

### 1️⃣ Clone the Repository

```
git clone https://github.com/Anjan-taty/Face-Mask-Detection-using-Ultalytics-and-OpenCV.git
cd Face-Mask-Detection-using-Ultalytics-and-OpenCV
```

---

### 2️⃣ Create Virtual Environment

**🪟 Windows**
```
python -m venv myenv
myenv\Scripts\activate
```

**🐧 Linux / 🍎 Mac**
```
python -m venv myenv
source myenv/bin/activate
```

---

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```
python main.py
```

🎥 Webcam starts automatically  
❌ Press **Q** to exit  

---

## 🧑 Face Detection

Uses OpenCV Haar Cascade:

```
haarcascade_frontalface_default.xml
```

✔ Fast  
✔ Lightweight  
✔ Built-in  

---

## 📊 System Behavior (Conceptual)

```
Normal Case:
[Face] → Model → Correct classification ✅

Edge Case:
[Blurred Face] → Model → Lower confidence ⚠️
```

---

## 🚀 Future Improvements

- 🔥 Replace Haar Cascade with YOLO / RetinaFace  
- 📊 Train on larger dataset  
- 🌐 Deploy using Flask / Streamlit  
- 🖼️ Add image upload support  
- ⚡ Use MobileNetV2 / EfficientNet  

---

## 🎯 Use Case Summary

| Domain | Application |
|------|------------|
| Healthcare | Mask compliance |
| Security | Monitoring systems |
| AI Learning | CV model practice |

---

## 👨‍💻 Author

Developed by **Anjan (Taty)**  
Passionate about AI, Computer Vision, and real-world applications 🚀  

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!