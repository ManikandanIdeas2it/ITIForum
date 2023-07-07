import uuid
from django.db import models


class Fourm_post(models.Model):
    post_id = models.UUIDField(
        blank=False, null=False, primary_key=True, default=uuid.uuid4, editable=False)
    post_text = models.CharField(max_length=600)
    post_image = models.BinaryField()
    post_caption = models.CharField(max_length=200)
    User_user_id = models.UUIDField(blank=False, null=False)
    Post_likes_like_id = models.UUIDField(blank=False, null=False)
    Post_comment_comm_id = models.UUIDField(blank=False, null=False)

    def __str__(self):
        return self.post_id


class Users(models.Model):
    user_id = models.UUIDField(
        blank=False, null=False, primary_key=True, default=uuid.uuid4, editable=False)
    user_name = models.CharField(max_length=50, blank=False, null=False)
    user_emp_id = models.CharField(max_length=6, blank=False, null=False)

    def __str__(self):
        return self.user_name
