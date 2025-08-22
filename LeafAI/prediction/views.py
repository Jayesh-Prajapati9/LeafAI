from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from .utils import predict_image
from .models import Prediction
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def predict_view(request):
    if request.method == "POST" and request.FILES.get("image"):
        uploaded_file = request.FILES["image"]

        # Save the file in MEDIA_ROOT
        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        file_path = fs.path(filename)

        # Run prediction
        predicted_label, conf = predict_image(file_path)
        prediction = predicted_label
        confidence = round(conf, 2)

        # Save prediction to database
        Prediction.objects.create(
            user=request.user,
            plant_name=uploaded_file.name.split('.')[0],  
            disease=prediction,
            confidence=confidence,
            image=filename
        )

        # Correct URL for template
        image_url = settings.MEDIA_URL + filename

        return render(request, "result.html", {
            "prediction": prediction,
            "confidence": confidence,
            "image_url": image_url,
        })

    return render(request, "prediction.html")
