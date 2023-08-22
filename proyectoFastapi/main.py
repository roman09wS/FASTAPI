from fastapi import FastAPI,Request,Form,status
from fastapi.responses import HTMLResponse,RedirectResponse
from fastapi.templating import Jinja2Templates
#consola pip install python-multipart
app = FastAPI()
template = Jinja2Templates(directory='public/templates')

productos = [
    {"nombre":"computador","precio":5000,"stock":34},
    {"nombre":"iphone","precio":7000,"stock":22},
    {"nombre":"tv","precio":4000,"stock":55}
]

@app.get("/",response_class=HTMLResponse)
def inicio(request:Request):
    return template.TemplateResponse("index.html",{"request":request})

@app.get("/add_producto",response_class=HTMLResponse)
def add_producto(request:Request):
    return template.TemplateResponse("add_producto.html",{"request":request})

@app.get("/listar_producto",response_class=HTMLResponse)
def listar_producto(request:Request):
    return template.TemplateResponse("listar_producto.html",{"request":request,"productos":productos})

@app.get("/editar/{indice}/{nombre}/{precio}/{stock}",response_class=HTMLResponse)
def editar(request:Request,indice:int,nombre:str,precio:int,stock:int):
    return template.TemplateResponse("editar_producto.html",{"request":request,"indice":indice,"nombre":nombre,"precio":precio,"stock":stock})

@app.get("/saludo")
def saludo():
    return {"Saludo":"Hola mundo"}

@app.post("/agregar_producto",response_class=RedirectResponse)
def add_producto(request:Request,name : str = Form(...),price:int = Form(...),stock:int = Form(...)):
    productos.append({"nombre":name,"precio":price,"stock":stock})
    return RedirectResponse(url="/listar_producto", status_code=status.HTTP_303_SEE_OTHER)

@app.get("/eliminar/{indice}",response_class=RedirectResponse)
def delete_product(request:Request,indice:int):
    productos.pop(indice)
    return "/listar_producto"

@app.post("/update_product",response_class=RedirectResponse)
def update_product(request:Request,indice:int = Form(...),name:str = Form(...),price:int = Form(...),stock:int = Form(...)):
    productos[indice]["nombre"] = name
    productos[indice]["precio"] = price
    productos[indice]["stock"] = stock
    return RedirectResponse(url="/listar_producto",status_code=status.HTTP_303_SEE_OTHER)

@app.get("/respuesta",response_class=HTMLResponse)
def getSaludo(request:Request):
    return template.TemplateResponse("saludo.html",{"request":request})
