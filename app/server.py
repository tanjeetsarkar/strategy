import strawberry

from fastapi import Depends, FastAPI
from models import SessionLocal
from schemas import Query, Mutation
from strawberry.fastapi import GraphQLRouter

async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def get_context(
    db=Depends(get_db)
):
    return {
    "db": db
    }

app = FastAPI()
schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema, context_getter=get_context,)

app.include_router(graphql_app, prefix="/graphql")


