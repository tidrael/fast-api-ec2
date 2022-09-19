from fastapi import FastAPI, File
from PIL import Image
from app.clf import ImageClassifier

app = FastAPI()


@app.get("/")
async def root():
    return {"Sever": "Running"}


@app.post("/predict")
async def predict(file: bytes = File(...)):
    upload_file = file
    image = Image.open(upload_file)
    model = ImageClassifier()
    prediction = model.predict(image)
    return {f"The result is: {prediction}"}
