from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.template.loader import get_template
from microBlogger.models import Blogs
from .forms import BlogsModelForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
def get(request):
    try:
    	context={}
    	if request.user.is_authenticated:
    		obj=Blogs.objects.all()[:5]#selecting only 5
    		#obj1=get_object_or_404(Blogs,slug="hello-world	")
    		#print (obj1)
    		context={"title":"Welcome to Twitter","user":request.user,"object":obj}
    	return render(request, 'index_microBlogger.html', context)
    except Exception as e:
        print (e)
        return render(request, 'index_microBlogger.html', {"user":"Something went Wrong"})
def about(request):
	print (request)
	obj=Blogs.objects.filter(title="From the CLI")
	print (obj)
	context       ={"user":request.user}
	template_name ='about.html'
	template_obj=get_template(template_name)
	return HttpResponse(template_obj.render(context))

def get_user_details(request,slug):
	#to check user user_details
	obj=get_object_or_404(Blogs,slug=slug)
	print (obj)
	template_name= "user_details.html"
	context={"object":obj}
	#fuctionality yet ot be defined
	return render(request,template_name,context)

def blog_list_view(request):
	res=Blogs.objects.all().published()
	#res=Blogs.objects.all()#.published()
	if request.user.is_authenticated:
		my_res=Blogs.objects.filter(user=request.user)
		res=(res|my_res).distinct()
	template_name= "blog_list_view.html"
	context={"object":res}
	return render(request,template_name,context)

@staff_member_required
#@login_required
def blog_create_view(request):
	#create using froms
	"""form=addBlogForm(request.POST or None)
				if form.is_valid():
					obj=Blogs.objects.create(**form.cleaned_data)
					form=addBlogForm()"""
	form=BlogsModelForm(request.POST or None,request.FILES or None)
	if form.is_valid():
		obj=form.save(commit=False)
		obj.user=request.user
		#form.save()
		obj.save()
		form=BlogsModelForm()
	#template_name= "blog_create_view.html"
	template_name= "form.html"
	context={"form":form}
	return render(request,template_name,context)

def blog_detail_view(request,slug):
	obj=get_object_or_404(Blogs,slug=slug)
	print (obj)
	template_name= "blog_detail_view.html"
	context={"object":obj}
	return render(request,template_name,context)

def blog_update_view(request,slug):
	obj=get_object_or_404(Blogs,slug=slug)
	form=BlogsModelForm(request.POST or None,instance=obj)
	if form.is_valid():
		print ("Insde")
		form.save()

	template_name="form.html"
	context={
	"form":form,
	"title":f"Update {obj.title}"
	
	}
	return render(request,template_name,context)
def blog_delete_view(request,slug):
	obj=get_object_or_404(Blogs,slug=slug)
	template_name="blog_delete_view.html"
	if request.method=="POST":
		obj.delete()
		return redirect("/microBlogger")
	context={
	"object":obj
	}
	return render(request,template_name,context)

