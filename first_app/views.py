from django.shortcuts import render
import datetime

# Create your views here.
def home(request):
    d =  {"author":"mahim","age":15,"list":['django','is','best'],"birthday":datetime.datetime.now(),"val":"I'm Mahim", 'times':datetime.datetime.now(),"courses":[
        {
            'id': 1,
            "name":"python",
            "fee":5000
        },
        {
            'id': 2,
            "name":"Djange",
            "fee": 6500
        },
        {
            'id': 3,
            "name":"C",
            "fee": 8800
        }
    ]}
    return render(request,'home.html',d)
def contact(request):
    return render(request,'Contact.html')
def about(request):
    return render(request,'About.html')