from django.urls import path
from .views import leadlist, lead_detail, lead_create

app_name = "leads"

urlpatterns = [
    path('', leadlist),
    path('<int:pk>/', lead_detail),
    path('create/', lead_create),

]