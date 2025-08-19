from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from prediction.models import Prediction

@login_required
def dashboard(request):
    predictions = Prediction.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "dashboard.html",{"predictions":predictions})