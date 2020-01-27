from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    path('', LoginView.as_view()),
    path('logout/', views.logout_view),

    path('products', views.product_manager),
    path('product/<int:id>', views.product_view),
    path('product', views.product_view),

    path('providers', views.provider_manager),
    path('provider/<int:id>', views.provider_view),
    path('provider', views.provider_view),

]
