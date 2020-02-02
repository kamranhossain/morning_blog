import graphene
from graphene_django.types import DjangoObjectType, ObjectType
 
from ..models import Author
 
 
class AuthorFields():
    name = graphene.String()
    description = graphene.String()
  
 
class AuthorType(DjangoObjectType, AuthorFields):
    class Meta:
        model = Author
    id = graphene.ID(required=True)
 
 
class AuthorInputType(graphene.InputObjectType, AuthorFields):
    id = graphene.ID()
 
 
class DeleteAuthorInputType(graphene.InputObjectType):
     id = graphene.ID(required=True)

class Query(ObjectType):
    author = graphene.Field(AuthorType, id=graphene.ID(required=True))
    authors = graphene.List(AuthorType)
 
    def resolve_author(self, info, **kwargs):
        id = kwargs.get("id")
        return Author.objects.get(id=id)
         
    def resolve_authors(self, info, **kwargs):
        return Author.objects.all()