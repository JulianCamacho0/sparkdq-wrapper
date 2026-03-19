from dataclasses import dataclass, field
from typing import Any, Dict, Optional, List
from .base_check_config import CheckConfig

################################        
##### ColumnLessThanCheck ######
################################
@dataclass(kw_only=True)
class ColumnLessThanCheck(CheckConfig):
    column: str
    limit: str
    inclusive: bool = False
    sparkdq_check: str = field(default="column-less-than-check", init=False, repr=False)

    def __post_init__(self):
        super().__post_init__()
        self._require_str(self.column, "column")
        self._require_str(self.limit, "limit")
        if not isinstance(self.inclusive, bool):
            raise ValueError("inclusive debe ser de tipo bool")
            
####################################    
##### ColumnGreaterThanCheck #######
####################################
@dataclass(kw_only=True)
class ColumnGreaterThanCheck(CheckConfig):
    column: str
    limit: str
    inclusive: bool = False
    sparkdq_check: str = field(default="column-greater-than-check", init=False, repr=False)

    def __post_init__(self):
        super().__post_init__()
        self._require_str(self.column, "column")
        self._require_str(self.limit, "limit")
        if not isinstance(self.inclusive, bool):
            raise ValueError("inclusive debe ser de tipo bool")

################################        
##### DateBetweenCheck #########
################################
@dataclass(kw_only=True)
class DateBetweenCheck(CheckConfig):
    columns: List[str]
    min_value: str
    max_value: str
    inclusive: tuple[bool, bool] = (False, False)
    sparkdq_check: str = field(default="date-between-check", init=False, repr=False)

    def __post_init__(self):
        super().__post_init__()
        #Pendiente validadciones

################################        
######## DateMaxCheck ##########
################################
@dataclass(kw_only=True)
class DateMaxCheck(CheckConfig):
    columns: List[str]
    max_value: str
    inclusive: bool = False
    sparkdq_check: str = field(default="date-max-check", init=False, repr=False)

    def __post_init__(self):
        super().__post_init__()
        #Pendiente validaciones 

################################        
######## DateMinCheck ##########
################################
@dataclass(kw_only= True)
class DateMinCheck(CheckConfig):
    columns: List[str]
    min_value: str
    inclusive: bool = False
    sparkdq_check: str = field(default="date-min-check", init=False, repr=False)

    def __post_init__(self):
        super().__post_init__()
        #Pendiente validaciones adicionales

################################        
##### NotNullCkeckConfig #######
################################
@dataclass(kw_only=True)
class NotNullCkeckConfig(CheckConfig):
    columns: List[str]
    sparkdq_check: str = field(default="null-check", init=False, repr=False)
    
    def __post_init__(self):
        super().__post_init__()
        if len(self.columns) == 0:
            raise ValueError("'columns' debe ser una lista no vacía.")
        
##########################################        
##### ExactlyOneNotNullCheckConfig #######
##########################################
@dataclass(kw_only=True)
class ExactlyOneNotNullCheckConfig(CheckConfig):
    columns: List[str]
    sparkdq_check: str = field(default="exactly-one-not-null-check", init=False, repr=False)

    def __post_init__(self):
        super().__post_init__()
        #Pendiente otras validaciones