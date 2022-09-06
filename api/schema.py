import strawberry


@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello World"


@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_user(self, name: str) -> str:
        return name


schema = strawberry.Schema(Query, Mutation)
