import uvicorn

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 8004
RELOAD = True
DEBUG = True


if __name__ == "__main__":
    uvicorn.run(
        app="api.learning:app",
        host=SERVER_HOST,
        port=SERVER_PORT,
        reload=RELOAD,
        use_colors=DEBUG,
    )