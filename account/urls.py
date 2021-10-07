
from .views import log_in, logout_view
from django.urls import path
from .views import Appointments, Blog, ChangePassword, ContactMessages, CreateProfile, Experience, FontsManage, ManageProfile, ManageSubscription, Layouts, FontsManage, Portfolio, Services, Skills, SkillEdit, SkillDelete, SkillActivate, SkillDeactivate, SubSKillActivate, SubSkillDeactivate, SubSkillDelete, SubSkillEdit, Testimonial, UploadCV

urlpatterns = [
    path('signup/', CreateProfile.as_view(), name="signup"),
    path('manage/<str:pk>/', ManageProfile.as_view(), name="manage-profile"),
    path('subscription/', ManageSubscription.as_view(),
         name="manage_subscription"),
    path('layouts/', Layouts.as_view(), name='layouts'),
    path('fonts/<str:pk>', FontsManage.as_view(), name='fonts'),
    path('services/', Services.as_view(), name='services'),
    path('skills/', Skills, name='skills'),
    path('skill-edit/<str:pk>', SkillEdit.as_view(), name="skill_edit"),
    path('skill-delete/<str:pk>', SkillDelete.as_view(), name="skill_delete"),
    path('skill-activate/<str:pk>', SkillActivate, name="skill_activate"),
    path('skill-deactivate/<str:pk>', SkillDeactivate, name="skill_deactivate"),
    path('subskill-edit/<str:pk>', SubSkillEdit.as_view(), name="subskill_edit"),
    path('subskill-delete/<str:pk>',
         SubSkillDelete.as_view(), name="subskill_delete"),
    path('subskill-activate/<str:pk>',
         SubSKillActivate, name="subskill_activate"),
    path('subskill-deactivate/<str:pk>',
         SubSkillDeactivate, name="subskill_deactivate"),
    path('experience/', Experience.as_view(), name='experience'),
    path('testimonial/', Testimonial.as_view(), name='testimonial'),
    path('portfolio/', Portfolio.as_view(), name='portfolio'),
    path('blog/', Blog.as_view(), name='blog'),
    path('appointments/', Appointments.as_view(), name='appointments'),
    path('contact_messages/', ContactMessages.as_view(), name='contact_messages'),
    path('upload_cv/', UploadCV.as_view(), name='upload_cv'),
    path('change_password/', ChangePassword.as_view(), name='change_password'),
    path('log_in/', log_in, name='log_in'),
    path('log_out/', logout_view, name='log_out')


]
