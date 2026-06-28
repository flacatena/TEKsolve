from django.shortcuts import render
from . models import Hardware, Software, Issue, Resolution
from django.http import Http404 , HttpResponseRedirect

def hardware_list(request):
    hardware_devices = Hardware.objects.all()
    return render(request, 'resolve_hardware.html',{'hardware_devices': hardware_devices})

def software_list(request):
    software_products = Software.objects.all()
    return render(request, 'resolve_software.html',{'software_products': software_products})

def hardware_issues(request,id):
    try:
        hardware_devices = Hardware.objects.get(id=id)
        issues_list = Issue.objects.filter(hardware=id)
    except Hardware.DoesNotExist:
        raise Http404("No Hardware found!")
    return render(request, 'show_hardware_issues.html',{'hardware_devices': hardware_devices, 'issues_list': issues_list})

def software_issues(request,id):
    try:
        software_products = Software.objects.get(id=id)
        issues_list = Issue.objects.filter(software=id)
    except Software.DoesNotExist:
        raise Http404("No Software found!")
    return render(request,'show_software_issues.html',{'software_products': software_products, 'issues_list': issues_list})

def show_hardware_resolution(request,id):
    try:
        resolution_steps = Resolution.objects.get(id=id)
        return render(request, 'show_hardware_resolution.html',{'resolution_steps': resolution_steps})

    except Resolution.DoesNotExist:
        resolution_steps =  Issue.objects.get(id=id)
        hardware_id = resolution_steps.hardware_id
        return render(request, 'show_hardware_resolution.html',{'resolution_steps': resolution_steps, 'hardware_id': hardware_id})


def show_software_resolution(request,id):
    try:
        resolution_steps = Resolution.objects.get(id=id)
        return render(request, 'show_software_resolution.hmtl',{'resolution_steps': resolution_steps})
    
    except Resolution.DoesNotExist:
        resolution_steps = Issue.objects.get(id=id)
        software_id = resolution_steps.software_id
        return render(request, 'show_software_resolution.html',{'resolution_steps': resolution_steps, 'software_id': software_id})


# Create your views here.python

