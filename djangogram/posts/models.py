from django.db import models
from djangogram.users import models as user_model

# Create your models here.

class TimeStampedModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    # 메타옵션을 줌으로써 단독으로 클래스 생성 불가
    class Meta:
        abstract = True

class Post(TimeStampedModel):
    author = models.ForeignKey(
                user_model.User, 
                null = True, 
                on_delete=models.CASCADE, 
                related_name='post_author'
            )
    image = models.ImageField(blank=True)
    caption = models.TextField(blank=True)
    image_likes = models.ManyToManyField(user_model.User, related_name='post_image_likes')

class Comment(TimeStampedModel):
    author = models.ForeignKey(
                user_model.User, 
                null = True, 
                on_delete=models.CASCADE, 
                related_name='comment_author'
            )
    posts = models.ForeignKey(
        Post,
        null=True,
        on_delete=models.CASCADE,
        related_name='comment_post'
    )
    contents = models.TextField(blank=True)