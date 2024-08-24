from django.urls import path
from shop import views

app_name = "shop"

urlpatterns = [
    path('', views.allProductCat, name = "allProductCat"),
    path('allproducts/<slug:cslug>', views.allproducts, name = "allproducts"),
    path('prodetail/<slug:pslug>', views.prodetail, name = "prodetail"),
    path('reg/', views.register, name="register"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
]
