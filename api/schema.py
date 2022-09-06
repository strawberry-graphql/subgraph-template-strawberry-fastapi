import strawberry
from strawberry.file_uploads import Upload


@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello World"

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_user(self, name: str, file: Upload) -> str:
        return str(file)


schema = strawberry.Schema(Query, Mutation)
