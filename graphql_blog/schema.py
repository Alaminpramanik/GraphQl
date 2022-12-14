import graphene
from page.schema.authors import schema as author_schema
from page.schema.blogs import schema as blog_schema
from accounts.schema.users import schema as user_schema 


class Query(author_schema.Query, blog_schema.Query, user_schema.Query):
    pass


class Mutation(author_schema.Mutation, blog_schema.Mutation, user_schema.Mutation):
    pass
    
schema = graphene.Schema(query=Query, mutation=Mutation)
