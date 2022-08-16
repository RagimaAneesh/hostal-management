from django import forms
from django.contrib.auth.forms import UserCreationForm

from newapp.models import Login, Student, Parent, Food, Fee, Notification, Studentcomplaint, Feedback, Attendence


class LoginRegister(UserCreationForm):
    class Meta:
        model = Login
        fields = ('username','password1','password2')

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = "__all__"
        exclude = ("user",)

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class ParentForm(forms.ModelForm):

    class Meta:
        model = Parent
        fields = "__all__"
        exclude = ("user",)

class FoodForm(forms.ModelForm):

    class Meta:
        model = Food
        fields = "__all__"
        exclude = ("user",)

class FeeForm(forms.ModelForm):

    class Meta:
        model = Fee
        fields = "__all__"
        exclude = ("user",)

class NotificationForm(forms.ModelForm):

    class Meta:
        model = Notification
        fields = ("notification",)

class ComplaintForm(forms.ModelForm):

    class Meta:
        model = Studentcomplaint
        fields = ("complaint",)

class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        fields = ("feedback",)

class AttendenceForm(forms.ModelForm):

    class Meta:
        model = Attendence
        fields = ("attendence",)


# class HostalForm(forms.ModelForm):
#
#     class Meta:
#         model = Attendence
#         fields = (" Details",)




