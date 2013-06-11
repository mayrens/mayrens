# Create your views here.
from django.http import HttpResponse
from OffenseManagement.ManageOffense.models import Offence_Entry, Offence_Type,\
    Location, Corrective_Period, Sub_Contractor, Site
from django.template import Context, loader
from django.core import serializers

def index(request):
    entry_list = Offence_Entry.objects.all()
    template = loader.get_template('entry/entry_list.html')
    context = Context({
        'entry_list': entry_list,
    })
    return HttpResponse(template.render(context))

def type(request):
    data = serializers.serialize("xml", Offence_Type.objects.all())
    
    template = loader.get_template('droplist-xml/admin-data.xml')
    context = Context({
        'data': data,
    })
    return HttpResponse(template.render(context))

def location(request):
    data = serializers.serialize("xml", Location.objects.all())
    
    template = loader.get_template('droplist-xml/admin-data.xml')
    context = Context({
        'data': data,
    })
    return HttpResponse(template.render(context))

def period(request):
    data = serializers.serialize("xml", Corrective_Period.objects.all())
    
    template = loader.get_template('droplist-xml/admin-data.xml')
    context = Context({
        'data': data,
    })
    return HttpResponse(template.render(context))

def sub_contractor(request):
    data = serializers.serialize("xml", Sub_Contractor.objects.all())
    
    template = loader.get_template('droplist-xml/admin-data.xml')
    context = Context({
        'data': data,
    })
    return HttpResponse(template.render(context))

def site(request):
    data = serializers.serialize("xml", Site.objects.all())
    
    template = loader.get_template('droplist-xml/admin-data.xml')
    context = Context({
        'data': data,
    })
    return HttpResponse(template.render(context))