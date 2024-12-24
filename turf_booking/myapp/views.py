from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from .forms import equipmentform, TurfForm

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
            return render(request,"adminstrator/adminhome.html")
        elif login_obj.Type=="turf":
            return render(request,"owner/turfownerhome.html")
    

class Logout(View):
    def get(self, request):
        return HttpResponse('''<script> alert('Logged out successfully'); window.location = '/' </script> ''')

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
class turfregister(View):
    def get(self,request):
        return render(request,'owner/turfregister.html')
    def post(self,request):
        form = turfregisterform(request.POST)
        if form.is_valid():
                if LoginTable.objects.filter(username=request.POST['username']).exists():
                    return HttpResponse('''<script>alert("username already exists! please choose a different one.");window.location="/"<script>''')
                Login_instance = LoginTable.objects.create_user(
                    user_type='pending',
                    username=request.POST['username'],
                    password=request.POST['password']
                )    
                reg_form = form.save(commit=False)
                reg_form.LOGIN = Login_instance
                reg_form.save()
                return HttpResponse('''<script>alert("registered successfully!");window.location="/"</script>''')




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
    

class Addturf(View):
    def get(self, request): 
        form = TurfForm()
        return render(request, 'turf/addturf.html', {'form': form})
    
    def post(self, request):
        form = TurfForm(request.POST, request.FILES)
        if form.is_valid():
            turf = form.save(commit=False)
            turf.Ownername = Userprofile.objects.get(id=request.POST.get("userid"))

            turf.save()

            # Get slots from POST data
            slots = request.POST.getlist("slots")
            for slot_time in slots:
                if slot_time.strip():  # Check for non-empty slot
                    Slot.objects.create(
                        turfid=turf,
                        timeslot=slot_time.strip()
                    )

            return HttpResponse('''<script>alert("Turf and slots added successfully.");window.location="/turfapp/view/";</script>''')

        
        return render(request, 'turf/addturf.html', {'form': form})

        
class Viewturf(View):
    def get(self, request):
        try:
            turfs =request.session['user_id']
            requests=Turf.objects.filter(Ownername=turfs)
        except Userprofile.DoesNotExist:
            return HttpResponse("Userprofile not found for the current user.", status=404)
        return render(request, 'turf/viewturf.html', {'turfs': requests})

    
class Deleteturf(View):
    def get(self, request, id):
        try:
            turf = Turf.objects.get(id=id)
            turf.delete() 
            return HttpResponse('''<script>alert("Turf deleted successfully.");window.location="/turfapp/view/";</script>''')
        except Turf.DoesNotExist:
            return render(request, 'turf/viewturf.html', {'error': 'Turf not found'})

       

class Editturf(View):
    def get(self, request, id):
        turf = Turf.objects.get(pk=id)
        form = TurfForm(instance=turf)
        return render(request, 'turf/editturf.html', {'turf': form})
    
    def post(self, request, id):
        turf = Turf.objects.get(pk=id)
        form = TurfForm(request.POST,request.FILES,  instance=turf)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("Turf Edited successfully.");window.location="/turfapp/view/";</script>''')
        return render(request, 'turf/editturf.html', {'turf': form})
    