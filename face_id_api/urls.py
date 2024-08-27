from django.urls import path
from .views import result_add
urlpatterns = [
    path('postdata/', result_add)

]