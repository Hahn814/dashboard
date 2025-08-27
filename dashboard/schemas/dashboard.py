import strawberry

@strawberry.type
class Query:
    @strawberry.field
    def dashboard(self) -> str:
        return "Dashboard Query"

    @strawberry.field
    def get_task_by_id(self, id: int) -> str:
        return f"Task ID: {id}"