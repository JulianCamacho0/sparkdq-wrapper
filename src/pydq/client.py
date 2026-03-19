from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Optional, Union

from .runner import SparkDQRunner


@dataclass
class PyDQ:
    """
    Cliente 
      - Se instancia con un SparkSession (con conexión a LZ)
      - Internamente crea el Runner
    """
    spark: Any
    runner = SparkDQRunner()

    def run_df(
        self,
        df: Any,
        checkset: Any
    ) -> Dict[str, Any]:
        
        return self.runner.run_df(df, checkset)

    def run_table(
        self,
        table_name: str,
        checkset: Any
    ) -> Dict[str, Any]:
        
        df = self.spark.table(table_name)
        return self.run_df(df, checkset)

   
   