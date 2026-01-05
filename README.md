Below is a **revised, project-specific `README.md`** for your **Potato Disease Prediction system with 99% accuracy**, aligned with your FastAPI + TensorFlow implementation.

You can replace your existing README with this.

---

# Potato Disease Prediction System (99% Accuracy)

This project is a **deep learning–based Potato Disease Prediction system** exposed as a **FastAPI REST API**.
The model classifies potato leaf images into disease categories with **~99% accuracy** and returns both the predicted class and confidence score.

---

## 🚀 Key Highlights

* **99% model accuracy** on validation data
* Image classification using **TensorFlow / Keras**
* High-performance **FastAPI backend**
* REST API for real-world integration
* Static web UI for quick testing
* CORS-enabled for frontend/mobile apps

---

## 🧠 Disease Classes

The model predicts the following potato leaf conditions:

| Class Name | Description          |
| ---------- | -------------------- |
| Early      | Early Blight disease |
| Late       | Late Blight disease  |
| Healthy    | Healthy potato leaf  |

---

## 🧪 Model Details

* **Architecture:** CNN (trained using TensorFlow/Keras)
* **Input Shape:** `224 × 224 × 3`
* **Model Format:** `model.h5`
* **Accuracy:** ~99%
* **Inference Mode:** Single-image prediction

---

## 🛠 Tech Stack

* **Backend:** FastAPI
* **ML Framework:** TensorFlow / Keras
* **Image Processing:** NumPy, Pillow
* **Server:** Uvicorn
* **Language:** Python

---

## 📁 Project Structure

```
.
├── main.py
├── model.h5
├── static/
│   └── index.html
├── README.md

```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/potato-disease-prediction.git
cd potato-disease-prediction
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Add Model File

Place your trained model in the project root:

```
model.h5
```

> Note: `model.h5` should NOT be pushed to GitHub (already ignored via `.gitignore`).

---

## ▶️ Run the Application

```bash
uvicorn main:app --reload
```

or

```bash
python main.py
```

Server URL:

```
http://127.0.0.1:8000
```

---

## 🔍 API Usage

### 📌 Predict Potato Disease

**Endpoint**

```
POST /predict
```

**Request**

* Type: `multipart/form-data`
* Key: `file`
* Value: Potato leaf image (`.jpg`, `.png`)

**Sample Response**

```json
{
  "class": "Late",
  "confidence": 0.9912
}
```

---

## 🖥 Web UI

A simple static UI is available at:

```
http://127.0.0.1:8000/ui
```

Use it to upload images and test predictions visually.

---

## 🌐 CORS Configuration

CORS is enabled for all origins to support:

* Web frontends
* Mobile apps
* External services

---

## 📊 Use Cases

* Smart agriculture systems
* Crop disease monitoring
* Farmer assistance platforms
* Agri-tech research projects

---

## 🚧 Future Enhancements

* Multi-leaf batch prediction
* Grad-CAM visualization
* Model versioning
* Docker deployment
* Cloud hosting (AWS/GCP/Azure)

---

## 👤 Author

**Atharva Bhakare**
Machine Learning / AI Engineer


