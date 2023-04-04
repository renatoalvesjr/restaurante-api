from typing import Annotated, Any

from fastapi import FastAPI, Path, Body, Response
#from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field

class Restaurante(BaseModel):
    nome: str
    endereco: str
    numero: str | None = Field(
        default=None, max_length=11
    )
    cnpj: str = Field(max_length=14)
    classificacao: float | None = Field(default=None, ge=0, le=5)
    
    class Config:
        schema_extra = {
            "restaurante":{
                "nome":"simple food",
                "endereco":"some place",
                "numero":"12987654321",
                "cnpj":"12345678901234",
                "classificacao":4.54
            }
        }


app = FastAPI()

'''@app.get("/")
def sla():
    return "Aoooooooooooooooba"
'''

@app.put("/restaurantes/{item_id}", response_model=Restaurante)
async def update_item(item_id: int, restaurante: Annotated[Restaurante, Body(embed=True)]) -> Any:
    json_encoded = jsonable_encoder(restaurante)
    results = {"item_id":item_id, "restaurante":restaurante}
    return results
