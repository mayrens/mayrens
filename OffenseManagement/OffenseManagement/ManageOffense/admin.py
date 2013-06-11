##from OffenseManagement.ManageOffense.models import *
from django.contrib import admin
from models import *

class OffenceManagementAdmin(admin.ModelAdmin):
    exclude = ('version', 'user',)

class OffenceTypeAdmin(OffenceManagementAdmin):
    def queryset(self, request):
        qs = super(OffenceTypeAdmin, self).queryset(request)
        
        if request.user.is_superuser:
            return qs
        
        return qs.filter(user=request.user.id)
    
    def save_model(self, request, obj, form, change):
        obj.user = request.user.id
        super(OffenceTypeAdmin, self).save_model(request, obj, form, change)
    
class CorrectivePeriodAdmin(OffenceManagementAdmin):
    def queryset(self, request):
        qs = super(CorrectivePeriodAdmin, self).queryset(request)
        
        if request.user.is_superuser:
            return qs
        
        return qs.filter(user=request.user.id)
    
    def save_model(self, request, obj, form, change):
        obj.user = request.user.id
        super(CorrectivePeriodAdmin, self).save_model(request, obj, form, change)
    
class LocationAdmin(OffenceManagementAdmin):
    def queryset(self, request):
        qs = super(LocationAdmin, self).queryset(request)
        
        if request.user.is_superuser:
            return qs
        
        return qs.filter(user=request.user.id)
    
    def save_model(self, request, obj, form, change):
        obj.user = request.user.id
        super(LocationAdmin, self).save_model(request, obj, form, change)
    
class SubContractorAdmin(OffenceManagementAdmin):   
    def queryset(self, request):
        qs = super(SubContractorAdmin, self).queryset(request)
        
        if request.user.is_superuser:
            return qs
        
        return qs.filter(user=request.user.id)
    
    def save_model(self, request, obj, form, change):
        obj.user = request.user.id
        super(SubContractorAdmin, self).save_model(request, obj, form, change)
    
class SiteAdmin(OffenceManagementAdmin):
    def queryset(self, request):
        qs = super(SiteAdmin, self).queryset(request)
        
        if request.user.is_superuser:
            return qs
        
        return qs.filter(user=request.user.id)
    
    def save_model(self, request, obj, form, change):
        obj.user = request.user.id
        super(SiteAdmin, self).save_model(request, obj, form, change)

admin.site.register(Offence_Type, OffenceTypeAdmin)
admin.site.register(Corrective_Period, CorrectivePeriodAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Sub_Contractor, SubContractorAdmin)
admin.site.register(Site, SiteAdmin)