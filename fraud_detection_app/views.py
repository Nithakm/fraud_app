from django.shortcuts import render
from django.views import View

# Create your views here.


class UserLoginView(View):
    def get(self,request,*args,**kwargs):
        return render(request, 'user_login.html')
    
class UserRegisterView(View):
    def get(self,request,*args,**kwargs):
        return render(request, 'user_register.html')
    
class AdminDashboardView(View):
    def get(self,request,*args,**kwargs):
        return render(request, 'admin_dashboard.html')
    
class AdminLoginView(View):
    def get(self,request,*args,**kwargs):
        return render(request, 'admin_login.html')
    
class UserManagmentView(View):
    def get(self,request,*args,**kwargs):
        return render(request, 'user_managment.html')
    
class ApplicationView(View):
    def get(self,request,*args,**kwargs):
        return render(request, 'application.html')
    
class ActivitiesView(View):
    def get(self,request,*args,**kwargs):
        return render(request, 'activities.html')
    
class UserDashboardView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'user_dashboard.html')

class ScanAppView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'scan_app.html')
    
class ScanningView(View):
     def get(self,request,*args,**kwargs):
        return render(request,'scanning.html')
     
class ResultView(View):
     def get(self,request,*args,**kwargs):
        return render(request,'result.html')
    