from fastapi import FastAPI

app = FastAPI()

#rotaraiz

@app.get("/")
def raiz():
    return{"API ONLINE":"Digite /docs na URL para acessar o contéudo"}


basedados = {

    "item":[
    {

        "id": 1,
        "produto":"sabonete",
        "valor":4.00,
        "quantidade":800,
    },
    {
        "id": 2,
        "produto":"sabão em pó",
        "valor":15.80,
        "quantidade":400,
    }

    ]

}

# Rota Get ALL
@app.get("/itens")  # endpoint usuários
def get_todos_os_itens():
    return basedados


# Rota GET ID

@app.get("/usuarios/{id_itens}")
def get_by_id(id: int):
    for indice in range(len(basedados['item'])):
        if id == basedados['item'][indice]['id']:
            return basedados['items']
    #este for percorre todos os itens da array[basedados['item']] até identificar um compatível com o descrito pelo usuário.
    return {"Erro": 404, "Mensagem": "Usuário não encontrado"}  ##else não é necessário

@app.get("/qtditens")
def qtditens():
    return{"Quantidade de itens": len(basedados)}


@app.get("/somavalores")
def somavalores():
    qtd = len(basedados['item'])
    valores = []
    for indice in range(qtd):
        valores.append(basedados['item'][indice]['valor'])
    return sum(valores)

@app.get("/for")
def howUsefor():
    return basedados

