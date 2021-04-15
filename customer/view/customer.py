from django.contrib.auth.decorators import login_required
from customer.models import CustomerModel

from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from django.urls import reverse_lazy

from django.utils.decorators import method_decorator
from common.auth_decorator import group_required, role_required, admin

admin_decorators = [login_required(
    login_url='/accounts/login/'), group_required('master_admin_perm',)]
sub_admin_decorators = [login_required(
    login_url='/accounts/login/'), group_required('sub_admin_perm', 'master_admin_perm')]
# all_usr_decorators = [login_required(
#     login_url='/login/'), all_user]


@method_decorator(sub_admin_decorators, name="dispatch")
class Customer_CreateView(CreateView):
    model = CustomerModel
    template_name = 'customer_add.html'
    fields = ['customer_name', 'customer_email', 'customer_number',
              'customer_address']
    success_url = reverse_lazy('customer_list')

    def form_valid(self, form):
        form.instance.assigned_admin = self.request.user
        return super().form_valid(form)


@method_decorator(sub_admin_decorators, name="dispatch")
class Customer_UpdateView(UpdateView):
    model = CustomerModel
    template_name = 'subscriptionplan_edit.html'
    fields = ['customer_name', 'customer_email', 'customer_number',
              'customer_address']
    context_object_name = 'customer_list'


@method_decorator(sub_admin_decorators, name="dispatch")
class Customer_DeleteView(DeleteView):
    model = CustomerModel
    context_object_name = 'customer'
    template_name = 'customer_confirm_delete.html'
    success_url = reverse_lazy('customer_list')


@method_decorator(sub_admin_decorators, name="dispatch")
class Customer_ListView(ListView):
    model = CustomerModel
    template_name = 'customer_list.html'
    context_object_name = 'customers'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return CustomerModel.objects.all()
        else:
            return CustomerModel.objects.filter(assigned_admin=self.request.user)


@method_decorator(sub_admin_decorators, name="dispatch")
class Customer_DetailView(DetailView):
    model = CustomerModel
    template_name = 'customer_detail.html'
    context_object_name = 'customer'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return CustomerModel.objects.all()
        else:
            return CustomerModel.objects.filter(assigned_admin=self.request.user)
