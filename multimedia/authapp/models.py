from django.db import models
from django.contrib.auth.models import User
from multimedia.blogapp.models import Post, Category
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class CreatorProfile(models.Model):
    creator_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    date_joined_as_creator = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)
    bio = models.TextField(max_length= 1000, null=True, blank=True)
    social_links = models.JSONField(default= dict, null=True, blank = True)
    last_login = models.DateTimeField(auto_now=True)
    niche = models.ForeignKey(Category, on_delete=models.CASCADE,  null=True, blank=True)
    
    
    def __str__(self):
        return f"Bl{self.creator_id} {self.user.username}"
    

    @receiver(post_save, sender = User)
    def create_creator_profile(sender, instance, created, **kwargs):
        if created and hasattr(instance, 'is_creator') and instance.is_creator:
            CreatorProfile.objects.create(user=instance)
            
    def save_creator_profile(sender, instance, **kwargs):
        if hasattr(instance, 'creatorprofile'):
            instance.creatorprofile.save()    
    
  
class UserProfile(models.Model):
     user = models.OneToOneField(User, on_delete=models.CASCADE)
     is_creator = models.BooleanField(default=False)
     sex = models.CharField(max_length= 10, null=True, blank = True)
     country = models.CharField(max_length= 50, null=True, blank=True)
     profile_picture = models.ImageField(upload_to= "profil_pic/", blank=True, null=True)
     like_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="liked_by", null=True)
     bookmarked_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="bookmarked_by", null = True)
     followed_craetors = models.ForeignKey(CreatorProfile, on_delete=models.CASCADE, null=True, related_name= "followers", blank=True)
     preferences = models.JSONField(default=dict, blank=True)
     
     def __str__(self):
         return f"{self.user.id} {self.user.username}"
     
     @receiver(post_save, sender=User)
     def create_user_profile(sender, instance, created, **kwargs):
         if created:
             UserProfile.objects.create(user = instance)
         
     
     def save_user_profile(sender, instance, **kwargs):
         instance.userprofile.save()
     
     
        
