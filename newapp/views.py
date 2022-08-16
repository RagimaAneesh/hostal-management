import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


# Admin
from newapp.forms import LoginRegister, StudentForm, ParentForm, FoodForm, FeeForm, NotificationForm, ComplaintForm,FeedbackForm
from newapp.models import Parent, Student, Food, Notification, Studentcomplaint, Feedback, Attendence


def home(request):
    return render(request,'Modified_files/homepage.html')
def hom(request):
    return render(request,'admin/hom.html')
def admindash(request):
    return render(request,'Modified_files/dashtheme.html')
# def log(request):
#     return render(request,'Modified_files/login.html')

def home_log(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('ad')
            if user.is_student:
                return redirect('student')
            if user.is_parent:
                return redirect('parent')
            else:
                messages.info(request, 'invallid')

    return render(request, 'Modified_files/login.html')

def student(request):
    return render(request,'student/studentdash.html')


def student_register(request):
    form1 = LoginRegister()
    form2 = StudentForm()
    if request.method == "POST":
        form1 = LoginRegister(request.POST)
        form2 = StudentForm(request.POST,request.FILES)
        if form1.is_valid() and form2.is_valid() :
            user = form1.save(commit=False)
            user.is_student = True
            user.save()
            user1 =form2.save(commit=False)
            user1.user = user
            user1.save()
            return redirect('student')

    return render(request,'student/studentregister.html',{"form1":form1,"form2":form2})

def parent(request):
    return render(request,'parent/parentdash.html')

def parent_register(request):
    form1 = LoginRegister()
    form2 = ParentForm()
    if request.method == 'POST':
        form1 = LoginRegister(request.POST)
        form2 = ParentForm(request.POST,request.FILES)
        if form1.is_valid() and form2.is_valid():
            user = form1.save(commit=False)
            user.is_parent = True
            user.save()
            user1 =form2.save(commit=False)
            user1.user = user
            user1.save()
            return redirect('parent_home')

    return render(request,'parent/parentregi.html',{"form1":form1,"form2":form2})

def parent_view(request):
    data = Parent.objects.all()
    return  render(request,'admin/parentview.html',{"data":data})

def parent_delete(request,id):
    n = Parent.objects.get(id=id).delete()
    return redirect('parentv')

def student_view(request):
    data = Student.objects.all()
    return  render(request,'admin/studentview.html',{"data":data})

def student_update(request,id):
    n = Student.objects.get(id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST,instance = n)
        if form.is_valid():
            form.save()
            return redirect('studentv')
    else:
            form = StudentForm(instance=n)
    return render(request,'admin/updatestudent.html',{"form":form})

def student_delete(request,id):
    n = Student.objects.get(id=id).delete()
    return redirect('studentv')

def food_details(request):
    form = FoodForm
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ad')
    return render(request, 'admin/food.html', {"form":form})


def food_view(request):
    data = Food.objects.all()
    return render(request, 'admin/foodview.html', {"data": data})

def food_delete(request,id):
    n = Food.objects.get(id=id).delete()
    return redirect('fdv')

def fee_details(request):
    form = FeeForm
    if request.method == 'POST':
        form = FeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ad')
    return render(request, 'admin/fee.html', {"form":form})

def notification(request):
    form =NotificationForm
    if request.method =='POST':
        form = NotificationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,'notification sending successfully')
            return redirect('ad')
    return render(request,'admin/notification.html', {"form": form})

def view_notification(request):
    data = Notification.objects.all()
    return render(request,'admin/notificationview.html', {"data": data})

def complaints(request):
    form = ComplaintForm
    u=request.user
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user = u
            obj.save()
            messages.info(request, 'notification sending successfully')
            return redirect('ad')
    else:
        form = ComplaintForm()
    return render(request,'admin/studentcomplaint.html', {"form": form})

def view_complaints(request):
    data = Studentcomplaint.objects.all()
    return render(request,'admin/complaintview.html', {"data": data})

def student_complaint(request):
    data = Studentcomplaint.objects.all()
    return render(request,'admin/studentcomplain.html', {"data": data})

def reply_complaint(request,id):
    complaint = Studentcomplaint.objects.get(id=id)
    if request.method =="POST":
       r=request.POST.get('reply')
       complaint.reply = r
       complaint.save()
       messages.info(request,'Reply send for the complaint')
       return redirect('student_complaint')
    return render(request,'admin/reply.html', {"complaint":complaint})

def feed_back(request):
    form =  FeedbackForm
    u = request.user
    if request.method == 'POST':
        form =  FeedbackForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = u
            obj.save()
            messages.info(request, 'notification sending successfully')
            return redirect('ad')
    else:
        form = FeedbackForm()
    return render(request, 'admin/feedback.html', {"form": form})

def view_feedback(request):
    data = Feedback.objects.all()
    return render(request,'admin/viewfeedback.html', {"data": data})

def Attendenc(request):
    stud= Student.objects.all()
    print(student)
    return render(request,'admin/attendence.html',{"stud":stud})

now = datetime.datetime.now()
def mark(request, user_id):
    user = Student.objects.get(user_id=user_id)
    print("hello")
    print(user)
    att =Attendence.objects.filter(student=user,date=datetime.date.today())
    # att = Attendence.objects.get(student=user)

    print("hii")
    print(att)
    if att.exists():
        messages.info(request,"Today's attendance already marked this student")
        return redirect('ad')
    else:
        if request.method =='POST':
            attendc =request.POST.get('attendence')
            Attendence(student=user,date= datetime.date.today(),attendence=attendc.time,time=now.time()).save()
            messages.info(request,"Attendence Added Successfully")
            return redirect('ad')
    return render(request,'admin/markattendence.html')








