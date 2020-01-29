from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    path('', LoginView.as_view()),
    path('logout/', views.logout_view),

    path('products', views.product_manager),
    path('product/<int:id>', views.product_view),
    path('product', views.product_view),

    path('persons', views.person_manager),
    path('person/<int:id>', views.person_view),
    path('person', views.person_view),

]
