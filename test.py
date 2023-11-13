from fastapi import FastAPI, Depends
from enum import Enum

app = FastAPI()


class Tag(str, Enum):
    IMMUTABLE = 'immutable'
    MUTABLE = 'mutable'


@app.post('/a', 
          tags=[Tag.IMMUTABLE],
          summary="Первая функция", 
          responses={200:{"description": "Возвращает строку"}},
          description="POST запрос, возвращающий строку.")
def a() -> str:
    """
    Описание функции POST /a.
    """
    return 'Вот это ответ!'


@app.get(
    '/b',
    tags=[Tag.MUTABLE],
    description='Функция возвращает список.',
    summary='Вторая функция')
def b() -> list[str]:
    return ['Вот', 'это', 'ответ!']

@app.post(
        '/c', 
        tags=[Tag.IMMUTABLE], 
        summary="Третья функция",
        responses={200:{"description": "Возвращает целое число"}},
    description="POST запрос, возвращающий число.")
def c() -> int:
    """
    Описание функции POST /c.
    """
    return 42


@app.get(
        '/d', 
        tags=[Tag.IMMUTABLE], 
        summary="Четвертая функция", 
    description="GET запрос, возвращающий словарь.")
def d() -> dict[str, str]:
    return {'Вот': 'это ответ!'}
