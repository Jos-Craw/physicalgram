from django.shortcuts import render, get_object_or_404,redirect
from .models import Post, AdvUser, Comment
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import PostForm, ChangeUserInfoForm, RegisterUserForm, CommentForm
from django.contrib.auth import logout
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordChangeView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.signing import BadSignature
from .utilities import signer

@login_required
def index(request):
	posts = Post.objects.all()
	return render(request, 'news/index.html',{'posts': posts})

	initial= {'post':post.pk}
	initial['author'] = request.user.username
	form_class = CommentForm
	form = form_class(initial=initial)
	if request.method == 'POST':
		c_form = form_class(request.POST)
		if c_form.is_valid():
			c_form.save()
		else:
			form = c_form
	return render(request, 'news/index.html',{'post':post,'comments':comments,'form':form})

@login_required
def profile(request):
	posts = Post.objects.filter(author=request.user.pk)
	context = {'posts': posts}
	return render(request,'news/profile.html',context)

@login_required
def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=pk)
    initial= {'post':post.pk}
    initial['author'] = request.user.username
    form_class = CommentForm
    form = form_class(initial=initial)
    if request.method == 'POST' or request.FILES:
    	c_form = form_class(request.POST,request.FILES)
    	if c_form.is_valid():
    		c_form.save()
    	else:
    		form = c_form
    return render(request, 'news/detail.html',{'post':post,'comments':comments,'form':form})

@login_required
def create(request):
	if request.method == 'POST' or request.FILES:
		form = PostForm(request.POST,request.FILES)
		if form.is_valid():
			post = form.save()
			return redirect('news:profile')
	else:
		form =PostForm(initial={'author':request.user.pk})
	context = {'form':form}
	return render(request,'news/create.html',context)

@login_required
def editpost(request,pk):
	post = get_object_or_404(Post,pk=pk)
	if request.method == 'POST' or request.FILES:
		form = PostForm(request.POST,request.FILES,instance=post)
		if form.is_valid():
			post = form.save()
			return redirect('news:profile')
	else:
		form = PostForm(instance=post)
	context = {'form':form}
	return render(request,'news/editpost.html',context)

@login_required
def deletepost(request,pk):
	post = get_object_or_404(Post,pk=pk)
	if request.method == 'POST':
		post.delete()
		return redirect('news:profile')
	else:
		context={'post':post}
	return render(request,'news/deletepost.html',context)

@login_required
def good(request):
	return render(request, 'news/good.html')

@login_required
def about(request):
	return render(request, 'news/about.html')	

class POSTLoginView(LoginView):
	template_name='news/login.html'

class POSTLogoutView(LoginRequiredMixin, LogoutView):
	template_name='news/logout.html'

class POSTChangeView(SuccessMessageMixin,LoginRequiredMixin,PasswordChangeView):
	template_name = 'news/password_change.html'
	success_url = reverse_lazy('news:profile')
	success_message = 'Password changed'

class ChangeUserInfoView(SuccessMessageMixin,LoginRequiredMixin,UpdateView):
	model = AdvUser
	template_name ='news/change_user_info.html'
	form_class = ChangeUserInfoForm
	success_url = reverse_lazy('news:profile')
	success_message = 'Info changed'

	def dispatch(self,request,*args,**kwargs):
		self.user_id = request.user.pk
		return super().dispatch(request,*args,**kwargs)

	def	get_object(self,queryset=None):
		if not queryset:
			queryset = self.get_queryset()
		return get_object_or_404(queryset,pk=self.user_id)

class RegisterUserView(CreateView):
	model = AdvUser
	template_name = 'news/register_user.html'
	form_class = RegisterUserForm
	success_url = reverse_lazy('news:register_done')

class RegisterDoneView(TemplateView):
	template_name = 'news/register_done.html'

class DeleteUserView(LoginRequiredMixin,DeleteView):
	model = AdvUser
	template_name = 'news/delete_user.html'
	success_url = reverse_lazy('news:index')

	def dispatch(self,request,*args,**kwargs):
		self.user_id = request.user.pk
		return super().dispatch(request,*args,**kwargs)

	def post(self, request,*args,**kwargs):
		logout(request)
		messages.add_message(request,messages.SUCCESS,'User deleted')
		return super().post(request,*args,**kwargs)

	def get_object(self, queryset=None):
		if not queryset:
			queryset = self.get_queryset()
		return get_object_or_404(queryset,pk=self.user_id)

def user_activate(request,sign):
	try:
		username = signer.unsign(sign)
	except BadSignature:
		return render(request,'news/bad_signature.html')
	user = get_object_or_404(AdvUser, username=username)
	if user.is_activated:
		template = 'news/user_is_activated.html'
	else:
		template = 'news/activation_done.html'
		user.is_active = True
		user.is_activated = True
		user.save()
	return render(request, template)