from django.shortcuts import render
from product.forms import Productform
from product.models import Productdb
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages

#modelform concept
def createproduct(request):
    if request.method=='POST':
        form = Productform(request.POST,request.FILES)
        print(form)
        if form.is_valid():
            user = form.save(commit=False)
            upload_image=request.FILES.get("pimg")   
            fs = FileSystemStorage()
            file =fs.save(upload_image.name,upload_image)
            user.pimg=file
            form.save()
            messages.success(request,"your product is created")
    form = Productform()
    return render(request,"createpro.html",{'form':form})


def readproduct(request):
    var=Productdb.objects.all()
    return render(request,"readpro.html",{'form':var})


def modifyproduct(request,id):
    #get the value inside db
    var=Productdb.objects.get(id=id)
    #post the values inside the db 
    if request.method=='POST':
        form = Productform(request.POST,request.FILES,instance=var)
        if form.is_valid():
            form.save()
            messages.success(request,"your product is created in the db without image")
    return render(request,"modifypro.html",{'form':var})

def deleteproduct(request,id):
    #get the value inside db
    var=Productdb.objects.get(id=id)
    var.delete()
    var1=Productdb.objects.all()
    return HttpResponseRedirect('/product/readp/')

'''
def modifyproduct(request,id):
    #get the value inside db
    var=Productdb.objects.get(id=id)
    #post the values inside the db 
    if request.method=='POST':
        form = Productform(request.POST,request.FILES,instance=var)
        if form.is_valid():
            user = form.save(commit=False)
            upload_image=request.FILES.get("pimg")
            if upload_image!=None:  
                fs = FileSystemStorage()
                file =fs.save(upload_image.name,upload_image)
                user.pimg=file
                form.save()
                messages.success(request,"your product is created in the db with image")
            form.save()
            messages.success(request,"your product is created in the db without image")
    return render(request,"modifypro.html",{'form':var})

'''

































'''
# Create your views here.
def createproduct(request):
    #get the data
    if request.method=='POST':
        form = Productform(request.POST,request.FILES)
        upload_image=request.FILES.get("pimg")   
        fs = FileSystemStorage()
        file =fs.save(upload_image.name,upload_image)
        pname=request.POST.get("pname")   
        pdesc=request.POST.get("pdesc")   
        pprice=request.POST.get("pprice")   
        pdiscount=request.POST.get("pdiscount")   
        var = Productdb.objects.create(pname=pname,pdesc=pdesc,pprice=pprice,pdiscount=pdiscount,pimg=file)
        messages.success(request,"your product is created in the db")
    #post the data
    form = Productform()
    return render(request,"createpro.html",{'form':form})
'''