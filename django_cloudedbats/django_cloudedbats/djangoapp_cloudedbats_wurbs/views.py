from django.shortcuts import render

def list_wurbs(request):
    """ """
    return render(request, "cloudedbats_wurbs.html", {})

