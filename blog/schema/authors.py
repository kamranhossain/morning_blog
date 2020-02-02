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