from core.views import home, about, registration, success, all_profile, signup
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('registeration/', registration, name='registration'),
    path('success/', success, name='success'),
    path('profile/', all_profile, name='profiles'),

    # auth routes
    path('signup/', signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='student/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]