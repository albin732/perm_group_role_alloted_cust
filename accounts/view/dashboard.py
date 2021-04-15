from django.views import View
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.utils.decorators import method_decorator
from common.auth_decorator import role_required, admin, sub_admin

admin_decorators = [login_required(
    login_url='/accounts/login/'), role_required('master_admin')]
sub_admin_decorators = [login_required(
    login_url='/accounts/login/'), role_required('sub_admin')]


@ method_decorator(admin_decorators, name="dispatch")
class AdminDashboard(View):
    # @login_required(login_url='/accounts/login/')
    def get(self, request):
        return render(request, "admin_dashboard.html")


@ method_decorator(sub_admin_decorators, name="dispatch")
class SubAdminDashboard(View):
    # @login_required(login_url='/accounts/login/')
    def get(self, request):
        return render(request, "sub_admin_dashboard.html")
