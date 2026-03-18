import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load trained model
model = load_model('mask_detector.h5')

# Load Haar Cascade (built into OpenCV)
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml' # type: ignore
)

cap = cv2.VideoCapture(0)
print("Press Q to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        face_roi = frame[y:y+h, x:x+w]

        # FIX 1: Convert BGR → RGB (OpenCV reads BGR, model trained on RGB)
        face_roi_rgb = cv2.cvtColor(face_roi, cv2.COLOR_BGR2RGB)

        # Preprocess for CNN
        resized = cv2.resize(face_roi_rgb, (128, 128))
        normalized = resized / 255.0
        input_tensor = np.expand_dims(normalized, axis=0)  # shape: (1,128,128,3)

        prediction = model.predict(input_tensor, verbose=0)[0][0]

        # FIX 2: class_indices = {'with_mask': 0, 'without_mask': 1}
        # So prediction > 0.5 means without_mask = No Mask
        if prediction > 0.5:
            label = f"No Mask ({prediction:.2f})"
            color = (0, 0, 255)   # Red
        else:
            label = f"Mask ({1 - prediction:.2f})"
            color = (0, 255, 0)   # Green

        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
        cv2.putText(frame, label, (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

    cv2.imshow("Face Mask Detector", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()