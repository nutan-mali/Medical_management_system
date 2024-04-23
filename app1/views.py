from django.shortcuts import render, HttpResponse,redirect,get_object_or_404
from .forms import MedicineForm, ScheduleForm
from .models import Medicine,Schedule,UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
# Create your views here.


def SignupPage(request):
    if request.method=='POST':
        # Extract data from the POST request
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:
             # Create a new user and save it to the database
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        # Extract data from the POST request
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        # Authenticate the user
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            print(user)
            # Login the user and redirect to the home page (Here 'house' is the home page)
            return redirect('user_profile')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')


@login_required
def user_profile(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
        medical_history = user_profile.medical_history
    except UserProfile.DoesNotExist:
        medical_history = "No medical history found"
        user_profile = None 
    
        # Handle case where user profile doesn't exist
    username = request.user.username 
    form = MedicineForm(initial={'username': username})
    print("form")
    if request.method == 'POST': 
        print("test")
        form = MedicineForm(request.POST)
        print(request.POST)
        if form.is_valid(): 
            medicine = form.save(commit=False)
            medicine.user_profile = user_profile 
            medicine.save()
            form.save() 
            print("save")
            return redirect('medicine',medicine_id=medicine.pk)
        print("Username:", username) 
        print("not work")
    return render(request, 'medicine.html', {'medical_history': medical_history, 'form': form})


@login_required          
def medicine(request, medicine_id):
    print(f"Medicine ID: {medicine_id}")
    username = request.user.username
    print("Username in medicine view:", username)
    
    medicine = get_object_or_404(Medicine, pk=medicine_id)
    if request.method == 'POST':
        schedule_form = ScheduleForm(request.POST)
        if schedule_form.is_valid():
            schedule = schedule_form.save(commit=False)
            schedule.medicine = medicine  # Associate with the selected medicine
            schedule.save()
            return redirect('medicine_report', medicine_id=medicine.pk)
  # Redirect back to the same view
    else:
        schedule_form = ScheduleForm(initial={'medicine': medicine})

    return render(request, 'medicine_details.html', {'medicine': medicine,'username': username, 'schedule_form': schedule_form})
    # username = ""
     # return HttpResponse("save successfully")
   

@login_required
def medicine_report(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
        medicines = user_profile.medicines.all()
    except UserProfile.DoesNotExist:
        user_profile = None
        medicines = []

    medicine_data = []
    for medicine in medicines:
        schedules = Schedule.objects.filter(medicine=medicine)
        medicine_data.append({
            'medicine': medicine,
            'schedules': schedules,
        })

    