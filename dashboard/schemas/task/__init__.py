import strawberry

@strawberry.type
class Task:
    id: int
    name: str