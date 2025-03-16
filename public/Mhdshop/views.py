from django.shortcuts import render,redirect



from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def header(request):
    return render(request, 'header.html')


def footer(request):
    return render(request, 'footer.html')



def  Carpet_tiles(request):
    return render(request, 'Carpet_tiles.html')

def  Interior_decoration(request):
    return render(request, 'Interior_decoration.html')

def  furniture(request):
    return render(request, 'furniture.html')

def  spc(request):
    return render(request, 'spc.html')

def  Lvt(request):
    return render(request, 'Lvt.html')

def Vinylsheetfloor(request):
    return render(request, 'Vinylsheetfloor.html')

def  Blinds(request):
    return render(request, 'Blinds.html')

def wallTowall(request):
    return render(request, 'wallTowall.html')

