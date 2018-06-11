from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "page/home.html")
def education(request):
    return render(request, "page/education.html")
def school_diploma(request):
    return render(request, "page/second/school.html")
def AIT_diploma(request):
    return render(request, "page/second/AIT.html")
def DonNTU_diploma(request):
    return render(request, "page/second/DonNTU.html")
def license(request):
    image_data = open("C:/Users/platan/Desktop/proskurenko/page/static/images/aspirantura.jpg", "rb").read()
    return HttpResponse(image_data, content_type="image/jpg")
def teacher_license(request):
	return render(request, "page/second/teacher.html")
def experience(request):
	return render(request, "page/experience.html")
def book1(request):
	return render(request, "page/second/book.html")
def book2(request):
	return render(request, "page/second/book2.html")
def book3(request):
	return render(request, "page/second/book3.html")
def book4(request):
	return render(request, "page/second/book4.html")
def publication(request):
    return render(request, "page/publication.html")
def characteristic(request):
    return render(request, "page/characteristic.html")
def vlog(request):
    return render(request, "page/vlog.html")
def projects(request):
    return render(request, "page/projects.html")
# Create your views here.
