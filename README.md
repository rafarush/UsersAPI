<h1>Gestor de Ususarios (API)</h1>
<h2>Info...</h2>


<h3>Guia para hcaer APIs</h3>
<code> from fastapi import FastAPI
app = FastAPI()
</code>
<p>
Se inicia server con: uvicorn main:app --reload
La forma generica es: uvicorn '<nombreDelArchivoPython>:<nombreDeLaInstanciaFastApi>' 

Documentacion con Swagger: http://127.0.0.1:8000/docs    ||  La forma generica: <url>/docs
Documentacion con Redocly: http://127.0.0.1:8000/redoc   ||  La forma generica: <url>/redoc
</p>
