from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from .forms import equipmentform

from .models import *

# Create your views here.

class Login(View):
    def get(self, request):
        return render(request, 'login.html')
    
class viewlogin(View):
    def get(self,request):
        return render(request,'login.html')
    def post(self,request):
        username=request.POST['username']
        password=request.POST['password']
        login_obj=LoginTable.objects.get(username=username, password=password)
        if login_obj.Type=="admin":
            return render(request,"owner/adminhome.html")
        elif login_obj.Type=="turf":
            return render(request,"owner/turfownerhome.html")
    

# /////////////////////////////////// ADMIN /////////////////////////////////////    




class Turfowners(View):
    def get(self,request):
        obg=turf.objects.all()
        return render(request,'adminstrator/verify_turfowners.html',{'obg':obg})
class accept_turf(View):
    def get(self,request,t_id):
        obg=LoginTable.objects.get(id=t_id)
        obg.Type='turf'
        obg.save()
        return redirect('turfowner')
class reject_turf(View):
      def get(self,request,t_id):
        obg=LoginTable.objects.get(id=t_id)
        obg.Type='reject'
        obg.save()
        return redirect('turfowner')



class Complaints(View):
    def get(self,request):
        obg=ComplaintTable.objects.all()
        return render(request,'adminstrator/viewcomplaints.html',{'obg':obg})

class reply(View):
    def  get(self,request, c_id):
         return render(request,'adminstrator/reply.html')
    def post(self,request,c_id):
        reply=request.POST['reply']
        obj=ComplaintTable.objects.get(id=c_id)
        obj.reply=reply
        obj.save()
        return redirect('complaints')
class Users(View):
    def get(self,request):
        obg=UserTable.objects.all()
        return render(request,'adminstrator/viewusers.html',{'obg':obg})
    
class viewequipment(View):
    def get(self,request):
        obg=EquipmentTable.objects.all()
        return render (request,'adminstrator/viewequipments.html',{'obg':obg})
    
# ////////////////////////////////////// owner ////////////////////////////////////////////

class Addmanagment(View):
    def get(self,request):
        return render(request,'owner/add_manage.html')


class turfownerhome(View):
    def get(self,request):
        return render(request,'owner/turfownerhome.html')

        
class Viewbooking(View):
    def get(self,request):
        obg=bookingtable.objects.all()
        return render(request,'owner/viewbooking.html',{'obg':obg})

class turf_complaint(View):
    def get(self,request):
        obg=ComplaintTable.objects.all()
        return render(request,'owner/viewcomplaints.html',{'obg':obg})


class Viewfeedback(View):
    def get(self,request):
        obg=FeedbackTable.objects.all()
        return render(request,'owner/viewfeedback.html')  
          

class Adminhome(View):
     def get(self,request):
         return render(request,'adminstrator/adminhome.html')

            
class addequipment(View):
    def get (self,request):
        return render(request,'owner/addequipment.html')
    def post(self,request):
       
        form=equipmentform(request.POST)
        if form.is_valid():
            print("hhhhh")
            form.save()
            print("hvhghgf")
            return HttpResponse('''<script>alert("equipment added successfully");window.location="/manageequips/"</script>''')

class editequipment(View):
    def get(self,request,id):
        obg=EquipmentTable.objects.get(id=id)
        return render(request,'owner/editequipment.html',{'obg':obg})
    def post(self,request,id):
        obg=EquipmentTable.objects.get(id=id)
        form=equipmentform(request.POST,instance=obg)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("equipment updated successfully");window.location="/manageequips"</script>''')


class manageequips(View):
    def get(self,request)     :
        obg=EquipmentTable.objects.all()         
        return render(request,'owner/manageequips.html',{'obg':obg})
        

class deleteequipment(View):
    def get(self,request,id):
        obg=EquipmentTable.objects.get(id=id)
        obg.delete()
        return HttpResponse('''<script>alert("equipment deleted successfully");window.location="/manageequips"</script>''')
