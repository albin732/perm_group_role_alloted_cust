
from .view.logs import Login, Logout
from django.urls import path
from .view.dashboard import AdminDashboard, SubAdminDashboard
from .view.registeration import SignUp

urlpatterns = [
    path('SignUp/', SignUp.as_view(), name='SignUp'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('admin_dashboard/', AdminDashboard.as_view(), name='admin_dashboard'),
    path('sub_admin_dashboard/', SubAdminDashboard.as_view(),
         name='sub_admin_dashboard'),
]
