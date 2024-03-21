
from django.contrib import admin
from django.urls import path
from students import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',views.create,name='create'),

    path('update/<int:id>/',views.update, name='update'),
      path('delete/<int:id>/',views.delete, name='delete'),



    
    # path('read',views.create),
]
