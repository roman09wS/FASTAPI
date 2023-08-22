from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

#Agregando los archivos estaticos que están en la carpeta dist del proyecto
app.mount("/static", StaticFiles(directory="public/dist"), name="static")

template = Jinja2Templates(directory='public/templates')

@app.get("/", response_class=HTMLResponse)
def inicio(request: Request):
    return template.TemplateResponse('index.html', {"request": request})

@app.get("/censo", response_class=HTMLResponse)
def pagCenso(request: Request):
    return template.TemplateResponse('censo.html', {"request": request})

@app.get("/ConceptosBasicos", response_class=HTMLResponse)
def pagConceptosBasicos(request: Request):
    return template.TemplateResponse('conceptosBasicos.html', {"request": request})

@app.get("/Estatutos", response_class=HTMLResponse)
def pagEstatutos(request: Request):
    return template.TemplateResponse('Estatutos.html', {"request", request })

@app.get("/Contrato_de_condiciones_uniformes", response_class=HTMLResponse)
def pagContrato_de_condiciones_uniformes(request: Request):
    return template.TemplateResponse('Contrato_de_condiciones_uniformes.html', {"request": request})

@app.get("/Invitacion_a_la_asamblea", response_class=HTMLResponse)
def pagInvitacion_a_la_asamblea(request: Request):
    return template.TemplateResponse('Invitacion_a_la_asamblea.html', {"request": request})

@app.get("/cuorum",response_class=HTMLResponse)
def pagCuorum(request:Request):
    return template.TemplateResponse("cuorum.html",{"request":request})

@app.get("/orden_dia",response_class=HTMLResponse)
def pagOrdenDia(request:Request):
    return template.TemplateResponse("orden_dia.html",{"request":request})

@app.get("/eleccion_comision",response_class=HTMLResponse)
def pagEleccion(request:Request):
    return template.TemplateResponse("eleccion_comision.html",{"request":request})

@app.get("/llamado_lista",response_class=HTMLResponse)
def pagLlamado(request:Request):
    return template.TemplateResponse("llamado_lista.html",{"request":request})
@app.get("/aprobacion_estatutos", response_class = HTMLResponse)
def pagAprobacion_estatutos(request: Request):
    return template.TemplateResponse("aprobacion_estatutos.html", {"request": request}) 

@app.get("/eleccion_junta_administradora", response_class = HTMLResponse)
def pagEleccion_junta_administradora(request: Request):
    return template.TemplateResponse("eleccion_junta_administradora.html", {"request": request}) 

@app.get("/aprobacion_acta_constitucion", response_class = HTMLResponse)
def PagAprobacion_acta_constitucion(request: Request):
    return template.TemplateResponse("aprobacion_acta_constitucion.html", {"request": request}) 
