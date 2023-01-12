from django.shortcuts import render, redirect
from .models import Category, Photo

# Create your views here.
def gallery(request):
    
    category = request.GET.get('category')
    if category==None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name__contains=category)
    categories = Category.objects.all()
    return render(request,"photos/gallery.html",{
        "categories":categories,
        "photos":photos
    })



def viewPhoto(request,pk):
    photo = Photo.objects.get(pk=pk)
    return render(request,"photos/photo.html",{
        "photo":photo
    })




def addPhoto(request):
    categories = Category.objects.all()
    if request.method=="POST":
        data = request.POST
        image = request.FILES.get('image')
        if data['category']!='none':
            category=Category.objects.get(id=data['category'])
        elif data['category_new']!='':
            category,created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category = None
        photo = Photo.objects.create(image=image,description=data['description'],category=category)
        return redirect('gallery')
    return render(request,"photos/add.html",{
        "categories":categories
        })
        