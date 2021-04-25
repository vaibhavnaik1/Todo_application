from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', views.index, name="todo"),
	path('del/<int:id>', views.delete_data , name="del"),
]
