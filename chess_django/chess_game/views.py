from django.shortcuts import render, HttpResponse
from .models import toDoItem

# Create your views here.
def chessboard(request):
    return render(request, 'chessboard.html')

def main_page(request):
    return render(request, 'main_page.html')