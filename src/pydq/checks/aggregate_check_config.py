from dataclasses import dataclass, field
from typing import Any, Dict, Optional, List
from decimal import Decimal
from .base_check_config import CheckConfig

################################        
### ColumnsAreCompleteCheck ####
################################
@dataclass(kw_only=True)
class ColumnsAreCompleteCheck(CheckConfig):
    columns: List[str]
    sparkdq_check: str = field(default="columns-are-complete-check", init=False, repr=False)

    def __post_init__(self):
        super().__post_init__()
        #Pendiente validaciones adicionales

################################        
##### ColumnPresenceCheck ######
################################
@dataclass(kw_only=True)
class ColumnPresenceCheck(CheckConfig):
    required_columns: list[str]
    sparkdq_check: str = field(default="column-presence-check", init=False, repr=False)

    def __post_init__(self):
        super().__post_init__()
        #Pendiente validaciones adicionales

#########################################        
##### CompletenessRatioCheckConfig ######
#########################################
@dataclass(kw_only=True)
class CompletenessRatioCheckConfig(CheckConfig):
    column: str
    min_ratio: float
    sparkdq_check: str = field(default="completeness-ratio-check", init=False, repr=False)

    def __post_init__(self):
        super().__post_init__()
        #Pendiente validaciones adicionales

    