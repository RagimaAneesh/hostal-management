from django.urls import path
from newapp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('hom', views.hom, name='hom'),
    path('ad', views.admindash, name='ad'),
    # path('log', views.log, name='log'),
    path('home_log',views.home_log,name='home_log'),
    path('student',views.student,name='student'),
    path('studentregister',views.student_register,name='studentregister'),
    path('parent_home', views.parent, name='parent_home'),
    path('parentregister',views.parent_register,name='parentregister'),
    path('parentv',views.parent_view,name='parentv'),
    path('parentd/<int:id>/',views.parent_delete,name='parentd'),
    path('studentv',views.student_view,name='studentv'),
    path('studentu/<int:id>/',views.student_update,name='studentu'),
    path('studentd/<int:id>/', views.student_delete, name='studentd'),
    path('food',views.food_details,name='food'),
    path('fdv',views.food_view,name='fdv'),
    path('fdd/<int:id>/', views.food_delete, name='fdd'),
    path('fe',views.fee_details,name='fe'),
    path('notification',views.notification,name='notification'),
    path('notificationview',views.view_notification,name='notificationview'),
    path('complain',views.complaints,name='complain'),
    path('complainv',views.view_complaints,name='complainv'),
    path('student_complaint',views.student_complaint,name='student_complaint'),
    path('reply/<int:id>/',views.reply_complaint,name='reply'),
    path('feedback',views.feed_back,name='feedback'),
    path('feedbackv',views.view_feedback,name='feedbackv'),
    path('attend',views.Attendenc,name='attend'),
    path('attendmark/<int:user_id>/',views.mark,name='attendmark')

]