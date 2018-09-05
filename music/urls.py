from django.urls import path
from . import views

urlpatterns = [
	path('',views.index, name = 'index_music'),
	path('ngoma/',views.ngoma2, name = 'ngoma2')
]
