from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template
from .forms import ContactForm

def contact_page(request):
	template_name="form.html"
	form=ContactForm(request.POST or None)
	if form.is_valid():
		print (form.cleaned_data)
		form=ContactForm()
	context={
	"form":form,
	"title": "Contact Us"
	}
	return render(request,template_name,context)