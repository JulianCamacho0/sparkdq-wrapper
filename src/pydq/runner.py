import time
import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Sequence, Union
from .check_set import CheckSetConfig

class SparkDQRunner:
    """
    Runner que ejecuta SparkDQ debajo
    """

    def __init__(self, strict: bool = True):
        self.strict = strict

    def run_df(
        self,
        df: Any,
        checkset_config: CheckSetConfig
    ) -> Dict[str, Any]:
        """
        Ejecuta SparkDQ sobre un DataFrame.

        :param df: pyspark.sql.DataFrame
        :param checkset_config: tu CheckSetConfig con to_sparkdq_dicts
        """
    
        start = time.time()
        try:
            #Imports lazy para no romper import del paquete si sparkdq no está instalado
            from sparkdq.management import CheckSet as SparkDQCheckSet
            from sparkdq.engine import BatchDQEngine
            from sparkdq.core import Severity

            #Crear CheckSet de SparkDQ y cargar dicts
            sparkdq_checkset = SparkDQCheckSet()
            sparkdq_checkset.add_checks_from_dicts(json.loads(checkset_config.to_sparkdq_json()))

    
            #Ejecutar engine
            engine = BatchDQEngine(sparkdq_checkset)
            result = engine.run_batch(df)

            elapsed_ms = int((time.time() - start) * 1000)

            #Construir salida amigable
            summary_obj = result.summary()
            summary = self._summary_to_dict(summary_obj)

            out: Dict[str, Any] = {
                "status": "ok",
                "processing_time_ms": elapsed_ms,
                "checks": checkset_config.get_ids(),  
                "summary": summary
            }

            return out

        except Exception as e:
            elapsed_ms = int((time.time() - start) * 1000)
            msg = f"Error ejecutando SparkDQ (elapsed_ms={elapsed_ms}): {e}"
            return {"status": "error", "processing_time_ms": elapsed_ms, "error": msg}

   

    def _summary_to_dict(self, summary_obj: Any) -> Dict[str, Any]:
        """
        Convierte el summary de SparkDQ a dict de manera defensiva.
        """
        # si ya es dict
        if isinstance(summary_obj, dict):
            return  summary_obj

        # si tiene to_dict
        if hasattr(summary_obj, "to_dict") and callable(summary_obj.to_dict):
            try:
                return summary_obj.to_dict()
            except Exception:
                pass

        # si es dataclass/pydantic-like
        if hasattr(summary_obj, "__dict__"):
            d = dict(summary_obj.__dict__)
            # normaliza a tipos serializables
            return self._make_json_safe(d)

        # fallback
        return {"value": str(summary_obj)}

  