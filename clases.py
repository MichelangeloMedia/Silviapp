from pydantic import BaseModel
import datetime
from typing import Optional

class Paciente(BaseModel):
    nombre: str
    apellido: str
    fecha_de_nac: datetime.date
    num_de_socio: int
    obra_social: str
    tel: Optional[int] = None
    email: Optional[str] = None

    @property
    def edad(self) -> int:
        today = datetime.date.today()
        birthday = self.fecha_de_nac
        return (
            today.year - birthday.year
            - ((today.month, today.day) < (birthday.month, birthday.day))
        )

paciente = Paciente(
    nombre="Santiago",
    apellido="Morrongiello",
    fecha_de_nac="2011-11-17",
    num_de_socio=12345,
    obra_social="Osecac"
)

print(f'{paciente.nombre} {paciente.apellido} tiene {paciente.edad} años')


