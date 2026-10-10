from django.http import response
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import User
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.
class CustomUserCreationForm(UserCreationForm):
	class Meta(UserCreationForm.Meta):
		model = User
		fields = ('username', 'email', 'password1', 'password2')

class RegisterView(CreateView):
	model = User
	form_class = CustomUserCreationForm
	template_name = 'users/register.html'
	success_url = reverse_lazy('core:index')	# 注册成功跳转首页

	# 🔥 面试高频点：重写 form_valid，在注册成功后自动登录用户
	def form_valid(self, form):
		response = super().form_valid(form)
		login(self.request, self.object, backend='django.contrib.auth.backends.ModelBackend')
		return response

# 登录/登出功能
class UserLoginView(LoginView):
	template_name = 'users/login.html'
	# 如果登录成功，自动跳转到 LOGIN_REDIRECT_URL 配置的地址

class UserLogoutView(LogoutView):
	pass # 什么都不用写，直接继承
