from rest_framework import serializers

from blog.models import Category as CategoryModel
from blog.models import Article as ArticleModel
from blog.models import Comment as CommentModel

from user.models import User as UserModel
from user.models import UserProfile as UserModel
from user.models import Hobby as HobbyModel


# from blog.serializers import ArticleSerializer

class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__"