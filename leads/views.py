from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Lead,Agent
from .forms import LeadForm
# Create your views here.

def leadlist(request):
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }
    
    return render(request, "leads/leadlist.html", context)

def lead_detail(request, pk):
    lead = Lead.objects.all()
    context = {
        "lead": lead
    }
    
    return render(request, "leads/lead_detail.html", context)

def lead_create(request):
    form = LeadForm()
    if request.method == "POST":
        
        form = LeadForm(request.POST)
        if form.is_valid():
            
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            agent = Agent.objects.first()
            Lead.objects.create(
                first_name=first_name,
                last_name=last_name,
                age=age,
                agent=agent
            )
            
            return redirect("/leads")
    context = {
        "form": form
    }
    
    return render(request, "leads/lead_create.html", context)