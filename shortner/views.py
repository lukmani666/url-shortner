from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Url

import string, random


def gen_rand():
    return "".join(random.choices(string.ascii_uppercase + string.digits, k=8))

def index(req):
    # print(gen_rand())
    if req.method == "POST":
        url = Url.objects.create(url=req.POST.get("url"), code=gen_rand())
        # return redirect(reverse("shortner", kwargs={"code": url.code}))
        short = req.META.get("HTTP_REFERER")
        return render(req, "shortner/index.html", {"url": url, "short": f"{short}{url.code}"})
    return render(req, "shortner/index.html")

def shortner(req, code):
    url = get_object_or_404(Url, code=code)
    return redirect(url.url)