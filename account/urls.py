
from django.urls import path
from .views import Appointments, Blog, ChangePassword, ContactMessages, CreateProfile, Experience, FontsManage, ManageProfile, ManageSubscription, Layouts, FontsManage, Portfolio, Services, Skills, Testimonial, UploadCV

urlpatterns = [
    path('signup/', CreateProfile.as_view(), name="signup"),
    path('manage/<str:pk>/', ManageProfile.as_view(), name="manage-profile"),
    path('subscription/', ManageSubscription.as_view(),
         name="manage_subscription"),
    path('layouts/', Layouts.as_view(), name='layouts'),
    path('fonts/<str:pk>', FontsManage.as_view(), name='fonts'),
    path('services/', Services.as_view(), name='services'),
    path('skills/', Skills.as_view(), name='skills'),
    path('experience/', Experience.as_view(), name='experience'),
    path('testimonial/', Testimonial.as_view(), name='testimonial'),
    path('portfolio/', Portfolio.as_view(), name='portfolio'),
    path('blog/', Blog.as_view(), name='blog'),
    path('appointments/', Appointments.as_view(), name='appointments'),
    path('contact_messages/', ContactMessages.as_view(), name='contact_messages'),
    path('upload_cv/', UploadCV.as_view(), name='upload_cv'),
    path('change_password/', ChangePassword.as_view(), name='change_password'),


]
