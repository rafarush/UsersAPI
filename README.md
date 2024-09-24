<h1>Gestor de Ususarios (API)</h1>
<h2>Info...</h2>


<h3>Guia para hacer APIs con FastApi</h3>
<p>Se importa clase FastApi:</p><code>from fastapi import FastAPI<p>Se instancia la clase FastApi:</p>app = FastAPI()</code>
  
<p><br><br>
Se inicia server con: uvicorn main:app --reload
La forma generica es: uvicorn "<<nombreDelArchivoPython>>:<<nombreDeLaInstanciaFastApi>>" <br>

Documentacion con Swagger: http://127.0.0.1:8000/docs (La forma generica: <url>/docs)<br>
Documentacion con Redocly: http://127.0.0.1:8000/redoc (La forma generica: <url>/redoc)<br>
</p>
