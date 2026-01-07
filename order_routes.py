from fastapi import APIRouter

order_router = APIRouter(prefix="/pedidos",tags=["pedidos"])

#isso é um decorator, é uma linha que código que você coloca antes de uma função com um @, que atribui uma funcionalidade nova pra função criada abaixo
@order_router.get("/")
async def pedidos():
    """
    Essa é a rota padrão de pedidos do nosso sistema. Todas as rotas dos pedidos precisam de autenticação
    """
    return {"mensagem":"Você acessou a rota de pedidos"}
    