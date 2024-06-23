from fastapi import FastAPI


def create_api_application() -> FastAPI:
    app = FastAPI()
    return app


app = create_api_application()
