from dataclasses import dataclass, field
from typing import Any, Dict, Optional, List
from decimal import Decimal
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

##########################################        
######### IsContainedInCheck #############
##########################################
@dataclass(kw_only=True)
class IsContainedInCheck(CheckConfig):
    allowed_values: dict[str, list[object]]
    sparkdq_check: str = field(default="is-contained-in-check", init=False, repr=False)

    def __post_init__(self):
        super().__post_init__()
        #Pendiente otras validaciones

##########################################        
######### IsNotContainedInCheck ##########
##########################################
@dataclass(kw_only=True)
class IsNotContainedInCheck(CheckConfig):
    forbidden_values: dict[str, list[object]]
    sparkdq_check: str = field(default="is-not-contained-in-check", init=False, repr=False)

    def __post_init__(self):
        super().__post_init__()
        #Pendiente otras validaciones

################################        
##### NotNullCheck #######
################################
@dataclass(kw_only=True)
class NotNullCheck(CheckConfig):
    columns: List[str]
    sparkdq_check: str = field(default="not-null-check", init=False, repr=False)
    
    def __post_init__(self):
        super().__post_init__()
        if len(self.columns) == 0:
            raise ValueError("'columns' debe ser una lista no vacía.")
        
################################        
######### NullCheck ###########
################################
@dataclass(kw_only=True)
class NullCheck(CheckConfig):
    columns: List[str]
    sparkdq_check: str = field(default="null-check", init=False, repr=False)
    
    def __post_init__(self):
        super().__post_init__()
        if len(self.columns) == 0:
            raise ValueError("'columns' debe ser una lista no vacía.")
        
##########################################        
######### NumericBetweenCheck ##########
##########################################
@dataclass(kw_only=True)
class NumericBetweenCheck(CheckConfig):
    columns: List[str]
    min_value: float | int | Decimal
    max_value: float | int | Decimal
    inclusive:  tuple[bool, bool] = (False, False)
    sparkdq_check: str = field(default="numeric-between-check", init=False, repr=False)

    def __post_init__(self):
        super().__post_init__()
        #Pendiente otras validaciones

##########################################        
############ NumericMaxCheck #############
##########################################
@dataclass(kw_only=True)
class NumericMaxCheck(CheckConfig):
    columns: List[str]
    max_value: float | int | Decimal
    inclusive: bool = False
    sparkdq_check: str = field(default="numeric-max-check", init=False, repr=False)

    def __post_init__(self):
        super().__post_init__()
        #Pendiente otras validaciones

##########################################        
############ NumericMinCheck #############
##########################################
@dataclass(kw_only=True)
class NumericMinCheck(CheckConfig):
    columns: List[str]
    min_value: float | int | Decimal
    inclusive: bool = False
    sparkdq_check: str = field(default= "numeric-min-check", init=False, repr=False)

    def __post_init__(self):
        super().__post_init__()
        #Pendiente otras validaciones

##########################################        
############ RegexMatchCheck #############
##########################################
@dataclass(kw_only=True)
class RegexMatchCheck(CheckConfig):
    columns: str
    pattern: str
    ignore_case: bool = False
    treat_null_as_failure: bool = False
    sparkdq_check: str = field(default= "regex-match-check", init=False, repr=False)

    def __post_init__(self):
        super().__post_init__()
        #Pendiente otras validaciones

##########################################        
####### StringLengthBetweenCheck #########
##########################################
@dataclass(kw_only=True)
class StringLengthBetweenCheck(CheckConfig):
    columns: str
    min_length: int
    max_length: int
    inclusive: tuple[bool, bool] = (True, True)
    sparkdq_check: str = field(default= "string-length-between-check", init=False, repr=False)

    def __post_init__(self):
        super().__post_init__()
        #Pendiente otras validaciones

##########################################        
########## StringMaxLengthCheck ##########
##########################################
@dataclass(kw_only=True)
class StringMaxLengthCheck(CheckConfig):
    columns: str
    max_length: int
    inclusive: bool = True
    sparkdq_check: str = field(default= "string-max-length-check", init=False, repr=False)

    def __post_init__(self):
        super().__post_init__()
        #Pendiente otras validaciones

##########################################        
########## StringMinLengthCheck ##########
##########################################
@dataclass(kw_only=True)
class StringMinLengthCheck(CheckConfig):
    columns: str
    min_length: int
    inclusive: bool = True
    sparkdq_check: str = field(default= "string-min-length-check", init=False, repr=False)

    def __post_init__(self):
        super().__post_init__()
        #Pendiente otras validaciones

##########################################        
########## TimestampBetweenCheck #########
##########################################
@dataclass(kw_only=True)
class TimestampBetweenCheck(CheckConfig):
    columns: List[str]
    min_value: str
    max_value: str
    inclusive: tuple[bool, bool]
    sparkdq_check: str = field(default= "timestamp-between-check", init=False, repr=False)

    def __post_init__(self):
        super().__post_init__()
        #Pendiente otras validaciones

##########################################        
########## TimestampMaxCheck #############
##########################################
@dataclass(kw_only=True)
class TimestampMaxCheck(CheckConfig):
    columns: List[str]
    max_value: str
    inclusive: bool = False
    sparkdq_check: str = field(default= "timestamp-max-check", init=False, repr=False)

    def __post_init__(self):
        super().__post_init__()
        #Pendiente otras validaciones

##########################################        
########## TimestampMinCheck #############
##########################################
@dataclass(kw_only=True)
class TimestampMinCheck(CheckConfig):
    columns: List[str]
    min_value: str
    inclusive: bool = False
    sparkdq_check: str = field(default= "timestamp-min-check", init=False, repr=False)

    def __post_init__(self):
        super().__post_init__()
        #Pendiente otras validaciones

