from inv_app.models import Person, Item, Monitor, Phone, Network, Printer, ItemForm, PersonForm, MonitorForm, NetworkForm, PrinterForm, PhoneForm 
from django.shortcuts import get_object_or_404, render
from django.template import Context, loader
from django.http import HttpResponseRedirect, HttpResponse


def home(request):
	comps = Item.objects.all()
	moni = Monitor.objects.all()
	phones = Phone.objects.all()
	nets = Network.objects.all()
	prints = Printer.objects.all() 
	context = Context({
		'comps': comps,
		'moni': moni,
		'phones': phones,
		'nets': nets,
		'prints': prints
		})
	return render(request, 'inv_app/home.html', context)

def add(request):
    if request.method == 'POST': 
        form = ItemForm(request.POST)
        if form.is_valid(): 
            form.save()
            return HttpResponseRedirect('/add/') # Redirect after POST
    else:
        form = ItemForm() # An unbound form

    return render(request, 'inv_app/additem.html', {
        'form': form,
    })

def add_person(request):
    if request.method == 'POST': 
        person_form = PersonForm(request.POST)
        if person_form.is_valid(): 
            person_form.save()
            return HttpResponseRedirect('') # Redirect after POST
    else:
        person_form = PersonForm() # An unbound form

    return render(request, 'inv_app/additem.html', {
        'form': person_form,
    })

def add_monitor(request):
    if request.method == 'POST': 
        monitor_form = MonitorForm(request.POST)
        if monitor_form.is_valid(): 
            monitor_form.save()
            return HttpResponseRedirect('') # Redirect after POST
    else:
        monitor_form = MonitorForm() # An unbound form

    return render(request, 'inv_app/additem.html', {
        'form': monitor_form,
    })

def add_phone(request):
    if request.method == 'POST': 
        phone_form = PhoneForm(request.POST)
        if phone_form.is_valid(): 
            phone_form.save()
            return HttpResponseRedirect('') # Redirect after POST
    else:
        phone_form = PhoneForm() # An unbound form

    return render(request, 'inv_app/additem.html', {
        'form': phone_form,
    })

def add_printer(request):
    if request.method == 'POST': 
        printer_form = PrinterForm(request.POST)
        if printer_form.is_valid(): 
            printer_form.save()
            return HttpResponseRedirect('') # Redirect after POST
    else:
        printer_form = PrinterForm() # An unbound form

    return render(request, 'inv_app/additem.html', {
        'form': printer_form,
    })

def add_network(request):
    if request.method == 'POST': 
        network_form = NetworkForm(request.POST)
        if network_form.is_valid(): 
            network_form.save()
            return HttpResponseRedirect('') # Redirect after POST
    else:
        network_form = NetworkForm() # An unbound form

    return render(request, 'inv_app/additem.html', {
        'form': network_form,
    })

def edit(request, id):
    instance = get_object_or_404(Item, id=id)
    form = ItemForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')   
    return render(request, 'inv_app/additem.html', {'form': form})

def edit_person(request, id):
    instance = get_object_or_404(Person, id=id)
    form = PersonForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')   
    return render(request, 'inv_app/additem.html', {'form': form})

def edit_monitor(request, id):
    instance = get_object_or_404(Monitor, id=id)
    form = MonitorForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')   
    return render(request, 'inv_app/additem.html', {'form': form})

def edit_phone(request, id):
    instance = get_object_or_404(Phone, id=id)
    form = PhoneForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')   
    return render(request, 'inv_app/additem.html', {'form': form})

def edit_printer(request, id):
    instance = get_object_or_404(Printer, id=id)
    form = PrinterForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')   
    return render(request, 'inv_app/additem.html', {'form': form})

def edit_network(request, id):
    instance = get_object_or_404(Printer, id=id)
    form = NetworkForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')   
    return render(request, 'inv_app/additem.html', {'form': form})