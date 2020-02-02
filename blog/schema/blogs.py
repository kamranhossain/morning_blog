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


class Query(ObjectType):
    blog = graphene.Field(BlogType, id=graphene.ID(required=True))
    blogs = graphene.List(BlogType)
     
    def resolve_blog(self, info, **kwargs):
        id = kwargs.get("id")
        return Blog.objects.get(id=id)
 
    def resolve_blogs(self, info, **kwargs):
        return Blog.objects.all()