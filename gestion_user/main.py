from fastapi import FastAPI,Request,Form,status
from fastapi.responses import HTMLResponse,RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import databases

app = FastAPI()
app.mount("/static", StaticFiles(directory="public/static"), name="static")
template = Jinja2Templates(directory='public/templates')

DATABASE_URL = "mysql://root:@localhost/gestion_user"
database = databases.Database(DATABASE_URL)

#pip install databases


@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/crear_user",response_class=HTMLResponse)
def interfaz_user(request:Request):
    return template.TemplateResponse('crear_usuario.html',{"request":request})

@app.post("/addUsuario",response_class=RedirectResponse)
async def add_user(request:Request,nombre:str=Form(...),cargo:str=Form(...),ciudad:str=Form(...),edad:str=Form(...),salario:str=Form(...)):
    query = "INSERT INTO usuarios (nombre,cargo,ciudad,edad,salario) VALUES (:nombre,:cargo,:ciudad,:edad,:salario)"
    values = {"nombre": nombre,"cargo":cargo,"ciudad":ciudad,"edad":edad,"salario":salario}
    await database.execute(query=query, values=values)
    return RedirectResponse(url="/tabla",status_code=status.HTTP_303_SEE_OTHER)

@app.get("/getUser")
async def getuser():
    query = "SELECT * FROM usuarios"
    user = await database.fetch_all(query=query)
    if user is None:
        {"msg":"Falla en la consulta"}
    return user

@app.get("/", response_class=HTMLResponse)
async def getUsuarios(request: Request):
    return template.TemplateResponse("login.html", {"request": request})

@app.get("/index", response_class=HTMLResponse)
async def getUsuarios(request: Request):
    usuarios = await getuser()
    return template.TemplateResponse("index.html", {"request": request})

@app.get("/error", response_class=HTMLResponse)
async def getUsuarios(request: Request):
    usuarios = await getuser()
    return template.TemplateResponse("404.html", {"request": request})
    

@app.get("/tabla", response_class=HTMLResponse)
async def getUsuarios(request: Request):
    usuarios = await getuser()
    return template.TemplateResponse("tabla.html", {"request": request, "usuarios": usuarios,"mensaje":"Obtenidos con exito"})

@app.post("/login",response_class=RedirectResponse)
async def principal(request:Request,name:str = Form(...),passw:str=Form(...)):
    query = "SELECT * FROM admin WHERE nombre = :name AND passw = :passw LIMIT 1"
    values = {"name":name,"passw":passw}
    usuario = await database.fetch_one(query=query, values=values)
    if usuario is None:
        return RedirectResponse(url="/error",status_code=status.HTTP_303_SEE_OTHER)
    else:
        return RedirectResponse(url="/index",status_code=status.HTTP_303_SEE_OTHER)

@app.get("/modificar_user",response_class=HTMLResponse)
async def modi(request:Request):
    usuarios = await getuser()
    return template.TemplateResponse("modificar_usuario.html", {"request": request,"usuarios":usuarios,"lista_deactivate":"active"})

@app.get("/eliminar_user",response_class=HTMLResponse)
async def plantilla_eliminar(request:Request):
    usuarios = await getuser()
    return template.TemplateResponse("eliminar_usuario.html", {"request": request,"usuarios":usuarios,"lista_deactivate":"active"})

@app.get("/editar_usuario/{id_user}",response_class=HTMLResponse)
async def editar(request:Request,id_user:int):
    query = "SELECT * FROM usuarios WHERE id_user = :id_user LIMIT 1"
    values = {"id_user":id_user}
    usuario = await database.fetch_one(query=query, values=values)
    return template.TemplateResponse("modificar_usuario.html", {"request": request,"usuario":usuario,"activate":"activate form"})

@app.post("/update_user",response_class=RedirectResponse)
async def update_user(request:Request,id_user:str = Form(...),nombre:str = Form(...),cargo:str = Form(...),ciudad:str = Form(...),edad:str = Form(...),salario:str = Form(...)):
    query = "UPDATE usuarios SET nombre = :nombre,cargo = :cargo,ciudad = :ciudad,edad = :edad,salario = :salario WHERE id_user = :id_user"
    values = {"id_user":id_user,"nombre": nombre,"cargo":cargo,"ciudad":ciudad,"edad":edad,"salario":salario}
    await database.execute(query=query, values=values)
    return RedirectResponse(url="/tabla",status_code=status.HTTP_303_SEE_OTHER)

@app.get("/eliminar_usuario/{id_user}",response_class=HTMLResponse)
async def delete(request:Request,id_user:int):
    query = "SELECT * FROM usuarios WHERE id_user = :id_user LIMIT 1"
    values = {"id_user":id_user}
    usuario = await database.fetch_one(query=query,values=values)
    return template.TemplateResponse("eliminar_usuario.html", {"request": request,"usuario":usuario,"activate":"activate form"})

@app.post("/delete_user",response_class=RedirectResponse)
async def delete_user(id_user:int=Form(...)):
    query = "DELETE FROM usuarios WHERE id_user = :id_user"
    values = {"id_user":id_user}
    await database.execute(query=query,values=values)
    return RedirectResponse(url="/tabla",status_code=status.HTTP_303_SEE_OTHER)
