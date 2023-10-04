from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from hospitals import views
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls.static import static
from .pres_pdf import prescription_pdf

# IMPORTANT WARNING ::-- chat feature of the app is working fine 
# right now i am commenting the payment code because i will set this up later

urlpatterns = [
    path('', views.home_hospitals, name='home_hospitals'),
    # This function is for searching the hospitals in list
    path('search/', views.search, name='search'),
    # This one is for the password change
    # this is working for /2 but not for the /1 or anything, and also working for /6 and /7
    path('change-password/<int:pk>', views.change_password, name='change-password'),
    # path('add-billing/', views.add_billing, name='add-billing'),
    # the appointments error is due to the format required in appointments
    # and the format is http://127.0.0.1:8000/admin/doctor/appointment/add/
    path('appointments/', views.appointments, name='appointments'),
    # path('edit-billing/', views.edit_billing, name='edit-billing'),
    path('edit-prescription/', views.edit_prescription, name='edit-prescription'),
    # path('forgot-password/', views.forgot_password,name='forgot-password'),
    path('patient-dashboard/',views.patient_dashboard, name='patient-dashboard'),
    path('privacy-policy/', views.privacy_policy, name='privacy-policy'),
    
    # this profile settings is some showing some absurd data, with search functionality
    # ok i have figured this out, this also needs first login to access various things 
    # about the profile settings of the user
    
    path('profile-settings/',views.profile_settings, name='profile-settings'),
    path('about-us/', views.about_us, name='about-us'),
    
    # the patient register is for the patient registering account.
    path('patient-register/', views.patient_register, name='patient-register'),
    
    # the logout has some problem with directly accessing it 
    path('logout/', views.logoutUser, name='logout'),
    
    # this multiple hospital needs the user to first login as patient
    # same method can be used in the logout to prevent the error
    
    path('multiple-hospital/', views.multiple_hospital, name='multiple-hospital'),
    # this chat feature needs the user to first login as patient
    path('chat/<int:pk>/', views.chat, name='chat'),
    
    # this chat-doctor is giving some error, need to check its functionality
    # maybe it is same as the chat feature above
    # now this is working fine, i corrected this in the original function
    # path('chat-doctor/', views.chat_doctor, name='chat-doctor'),
    
    # this is for the particular hospital profile 
    path('hospital-profile/<int:pk>/', views.hospital_profile, name='hospital-profile'),
    
    # path('checkout-payment/', views.checkout_payment, name='checkout-payment'),
    
    # this shop is just a redirect to the pharmacy/shop/
    path('shop/', views.pharmacy_shop, name='pharmacy_shop'),
    
    # This is just a test data table which is just their for example as per my opinion
    # path('data-table/', views.data_table, name='data-table'),
    
    # This testing/ is probably to test if views are working fine or not
    # path('testing/',views.testing, name='testing')
    
    # this is department list, like cardiology
    # first go to hospital then to the department and doctor list, and then you got 
    # the departments from department you can select the doctors from same hosp and depart
    path('hospital-department-list/<int:pk>/', views.hospital_department_list, name='hospital-department-list'),
    path('hospital-doctor-list/<int:pk>/', views.hospital_doctor_list, name='hospital-doctor-list'),
    
    # The hospital-doctor-register is basically the url for a doctor to register to
    # a particular hospital, after logging in to the doctor profile
    path('hospital-doctor-register/<int:pk>/', views.hospital_doctor_register, name='hospital-doctor-register'),
    
    # this view-report page is giving reports of the user in random order
    path('view-report/<int:pk>', views.view_report, name='view-report'),
    
    # this test cart functionality is basically not showing anything, 
    # but i think this is related to the pharmacy shop testing stuff
    path('test-cart/<int:pk>/', views.test_cart, name='test-cart'),
    
    # this is also empty, but this maybe listing the prescriptions of the person
    # this is also working fine just dont allow external referring
    path('prescription-view/<int:pk>', views.prescription_view, name='prescription-view'),
    
    # this is also giving errors, need to check the views.py function for this
    # problem with all the paths given below
    
    
    # this pres_pdf is used for downloading the prescription in pdf format
    # to the users pc, this is present on the prescription download button
    path('pres_pdf/<int:pk>/',views.prescription_pdf, name='pres_pdf'),
    # this test urls are not working fine
    path('test-single/<int:pk>/', views.test_single, name='test-single'),
    path('test-remove-cart/<int:pk>/', views.test_remove_cart, name='test-remove-cart'),
    path('test-add-to-cart/<int:pk>/<int:pk2>/', views.test_add_to_cart, name='test-add-to-cart'),
    
    path('delete-prescription/<int:pk>/', views.delete_prescription, name='delete-prescription'),
    path('delete-report/<int:pk>/', views.delete_report, name='delete-report'),
]


# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

