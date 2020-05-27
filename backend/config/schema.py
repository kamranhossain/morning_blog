import graphene
import graphql_jwt

from apps.blog.schema.authors import schema as author_schema
from apps.blog.schema.blogs import schema as blog_schema
from apps.users.schema.users import schema as user_schema


class Query(author_schema.Query, blog_schema.Query, user_schema.Query, graphene.ObjectType):
    pass


class Mutation(author_schema.Mutation, blog_schema.Mutation):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
