from django.shortcuts import render, redirect
from blogs.models import Blogs
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from category.models import Category
from django.core.files.storage import FileSystemStorage
from django.contrib import messages

# Create your views here.
@login_required(login_url="member")
def panel(request):
    writer = auth.get_user(request)
    blogs = Blogs.objects.filter(writer=writer)
    blogCount = blogs.count()
    total = Blogs.objects.filter(writer=writer).aggregate(Sum("views"))
    return render(request, "backend/index.html", { "blogs": blogs, "writer": writer, "blogCount": blogCount, "total": total })

# fill article by a writer
@login_required(login_url="member")
def displayForm(request):
    writer = auth.get_user(request)
    blogs = Blogs.objects.filter(writer=writer)
    blogCount = blogs.count()
    total = Blogs.objects.filter(writer=writer).aggregate(Sum("views"))
    categories = Category.objects.all()
    return render(request, "backend/blogForm.html", { "blogs": blogs, "writer": writer, "blogCount": blogCount, "total": total, "categories": categories })

@login_required(login_url="member")
def insertData(request):
    try:
        if request.method == "POST" and request.FILES["image"]:
            datafile = request.FILES["image"]
            # retrieve form data 
            name = request.POST["name"]
            category = request.POST["category"]
            description = request.POST["description"]
            content = request.POST["content"]
            writer = auth.get_user(request)

            # check content type of the file, requires image only
            if str(datafile.content_type).startswith("image"):
                # upload file
                fs = FileSystemStorage()
                img_url = "blogImages/" + datafile.name
                filename = fs.save(img_url, datafile)
                # record data into DB
                blog = Blogs(name=name, category_id=category, description=description, content=content, writer=writer, image=img_url)
                blog.save()
                messages.info(request, "Sucessfully upload image!")
                return redirect("displayForm")
            else:
                messages.info(request, "Not available type of file, please upload image again")
                return redirect("displayForm")
    except:
        return redirect("displayForm")

@login_required(login_url="member")        
def deleteData(request, id):
    try:
        blog = Blogs.objects.get(id=id)
        fs = FileSystemStorage()
        fs.delete(str(blog.image)) # delete cover image
        blog.delete() # delete from database
        return redirect("panel")
    except:
        return redirect("panel")

@login_required(login_url="member")
def editData(request, id):
    # Common information of the blog's 
    writer = auth.get_user(request)
    blogs = Blogs.objects.filter(writer=writer)
    blogCount = blogs.count()
    total = Blogs.objects.filter(writer=writer).aggregate(Sum("views"))
    categories = Category.objects.all()

    blogEdit = Blogs.objects.get(id=id)
    return render(request, "backend/editForm.html", {"blogEdit": blogEdit, "writer": writer, "blogCount": blogCount, "total": total, "categories": categories })

@login_required(login_url="member")
def updateData(request, id):    
    try:
        if request.method == "POST":
            # retrieve the original information for editing
            blog = Blogs.objects.get(id=id)
            # retrieve form data 
            name = request.POST["name"]
            category = request.POST["category"]
            description = request.POST["description"]
            content = request.POST["content"]

            # Update information
            blog.name = name
            blog.category_id = category # must be a unique id of target blog
            blog.description = description
            blog.content = content
            blog.save() # save the latest infomation to DB
            messages.info(request, "Successfully update!")

            # Update the cover image of blog
            if request.FILES["image"]:
                datafile = request.FILES["image"]
                if str(datafile.content_type).startswith("image"):
                    # delete old image from blogImages folder
                    fs = FileSystemStorage()
                    fs.delete(str(blog.image))

                    # replace a new image
                    img_url = "blogImages/"+ datafile.name
                    filename = fs.save(img_url, datafile)
                    blog.image = img_url
                    blog.save()
            return redirect("panel")
    except:
        return redirect("panel")