import strawberry
from strawberry.tools import merge_types
from dashboard.schemas.dashboard import Query as DashboardQuery

Query = merge_types("Query", (DashboardQuery,))
graphql_schema = strawberry.Schema(query=Query)