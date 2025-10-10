from django.db import models
from django.utils import timezone
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):

    #Links author to the user or superuser
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    #Uses timezone 
    created_date = models.DateTimeField(default=timezone.now)
    #Publication date
    published_date = models.DateTimeField(blank=True, null=True)

    # Methods
    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comments=True)
    
    def get_absolute_url(self):
        # Return post_detail view/url with a kwarg of the primary key
        # Go to the post details from the post you just created (that is what self.pk represents here)
        return reverse("post_detail", kwargs={'pk': self.pk})
    
    def __str__(self):
        return self.title
    

class Comment(models.Model):

    post = models.ForeignKey('blog.Post', related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    # Reference approved_comments from approve_comments method
    approved_comments = models.BooleanField(default=False)

    def approve(self):
        self.approved_comments = True
        self.save()

    # A comment has to be approved by a super user
    # This means that we will probably go back to the posts list (list of posts) page instead of back to post_detail (the details of a post)
    # Homepage is going to be the list of all the posts
    def get_absolute_url(self):
        return reverse("post_list")

    def __str__(self):
        return self.text 