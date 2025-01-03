from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

from django.utils import timezone

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    Course = models.TextField(max_length=500, blank=True)
    profile_pic=models.ImageField( default="Default.jpg",upload_to='profile_pics',
    )


    def __str__(self):
        return self.user.username



class Post(models.Model):
    
    title=models.CharField(max_length=500, null=True)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    body=models.TextField()
    published=models.DateTimeField(default=timezone.now)

    def __str__(self):
     return f"post by :{self.author}"
    
    def total_likes(self):
        return self.likes.count()
    
    class Meta:
       ordering=['-published']


class Message(models.Model):
   sender=models.ForeignKey(User,on_delete=models.CASCADE,related_name='sent') 
   receiver=models.ForeignKey(User,on_delete=models.CASCADE,related_name='received') 
   content=models.TextField()
   time=models.DateTimeField(auto_now_add=True)
  

   def __str__(self):
      return f"from:{self.sender}to {self.receiver}"

class Like(models.Model):
   liker=models.ForeignKey(User, on_delete=models.CASCADE,related_name='liker')
   post=models.ForeignKey(Post, on_delete=models.CASCADE,related_name='likes')
  

   def __str__(self):
         return f" liked by {self.liker} "  

   class Meta:
        unique_together=('liker','post')









 

