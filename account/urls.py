from django.urls import path
from .views import CreateProfile, ManageProfile

urlpatterns = [
    path('signup/', CreateProfile.as_view(), name="signup"),
    path('manage/<str:pk>/', ManageProfile.as_view(), name="manage-profile"),


]
