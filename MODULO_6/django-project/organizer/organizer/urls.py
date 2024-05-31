"""
URL configuration for organizer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todo_app import views

# url_base = http://127.0.0.1:8000/

urlpatterns = [
    # Ejemplos de prueba
    path('admin/', admin.site.urls), # http://127.0.0.1:8000/admin/
    path('hello_world', views.hello_world), # http://127.0.0.1:8000/hello_world
    path('about', views.about), # http://127.0.0.1:8000/about
    path('json_task', views.json_tasks ), # http://127.0.0.1:8000/json_task
    # Aplicacion todo_app
    path('', views.index), # url_base = http://127.0.0.1:8000/
    path('update_task/<int:task_id>', views.update_task),
    path('delete_task/<int:task_id>', views.delete_task)
]

# request params : parametros de las consultas https
#http://127.0.0.1:8000/update_task/int:id