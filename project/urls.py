from django.contrib import admin
from django.urls import path
from AppAscenzi.views import index
from AppAscenzi.views import (
JugueteList, JugueteDetail, JugueteUpdate, JugueteDelete, JugueteCreate, JugueteSearch,
Login, SignUp, Logout, JugueteMineList)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name= "index"),
    path('juguete/list', JugueteList.as_view(), name="juguete-list"),
    path('juguete/<pk>/detail', JugueteDetail.as_view(), name="juguete-detail"),
    path('juguete/<pk>/update', JugueteUpdate.as_view(), name="juguete-update"),
    path('juguete/<pk>/delete', JugueteDelete.as_view(), name="juguete-delete"),
    path('juguete/create', JugueteCreate.as_view(), name="juguete-create"),
    path('juguete/search', JugueteSearch.as_view(), name="juguete-search"),
    path('login/', Login.as_view(), name="login"),
    path('signup/', SignUp.as_view(), name="signup"),
    path('logout/', Logout.as_view(), name="logout"),
    path('juguete/list/mine', JugueteMineList.as_view(), name="juguete-mine"),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

