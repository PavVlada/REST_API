from fastapi import FastAPI

from api import router


app = FastAPI(
    title='Task manager',
    description='Веб-сервис, предоставляющий REST API для управления персональным списком задач',
    version='1.0.0',
)
app.include_router(router)