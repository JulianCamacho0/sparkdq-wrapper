from dataclasses import dataclass, asdict, field
from typing import Any, Dict, Optional, Literal, List

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
            raise ValueError(f"'{field}' debe ser un string no vacío.")

    
    
