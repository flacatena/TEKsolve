from django.shortcuts import render, get_object_or_404 , redirect
from . models import Hardware, Software, Issue, Resolution
from django.http import Http404 , HttpResponseRedirect
from django.views.decorators.cache import cache_control
from . forms import IssueForm, ResolutionForm
from django.db.models import Q
from django import forms

# Display list of hardware to troubleshoot
def hardware_list(request):
    hardware_devices = Hardware.objects.all()
    return render(request, 'resolve_hardware.html',{'hardware_devices': hardware_devices})

# Display list of software to troubleshoot
def software_list(request):
    software_products = Software.objects.all()
    return render(request, 'resolve_software.html',{'software_products': software_products})

# Displays list of issues associated with a selected hardware
def hardware_issues(request,id):
    try:
        hardware_devices = Hardware.objects.get(id=id)
        issues_list = Issue.objects.filter(hardware=id)
    except Hardware.DoesNotExist:
        raise Http404("No Hardware found!")
    return render(request, 'show_hardware_issues.html',{'hardware_devices': hardware_devices, 'issues_list': issues_list})

# Displays lisf of software issues associated with a selected hardware
def software_issues(request,id):
    try:
        software_products = Software.objects.get(id=id)
        issues_list = Issue.objects.filter(software=id)
    except Software.DoesNotExist:
        raise Http404("No Software found!")
    return render(request,'show_software_issues.html',{'software_products': software_products, 'issues_list': issues_list})

# Displays specific hardware resolution to a selected hardware issue
def show_hardware_resolution(request,id): #receiving the issue with this id
    try:
        issue_selected = Issue.objects.get(id=id)
        resolution_to_issue = issue_selected.resolutions.reported_resolution
        hardware_selected = issue_selected.hardware_id
        return render(request,  'show_hardware_resolution.html',{'issue_selected': issue_selected, 'resolution_to_issue': resolution_to_issue, 'hardware_selected':hardware_selected})
    
    except Resolution.DoesNotExist: # except Issue.DoesNotExist:
        issue_selected =  Issue.objects.get(id=id)
        hardware_selected = issue_selected.hardware_id
        return render(request, 'show_hardware_resolution.html',{'issue_selected': issue_selected, 'hardware_selected': hardware_selected})
    
# Displays specific software resolution to a selected software issue    
def show_software_resolution(request,id):
    try:
        issue_selected = Issue.objects.get(id=id)
        resolution_to_issue = issue_selected.resolutions.reported_resolution
        software_selected = issue_selected.software_id
        return render(request, 'show_software_resolution.html',{'issue_selected': issue_selected, 'resolution_to_issue' : resolution_to_issue, 'software_selected':software_selected})
    
    except Resolution.DoesNotExist:
        issue_selected = Issue.objects.get(id=id)
        software_selected = issue_selected.software_id
        return render(request, 'show_software_resolution.html',{'issue_selected': issue_selected, 'software_selected': software_selected})
    
# Displays form to selected either software or hardware followed by the issue
@cache_control(no_store=True)
def enter_new_issue(request):
    hardware_exist = Hardware.objects.all()
    software_exist = Software.objects.all()
    if(software_exist or hardware_exist):
        if request.method == "POST":
            form = IssueForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/solvecenter")
            else:
                print(form.errors)
        else:
            form = IssueForm()
            #form.fields['hardware'].widget.attrs.update({'autofocus':True})
            #context = {"form":form}
        return render(request, "enter_new_issue.html",{'form':form, 'hardware_exist': hardware_exist, 'software_exist': software_exist})
    else:
        message = "No Hardware or Software exist in system, please enter Hardware or Software."
        return render(request,"base.html",{'message': message})
    
# Displays a form to enter a new resolution to an existing hardware of sofware issue
@cache_control(no_store=True)
def enter_new_resolution(request,id):#receiving issue object id
    parent_obj = get_object_or_404(Issue, id=id)
    try:
        child_obj = parent_obj.resolutions
    except Resolution.DoesNotExist:
        child_obj = None
    
    if request.method == 'POST':
        # Bind the POST data to the EXACT objects fetched above
        form1 = IssueForm(request.POST, instance=parent_obj)
        form2 = ResolutionForm(request.POST, instance=child_obj)

        if form1.is_valid() and form2.is_valid():  
            # Save the parent first to commit any changes
            saved_parent = form1.save()
            
            # Use commit=False to modify relationship data securely
            child_instance = form2.save(commit=False)
            
            # ENFORCE: Ensure form 2 belongs strictly to this parent object
            child_instance.issue = saved_parent 
            child_instance.save()

            return redirect('/solvecenter')
    else:
        form1 = IssueForm(instance=parent_obj) 
        form2 = ResolutionForm(instance=child_obj)
        fields_hide=['hardware','software','reported_issue','issue_pic']
        for field in fields_hide:
            form1.fields[field].widget = forms.HiddenInput() 
    return render(request, 'enter_new_resolution.html', {'form1': form1, 'form2': form2, 'issue': child_obj})

#Displays a list of issues that do not have a resolution for the purpose of selecting issue to assign a resolution
def display_issues_without_res(request):
    all_issues = Issue.objects.filter(Q(resolutions__reported_resolution__isnull = True)|(Q(resolutions__reported_resolution = "")))
    return render(request, "display_issues_without_res.html",{ 'all_issues': all_issues})







