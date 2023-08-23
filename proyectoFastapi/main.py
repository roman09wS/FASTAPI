from fastapi import FastAPI,Request,Form,status
from fastapi.responses import HTMLResponse,RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import databases


#consola pip install python-multipart
#pip install fastapi databases
#pip install --upgrade databases

app = FastAPI()
app.mount("/static", StaticFiles(directory="public/static"), name="static")
template = Jinja2Templates(directory='public/templates')

DATABASE_URL = "mysql://root:@localhost/personas"
database = databases.Database(DATABASE_URL)

productos = [
    {"nombre":"computador","precio":5000,"stock":34},
    {"nombre":"iphone","precio":7000,"stock":22},
    {"nombre":"tv","precio":4000,"stock":55}
]


@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

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

@app.get("/usuarios/{user_id}")
async def read_user(user_id: int):
    query = "SELECT * FROM usuarios WHERE id_user = :user_id"
    values = {"user_id": user_id}
    user = await database.fetch_one(query=query, values=values)
    if user is None:
        return {"message": "Usuario no encontrado"}
    return user

@app.get("/crear/{nombre}/{correo}")
async def add_user(nombre: str,correo:str):
    query = "INSERT INTO usuarios (nombre,correo) VALUES (:nombre,:correo)"
    values = {"nombre": nombre,"correo":correo}
    await database.execute(query=query, values=values)
    return {"msg":"Agregado exitosamente"}

@app.get("/crear_user",response_class=HTMLResponse)
def crear_user(request:Request):
    return template.TemplateResponse("crear_user.html",{"request":request})

@app.post("/agregar_usuario",response_class=RedirectResponse)
async def add_producto(nombre : str = Form(...),correo:str = Form(...)):
    query = "INSERT INTO usuarios (nombre,correo) VALUES (:nombre,:correo)"
    values = {"nombre": nombre,"correo":correo}
    await database.execute(query=query, values=values)
    return RedirectResponse(url="/listar_usuarios", status_code=status.HTTP_303_SEE_OTHER)

@app.get("/getUser")
async def getuser():
    query = "SELECT * FROM usuarios"
    user = await database.fetch_all(query=query)
    if user is None:
        {"msg":"Falla en la consulta"}
    return user

@app.get("/listar_usuarios", response_class=HTMLResponse)
async def getUsuarios(request: Request):
    usuarios = await getuser()
    return template.TemplateResponse("listar_usuarios.html", {"request": request, "usuarios": usuarios})

@app.get("/editar_usuario/{id}/{nombre}/{correo}",response_class=HTMLResponse)
def editar_user(request:Request,id:int,nombre:str,correo:str):
    return template.TemplateResponse("editar_usuario.html",{"request":request,"id":id,"nombre":nombre,"correo":correo})

@app.get("/eliminar_usuario/{id}",response_class=RedirectResponse)
async def eliminar_user(request:Request,id:int):
    query = "DELETE FROM usuarios WHERE id_user = :id"
    values = {"id":id}
    await database.execute(query=query,values=values)
    return "/listar_usuarios"

@app.post("/update_user",response_class=RedirectResponse)
async def update_user(request:Request,id:int=Form(...),nombre:str=Form(...),correo:str=Form(...)):
    query = "UPDATE usuarios SET correo = :correo,nombre = :nombre WHERE id_user = :id"
    values = {"id":id,"nombre": nombre,"correo":correo}
    await database.execute(query=query, values=values)
    return RedirectResponse(url="/listar_usuarios",status_code=status.HTTP_303_SEE_OTHER)
