from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends
from dependencies import pegar_sessao
from schemas import PedidoSchema
from models import Pedido

order_router = APIRouter(prefix="/pedidos",tags=["pedidos"])

#isso é um decorator, é uma linha que código que você coloca antes de uma função com um @, que atribui uma funcionalidade nova pra função criada abaixo
@order_router.get("/")
async def pedidos():
    """
    Essa é a rota padrão de pedidos do nosso sistema. Todas as rotas dos pedidos precisam de autenticação
    """
    return {"mensagem":"Você acessou a rota de pedidos"}
    
@order_router.post("/pedidos")
async def criar_pedido(pedidoSchema:PedidoSchema,session:Session = Depends(pegar_sessao)):
    novo_pedido = Pedido(usuario=pedidoSchema.id_usuario)
    session.add(novo_pedido)
    session.commit()
    return{"Mensagem":f"Pedido criado com sucesso. Id pedido:{novo_pedido.id}"}