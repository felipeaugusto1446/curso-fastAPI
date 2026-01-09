from fastapi import APIRouter, Depends
from models import Usuario
from dependencies import pegar_sessao
from main import bcrypt_context
auth_router = APIRouter(prefix="/auth",tags=["Auth"])

@auth_router.get("/")
async def autenticar():
    """
    Essa é a rota padrão de autenticação do nosso sistema
    """
    return {"Mensagem":"Você acessou a rota de autenticação","autenticado": False}

@auth_router.post("/criar_conta")
async def criar_conta(email:str,senha:str,nome:str,session = Depends(pegar_sessao)):
    usuario = session.query(Usuario).filter(Usuario.email==email).first()
    if usuario:
        #já existe um usuario com esse email
        return{"Mensagem":"Já existe um usuário com esse email"}
    else:
        # print("senha digitada:", repr(senha))
        # print("tamanho:", len(senha.encode("utf-8")))
        senha_criptografada = bcrypt_context.hash(senha)
        novo_usuario = Usuario(nome,email,senha_criptografada)
        session.add(novo_usuario)
        session.commit()
        return{"mensagem":"usuario cadastrado com sucesso"}
    
    