from django.shortcuts import render

# Create your views here.

def index(request):
    
    context = {
        "course_list" : ["Django", "python", "DSA", "Machine Learning", "Java"],

        "student": [{"Name": "Namling Limbu", "Course":"Django"}, {"Name": "Ganga", "Course":"Machine Learning"} ]
    }

    return render(request, "index.html", context)