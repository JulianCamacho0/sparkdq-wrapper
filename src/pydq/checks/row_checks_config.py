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
        self._validate_columns(value=self.columns)
        self._validate_date(self.min_value, 'min_value')
        self._validate_date(self.max_value, 'max_value')
        self._validate_inclusive_tuple(self.inclusive)

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
        self._validate_columns(self.columns)
        self._validate_date(self.max_value, 'max_value')
        if not isinstance(self.inclusive, bool):
            raise ValueError("inclusive debe ser de tipo bool")

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
        self._validate_columns(self.columns)
        self._validate_date(self.min_value, 'min_value')
        if not isinstance(self.inclusive, bool):
            raise ValueError("inclusive debe ser de tipo bool")

##########################################        
##### ExactlyOneNotNullCheckConfig #######
##########################################
@dataclass(kw_only=True)
class ExactlyOneNotNullCheckConfig(CheckConfig):
    columns: List[str]
    sparkdq_check: str = field(default="exactly-one-not-null-check", init=False, repr=False)

    def __post_init__(self):
        super().__post_init__()
        self._validate_columns(self.columns)

##########################################        
######### IsContainedInCheck #############
##########################################
@dataclass(kw_only=True)
class IsContainedInCheck(CheckConfig):
    allowed_values: dict[str, list[object]]
    sparkdq_check: str = field(default="is-contained-in-check", init=False, repr=False)

    def __post_init__(self):
        super().__post_init__()
        self._require_dict_of_lists(self.allowed_values, 'allowed_values')

##########################################        
######### IsNotContainedInCheck ##########
##########################################
@dataclass(kw_only=True)
class IsNotContainedInCheck(CheckConfig):
    forbidden_values: dict[str, list[object]]
    sparkdq_check: str = field(default="is-not-contained-in-check", init=False, repr=False)

    def __post_init__(self):
        super().__post_init__()
        self._require_dict_of_lists(self.forbidden_values, 'forbidden_values')

################################        
##### NotNullCheck #############
################################
@dataclass(kw_only=True)
class NotNullCheck(CheckConfig):
    columns: List[str]
    sparkdq_check: str = field(default="not-null-check", init=False, repr=False)
    
    def __post_init__(self):
        super().__post_init__()
        self._validate_columns(self.columns)
        
################################        
######### NullCheck ###########
################################
@dataclass(kw_only=True)
class NullCheck(CheckConfig):
    columns: List[str]
    sparkdq_check: str = field(default="null-check", init=False, repr=False)
    
    def __post_init__(self):
        super().__post_init__()
        self._validate_columns(self.columns)
        
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
        self._validate_columns(self.columns)
        self._validate_inclusive_tuple(self.inclusive)
        if not isinstance(self.min_value, (int, float, Decimal)):
            raise ValueError(f'min_value debe ser de tipo float o int o Decimal')
        if not isinstance(self.max_value, (int, float, Decimal)):
            raise ValueError(f'max_value deber ser de tipo float o int o Decimal')

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
        self._validate_columns(self.columns)
        if not isinstance(self.max_value, (int, float, Decimal)):
            raise ValueError(f'max_value deber ser de tipo float o int o Decimal')
        if not isinstance(self.inclusive, bool):
            raise ValueError("inclusive debe ser de tipo bool")

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
        self._validate_columns(self.columns)
        if not isinstance(self.min_value, (int, float, Decimal)):
            raise ValueError(f'min_value deber ser de tipo float o int o Decimal')
        if not isinstance(self.inclusive, bool):
            raise ValueError("inclusive debe ser de tipo bool")


##########################################        
############ RegexMatchCheck #############
##########################################
@dataclass(kw_only=True)
class RegexMatchCheck(CheckConfig):
    column: str
    pattern: str
    ignore_case: bool = False
    treat_null_as_failure: bool = False
    sparkdq_check: str = field(default= "regex-match-check", init=False, repr=False)

    def __post_init__(self):
        super().__post_init__()
        self._require_str(self.column, field='column')
        self._require_str(self.pattern)
        if not isinstance(self.ignore_case, bool):
            raise ValueError("ignore_case debe ser de tipo bool")
        if not isinstance(self.treat_null_as_failure, bool):
            raise ValueError("treat_null_as_failure debe ser de tipo bool")

##########################################        
####### StringLengthBetweenCheck #########
##########################################
@dataclass(kw_only=True)
class StringLengthBetweenCheck(CheckConfig):
    column: str
    min_length: int
    max_length: int
    inclusive: tuple[bool, bool] = (True, True)
    sparkdq_check: str = field(default= "string-length-between-check", init=False, repr=False)

    def __post_init__(self):
        super().__post_init__()
        self._require_str(self.column, field='column')
        self._validate_inclusive_tuple(self.inclusive)
        if not isinstance(self.min_length, int):
            raise ValueError(f'min_length debe ser de tipo int')
        if not isinstance(self.max_length, int):
            raise ValueError(f'max_length deber ser de tipo int')

##########################################        
########## StringMaxLengthCheck ##########
##########################################
@dataclass(kw_only=True)
class StringMaxLengthCheck(CheckConfig):
    column: str
    max_length: int
    inclusive: bool = True
    sparkdq_check: str = field(default= "string-max-length-check", init=False, repr=False)

    def __post_init__(self):
        super().__post_init__()
        self._require_str(self.column,'column')
        if not isinstance(self.max_length, int):
            raise ValueError(f'max_length deber ser de tipo int')
        if not isinstance(self.inclusive, bool):
            raise ValueError(f'inclusive deber ser de tipo bool')

##########################################        
########## StringMinLengthCheck ##########
##########################################
@dataclass(kw_only=True)
class StringMinLengthCheck(CheckConfig):
    column: str
    min_length: int
    inclusive: bool = True
    sparkdq_check: str = field(default= "string-min-length-check", init=False, repr=False)

    def __post_init__(self):
        super().__post_init__()
        self._require_str(self.column,'column')
        if not isinstance(self.min_length, int):
            raise ValueError(f'min_length deber ser de tipo int')
        if not isinstance(self.inclusive, bool):
            raise ValueError(f'inclusive deber ser de tipo bool')
        

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
        self._validate_columns(self.columns)
        self._validate_timestamp(self.min_value, 'min_value')
        self._validate_timestamp(self.max_value, 'max_value')
        self._validate_inclusive_tuple(self.inclusive)

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
        self._validate_columns(self.columns)
        self._validate_timestamp(self.max_value, 'max_value')
        if not isinstance(self.inclusive, bool):
            raise ValueError('inclusive debe ser de tipo bool')

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
        self._validate_columns(self.columns)
        self._validate_timestamp(self.min_value, 'min_value')
        if not isinstance(self.inclusive, bool):
            raise ValueError('inclusive debe ser de tipo bool')
