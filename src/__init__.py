from fastapi import FastAPI
from src.books.routes import book_router

version = "v1"

app = FastAPI(
    title="Bookly", description="A REST API fro a book review service", version=version
)
app.include_router(book_router, prefix=f"/api/{version}/books", tags=["Books"])