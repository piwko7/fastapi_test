from fastapi import FastAPI, Path

import random
import string
from dataclasses import dataclass

app = FastAPI()


@app.get("/")
def read_root():
    return {"Message": "Dzban"}


def generate_id() -> str:
    return "".join(random.choices(string.ascii_uppercase, k=12))


@dataclass
class Person:
    name: str
    adress: str
    active: bool = True
    email_addresses: list[str] = []


def main() -> None:
    person = Person(name="John", adress="123 Main St")