from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from accounts.forms import SignUpForm
from accounts.models import DetailModel
from django.contrib.auth.models import Group


class SignUp(View):

    def get(self, request):
        user_form = SignUpForm()
        return render(request, 'SignUp.html', {'user_form': user_form})

    def post(self, request):
        user_form = SignUpForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.detail.user_type = 'sub_admin'  # sub_admin
            user.detail.save()
            # permission Group add
            iusr_group = Group.objects.get(name='sub_admin_perm')
            iusr_group.user_set.add(user)
            messages.success(request, 'Account created successfully')
            return redirect('/accounts/SignUp')
        messages.success(request, 'Validation Error')
        return render(request, 'SignUp.html', {'user_form': user_form})
