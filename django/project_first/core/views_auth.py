from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from django.shortcuts import reverse, redirect, render
from .forms_auth import LoginForm


class LoginView(LoginView):
    template_name = 'my_auth/login.html'
    form_class = LoginForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('core:index'), request)
            context = {
                'form': form
            }
            return render(request, self.template_name, context)
        else:
            context = {
                'form': form
            }
            return render(request, self.template_name, context)
