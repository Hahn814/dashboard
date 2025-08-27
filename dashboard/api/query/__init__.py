from strawberry.fastapi import GraphQLRouter
from dashboard.schemas import graphql_schema as schema


router = GraphQLRouter(schema)