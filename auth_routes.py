from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth",tags=["Auth"])

@auth_router.get("/")
async def autenticar():
    """
    Essa é a rota padrão de autenticação do nosso sistema
    """
    return {"Mensagem":"Você acessou a rota de autenticação","autenticado": False}