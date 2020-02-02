import graphene
from graphene_django.types import DjangoObjectType, ObjectType
 
from ..models import Blog
from .authors import AuthorType
 
 
class BlogFields():
    title = graphene.String()
    body = graphene.String()
 
 
class BlogType(DjangoObjectType, BlogFields):
    class Meta:
        model = Blog
 
    id = graphene.ID(required=True)
    author = AuthorType()
 
 
class BlogInputType(graphene.InputObjectType, BlogFields):
    id = graphene.ID()
    author_id = graphene.ID()
 
 
class DeleteBlogInputType(graphene.InputObjectType):
     id = graphene.ID(required=True)