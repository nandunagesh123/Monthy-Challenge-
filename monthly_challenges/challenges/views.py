from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse

monthly_challengess= {
    "january" : "Prepare for gate exam",
    "february" : "prepare for govt exam and barc",
    "march"  : "Learn django",
    "april" : "apply for jobs",
    "may"  : "Get a job successfully",
    "june" : "Replace the current phone",
    "july" : "buy a  ps5 and monitor",
    "august": "renew the medical insurance",
    "september":"Travel somewhere (2-3 days)",
    "october" : "start investing again stocks / sip /mf",
    "november" : "buy gifts for my friends",
    "december" : "travel again and stay fit for agastyaarkoodam trek"     
}

# Create your views here.


def index(request):
    list_items = ""
    months = list(monthly_challengess.keys())
    
    for month in months :
        capitalize_months = month.capitalize()
        month_path = reverse("monthly-challenge", args={month})
        list_items += f"<li> <a href=\"{month_path}\">{capitalize_months}</a></li>"
        
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)
        
    

def monthly_challenges_by_number(request,month):
    months = list(monthly_challengess.keys())
    
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    
    redirect_month = months[month-1]
    redirect_path = reverse("monthly-challenge",args=[redirect_month])  #challenges/january/
    return HttpResponseRedirect(redirect_path )
    

def monthly_challenges(request,month):
    try:
        challemges_text = monthly_challengess[month]
        response_data = f"<h1>{challemges_text}</h1>"
    except:
        return HttpResponseNotFound("<h1>month not supported</h1>")
     
    return HttpResponse(response_data )

