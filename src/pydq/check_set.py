from dataclasses import dataclass, field
from typing import Any, Dict, List, Iterable, Optional, Union
import json
from pathlib import Path
from .checks.row_checks import CheckConfig 

@dataclass
class CheckSetConfig:
    """
    Contenedor de configuración para un set de checks.

    - name: nombre del set
    - checks: lista de CheckConfig
    """
    name: Optional[str] = None
    checks: List[CheckConfig] = field(default_factory=list)

    def __post_init__(self):
        self._require_str(self.name, "name")
        if not isinstance(self.checks, list):
            raise TypeError("'checks' debe ser una lista de CheckConfig.")
        self.validate()

    def add(self, check: CheckConfig) -> "CheckSetConfig":
        """Agrega un check config al set."""
        self._require_check(check)
        self.checks.append(check)
 
    def validate(self) -> None:
        if not self.checks:
            raise ValueError("El CheckSetConfig debe tener al menos 1 check.")

        # Todos deben ser CheckConfig
        for i, c in enumerate(self.checks):
            if not isinstance(c, CheckConfig):
                raise TypeError(f"checks[{i}] no es CheckConfig: {type(c)}")

        # IDs únicos
        ids = [c.id for c in self.checks]
        dup = self._find_duplicates(ids)
        if dup:
            raise ValueError(f"Hay IDs duplicados en el CheckSetConfig: {sorted(dup)}")
            
    @property
    def critical_checks(self) -> List[CheckConfig]:
        return [c for c in self.checks if c.severity == "critical"]

    @property
    def warning_checks(self) -> List[CheckConfig]:
        return [c for c in self.checks if c.severity == "warning"]

    def group_by_severity(self) -> Dict[str, List[CheckConfig]]:
        """Devuelve {'critical': [...], 'warning': [...]}"""
        return {
            "critical": self.critical_checks,
            "warning": self.warning_checks,
        }

    def get_ids(self) -> List[Dict[str, Any]]:
        if not self.checks:
            return []
        return [c.get_id() for c in self.checks]

    def to_sparkdq_dicts(self) -> List[Dict[str, Any]]:
        if not self.checks:
            return []
        return [c.to_sparkdq_dict() for c in self.checks]

    def to_sparkdq_json(self, *, indent: int = 2, ensure_ascii: bool = False) -> str:
        payload = self.to_sparkdq_dicts()
        return json.dumps(payload, indent=indent, ensure_ascii=ensure_ascii)

    @staticmethod
    def _require_str(value: Any, field_name: str):
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"'{field_name}' debe ser un string no vacío.")

    @staticmethod
    def _require_check(check: Any):
        if not isinstance(check, CheckConfig):
            raise TypeError(f"El objeto debe ser CheckConfig, llegó: {type(check)}")

    @staticmethod
    def _find_duplicates(items: List[str]) -> set:
        seen = set()
        dup = set()
        for x in items:
            if x in seen:
                dup.add(x)
            seen.add(x)
        return dup