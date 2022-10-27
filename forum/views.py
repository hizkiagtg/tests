from django.shortcuts import render

# Create your views here.
def show_forum(request):
    return render(request, "forum")
