import json
from django.shortcuts import render
from django.conf import settings


def index(request):
    family_data = json.load(open(settings.BASE_DIR / "data.json"))
    context = {
        "data":family_data["members"]
    }
    return render(request, "base.html", context)