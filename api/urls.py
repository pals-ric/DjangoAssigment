from django.urls import path
from .views import candidate_list

urlpatterns = [
    path('candidate/', candidate_list),

]