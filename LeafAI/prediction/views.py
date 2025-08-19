from django.shortcuts import render
from django.core.files.storage import default_storage
from .utils import predict_image
import os

def predict_view(request):
    prediction = None
    confidence = None
    image_url = None

    if request.method == "POST" and request.FILES.get("image"):
        # Save uploaded image temporarily
        uploaded_file = request.FILES["image"]
        file_path = default_storage.save(uploaded_file.name, uploaded_file)
        file_path = os.path.join(default_storage.location, file_path)

        # Run prediction
        predicted_label, conf, img = predict_image(file_path)
        prediction = predicted_label
        confidence = round(conf, 2)

        # Get image URL for frontend
        image_url = default_storage.url(uploaded_file.name)

    return render(request, "prediction.html", {
        "prediction": prediction,
        "confidence": confidence,
        "image_url": image_url,
    })
