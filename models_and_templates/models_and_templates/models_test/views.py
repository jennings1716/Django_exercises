from django.shortcuts import render,redirect
from models_test.models import Board
# Create your views here.
def home(request):
    if request.method=='POST':
        return redirect('form')
    boards = Board.objects.all()
    return render(request,'home.html',{'boards':boards})

def form(request):
    if request.method=='POST':
        name = request.POST['name']
        description = request.POST['description']
        board = Board.objects.create(name=name,description=description)
        board.save()
        return redirect('home')
    return render(request,'form.html')