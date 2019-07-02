from django.conf import settings
from django.db import models
from django.utils import timezone
from django.db.models import Q
User=settings.AUTH_USER_MODEL
# Create your models here.
class BlogsQuerySet(models.QuerySet):
	def published(self):
		now=timezone.now()
		return self.filter(publish_date__lte=now)
	def search(self,query):
		lookup=(Q(title__icontains=query ) | 
			   Q(content__icontains=query) |
			   Q(slug__icontains=query) |
			   Q(user__first_name__icontains=query) |
			   Q(user__last_name__icontains=query) | 
			   Q(user__username__icontains=query)) 
		return self.filter(lookup)


class BlogsManager(models.Manager):
	def get_queryset(self):
		return BlogsQuerySet(self.model , using=self._db)

	def published(self):
		return self.get_queryset().published()

	def search(self,query=None):
		if query is None:
			return self.get_queryset().none()
		return self.get_queryset().published().search(query)
class Blogs(models.Model):
	user	   =models.ForeignKey(User,default=1,on_delete=models.SET_NULL,null=True)
	image	   =models.ImageField(upload_to='image/',blank=True,null=True)
	title	   =models.CharField(max_length=200,null=False,blank=False)
	slug 	   =models.SlugField(unique=True)
	content    =models.TextField(blank=False,null=False)
	publish_date=models.DateTimeField(auto_now=False,auto_now_add=False,null=True,blank=True)
	timestamp=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)
	
	objects=BlogsManager()

	class Meta:
		ordering=['-publish_date','-updated','-timestamp']
	def get_absolute_url(self):
		#print ({self.slug})
		return f"/microBlogger/{self.slug}"

	def get_edit_url(self):
		return f"{self.get_absolute_url()}/edit"
		
	def get_delete_url(self):
		return f"{self.get_absolute_url()}/delete"