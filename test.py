from fastapi import FastAPI
from enum import Enum
from typing import List, Dict

app = FastAPI()


class Tag(Enum):
    IMMUTABLE = 'IMMUTABLE'
    MUTABLE = 'MUTABLE'


@app.post('/a', 
          tags=[Tag.IMMUTABLE],
          summary="Первая функция", 
          description="Описание для эндпоинта a."
        )
def a() -> str:
    """
    Описание функции a.
    """
    return 'Вот это ответ!'


@app.get(
        '/b', 
        tags=[Tag.MUTABLE], 
        summary="Вторая функция",
        description="Описание для эндпоинта b."
    )
def b() -> List[str]:
    """
    Описание функции b.
    """
    return ['Вот', 'это', 'ответ!']


@app.post(
        '/c', 
        tags=[Tag.IMMUTABLE], 
        summary="Третья функция",
        description="Описание для эндпоинта c."
    )
def c() -> int:
    """
    Описание функции c.
    """
    return 42


@app.get(
        '/d', 
        tags=[Tag.IMMUTABLE], 
        summary="Четвертая функция", 
        description="Описание для эндпоинта d."
    )
def d() -> Dict[str, str]:
    """
    Описание функции d.
    """
    return {'Вот': 'это ответ!'}