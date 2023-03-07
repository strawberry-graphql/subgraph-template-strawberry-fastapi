from typing import Optional

import strawberry
from strawberry.schema_directive import Location


@strawberry.schema_directive(locations=[Location.SCHEMA])
class Contact:
    name: str = strawberry.field(description="Contact title of the subgraph owner")
    url: Optional[str] = strawberry.field(
        description="URL where the subgraph's owner can be reached"
    )
    description: Optional[str] = strawberry.field(
        description="Other relevant notes can be included here; supports markdown links"
    )


@strawberry.federation.type(keys=["id"])
class Thing:
    id: strawberry.ID
    name: Optional[str]

    @classmethod
    def resolve_reference(cls, **representation) -> "Thing":
        id_ = strawberry.ID(representation["id"])

        return cls(id=id_, name="Thing")


@strawberry.type
class Query:
    @strawberry.field
    def thing(self, id: strawberry.ID) -> Optional[Thing]:
        return Thing(id=id, name="Thing")


@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_user(self, name: str) -> str:
        return name


schema = strawberry.federation.Schema(
    Query,
    Mutation,
    enable_federation_2=True,
    schema_directives=[
        Contact(
            name="Server Team",
            url="https://myteam.slack.com/archives/teams-chat-room-url",
            description=(
                "send urgent issues to [#oncall]"
                "(https://yourteam.slack.com/archives/oncall)."
            ),
        )
    ],
)
