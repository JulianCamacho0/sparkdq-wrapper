from dataclasses import dataclass, asdict, field
from typing import Any, Dict, Optional, Literal, List
from datetime import datetime
Severity = Literal["critical", "warning"]

def clean_none(d: dict) -> dict:
        """Elimina claves con valor None (para no ensuciar el JSON/YAML)."""
        return {k: v for k, v in d.items() if v is not None}

@dataclass(kw_only=True)
class CheckConfig:
    id: str
    sparkdq_check: str = field(default="", init=False, repr=False)
    severity: Severity = "critical"
    description: Optional[str] = None

    def __post_init__(self):
        self._require_str(self.id, "id")

        sev = (self.severity or "critical").strip().lower()
        if sev not in ("critical", "warning"):
            raise ValueError("severity debe ser 'critical' o 'warning'")
        object.__setattr__(self, "severity", sev)

        if self.description is not None and not isinstance(self.description, str):
            raise ValueError("description debe ser string o None")

    def get_id(self) -> Dict[str, Any]:
        
        out: Dict[str, Any] = {
            "check-id": self.id,
            "severity": self.severity
        }

        return out
        
    def to_sparkdq_dict(self) -> Dict[str, Any]:
            """
            Devuelve un dict compatible con SparkDQ add_checks_from_dicts().
            """
            if not self.sparkdq_check:
                raise ValueError(
                    f"{self.__class__.__name__} debe definir sparkdq_check (ej: 'null-check')."
                )
    
            raw = asdict(self)
    
            # Base SparkDQ
            out: Dict[str, Any] = {
                "check": self.sparkdq_check,
                "check-id": raw.pop("id"),
                "severity": raw.pop('severity')
            }
            
            raw.pop("description", None)
            raw.pop("sparkdq_check", None)
    
            # Resto de params => kebab-case
            for k, v in raw.items():
                out[k.replace("_", "-")] = v
    
            return clean_none(out)


    @staticmethod
    def _require_str(value: Any, field: str):
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{field} debe ser un string no vacío.")
        
    @staticmethod
    def _validate_date(value: Any, field: str):
        if not isinstance(value, str):
            raise ValueError(f'{field} debe ser un string en YYYY-MM-DD formato.')
        try:
            datetime.strptime(value, "%Y-%m-%d").date()
        except:
             raise ValueError(f'{field} debe estar en formato YYYY-MM-DD')
        
    @staticmethod
    def _validate_columns(value: Any):
         
         if not isinstance(value, List):
            raise ValueError('columns debe ser de tipo Lis.')
         else:
              if len(value) == 0:
                   raise ValueError('columns debe ser una lista no vacia.')
              for c in value:
                   if not isinstance(c, str) or not c.strip():
                    raise ValueError(f"Los elementos de 'columns' deben ser un string no vacío.")
    
    @staticmethod
    def _validate_inclusive_tuple(value: Any):
        if not isinstance(value, tuple):
            raise ValueError('inclusive debe ser de tipo tuple')
        else:
            for b in value:
                if not isinstance(b, bool):
                    raise ValueError("Los elementos de 'inclusive' deben ser de tipo bool")
                
    @staticmethod
    def _require_dict_of_lists(value: Any, field: str):
        
        if not isinstance(value, dict):
            raise ValueError(f"Se esperaba un diccionario dict[str, list], pero se recibió: {type(value).__name__}")
        
        if not value:
            raise ValueError(f"{field} debe ser un diccionario no debe estar vacío.")
        
        for key, lst in value.items():
            if not isinstance(key, str):
                raise ValueError(f"Todas las claves del diccionario {field} deben ser strings. Clave inválida: {key}")

            if not isinstance(lst, list):
                raise ValueError(
                    f"Todos los valores del diccionario {field} deben ser listas. La clave '{key}' tiene un valor de tipo: {type(lst).__name__}"
                )
            if not lst:
                raise ValueError(f"La lista asociada a la clave '{key}' del diccionario {field} no debe estar vacía.")
            
    @staticmethod
    def _validate_timestamp(value: Any, field: str):
       
        if isinstance(value, str):
            try:
                return datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                raise ValueError(
                    f"Formato de timestamp inválido: '{value}'. "
                    "Se esperaba 'YYYY-MM-DD HH:MM:SS'."
                )

        raise ValueError(
            f"{field} debe ser un timestamp (datetime o string válido), pero se recibió: {type(value).__name__}"
        )






    
    
