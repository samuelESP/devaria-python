from fastapi import FastAPI
from pydantic import BaseModel


class Usuario(BaseModel):
    nome: str
    usuario: str | None
    senha: str


app = FastAPI()


@app.get("/ola-mundo")
async def root():
    return {
        "mensagem": "Olá mundo, essa é a minha primeira API!"
    }


@app.get("/api/soma")
def soma():
    return {
        "resultado": 3 + 7
    }


@app.post("/api/login")
def login(usuario: Usuario):
    if usuario.nome == "Samuel" and usuario.senha == "123":
        return {
            "mensagem": "logado com sucesso"
        }
    else:
        return {
            "mensagem": "senha ou usuario incorretos"
        }
