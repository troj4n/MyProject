from django import forms
from .models import Blogs

class addBlogForm(forms.Form):
	title= forms.CharField()
	slug=  forms.SlugField()
	content= forms.CharField(widget=forms.Textarea)

class BlogsModelForm(forms.ModelForm):
	class Meta:
			model=Blogs
			fields =['title','image','slug','content','publish_date']
	
	def clean_title(self,*args,**kwargs):
		print (dir(self))
		instance=self.instance
		print(instance)
		title=self.cleaned_data.get("title")
		qs=Blogs.objects.filter(title__iexact=title)
		if instance is not None:
			qs=qs.exclude(pk=instance.pk)
		if qs.exists():
			raise forms.ValidationError("OOPS!! A tweet already exists with the same title. Consider changing tht title to something else")
		return title

	