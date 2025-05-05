from fastapi import FastAPI, HTTPException


app = FastAPI()
pacientes = []


@app.get("/")
def root():
    return {"Hello": "World"}


@app.post("/pacientes")
def post_paciente(paciente:str):
    pacientes.append(paciente)
    return pacientes


@app.get("/pacientes/{paciente_id}")
def get_paciente(paciente_id: int) -> str:
    if paciente_id < len(pacientes):
        return pacientes[paciente_id]
    else:
        raise HTTPException(status_code=404, detail="Éste paciente no existe")



