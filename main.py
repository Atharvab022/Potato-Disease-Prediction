import numpy as np
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from io import BytesIO
from PIL import Image
import tensorflow as tf
import uvicorn

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

MODEL = tf.keras.models.load_model("model.h5")
class_names = ["Early", "Late", "Healthy"]

def read_image(data):
    img = Image.open(BytesIO(data))
    img = img.resize((224, 224))   # Use correct size for your model
    return np.array(img)

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    img_bytes = await file.read()
    img = read_image(img_bytes)
    img_batch = np.expand_dims(img, 0)

    pred = MODEL.predict(img_batch)
    cls = class_names[np.argmax(pred)]
    conf = float(np.max(pred))

    return {"class": cls, "confidence": conf}

app.mount("/ui", StaticFiles(directory="static", html=True), name="static")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
