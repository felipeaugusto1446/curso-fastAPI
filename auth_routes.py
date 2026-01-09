from fastapi import APIRouter, Depends,HTTPException
from models import Usuario
from dependencies import pegar_sessao
from main import bcrypt_context
from schemas import UsuarioSchema
from sqlalchemy.orm import Session
auth_router = APIRouter(prefix="/auth",tags=["Auth"])

@auth_router.get("/")
async def autenticar():
    """
    Essa é a rota padrão de autenticação do nosso sistema
    """
    return {"Mensagem":"Você acessou a rota de autenticação","autenticado": False}

@auth_router.post("/criar_conta")
async def criar_conta(usuario_schemas:UsuarioSchema, session:Session = Depends(pegar_sessao)):
    usuario = session.query(Usuario).filter(Usuario.email==usuario_schemas.email).first()
    if usuario:
        #já existe um usuario com esse email
        raise HTTPException(status_code=400,detail="Email do usuario ja cadastrado")
    else:
        # print("senha digitada:", repr(senha))
        # print("tamanho:", len(senha.encode("utf-8")))
        senha_criptografada = bcrypt_context.hash(usuario_schemas.senha)
        novo_usuario = Usuario(usuario_schemas.nome,usuario_schemas.email,senha_criptografada,usuario_schemas.ativo,usuario_schemas.admin)
        session.add(novo_usuario)
        session.commit()
        return{"mensagem":f"usuario cadastrado com sucesso{usuario_schemas.email}"}
    
    