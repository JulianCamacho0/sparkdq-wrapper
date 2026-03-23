from dataclasses import dataclass, field
from typing import Any, Dict, Optional, List, Literal
from decimal import Decimal
from .base_check_config import CheckConfig

FreshnessPeriod = Literal["year", "month", "week", "day", "hour", "minute", "second"]

################################        
### ColumnsAreCompleteCheck ####
################################
@dataclass(kw_only=True)
class ColumnsAreCompleteCheck(CheckConfig):
    columns: List[str]
    sparkdq_check: str = field(default="columns-are-complete-check", init=False, repr=False)

    def __post_init__(self):
        super().__post_init__()
        self._validate_columns(self.columns)

################################        
##### ColumnPresenceCheck ######
################################
@dataclass(kw_only=True)
class ColumnPresenceCheck(CheckConfig):
    required_columns: list[str]
    sparkdq_check: str = field(default="column-presence-check", init=False, repr=False)

    def __post_init__(self):
        super().__post_init__()
        self._validate_columns(self.required_columns)

#########################################        
####### CompletenessRatioCheck ##########
#########################################
@dataclass(kw_only=True)
class CompletenessRatioCheck(CheckConfig):
    column: str
    min_ratio: float
    sparkdq_check: str = field(default="completeness-ratio-check", init=False, repr=False)

    def __post_init__(self):
        super().__post_init__()
        self._require_str(self.column, 'column')
        if not isinstance(self.min_ratio, float):
            raise ValueError('min_ratio debe ser de tipo float')
        else:
            if self.min_ratio<0.0 or self.min_ratio>1.0:
                raise ValueError('min_ratio debe estar en [0,1]')

#########################################        
####### RowCountBetweenCheck ############
#########################################
@dataclass(kw_only=True)
class RowCountBetweenCheck(CheckConfig):
    min_count: int
    max_count: int
    sparkdq_check: str = field(default="row-count-between-check", init=False, repr=False)

    def __post_init__(self):
        super().__post_init__()
        if not isinstance(self.min_count, int):
            raise ValueError('min_count debe ser de tipo int.')
        if not isinstance(self.max_count, int):
            raise ValueError('max_count debe ser de tipo int.')
        if self.min_count>= self.max_count:
            raise ValueError('min_count debe ser menor que max_count.')

#########################################        
####### RowCountExactCheck ##############
#########################################
@dataclass(kw_only=True)
class RowCountExactCheck(CheckConfig):
    expected_count : int
    sparkdq_check: str = field(default="row-count-exact-check", init=False, repr=False)

    def __post_init__(self):
        super().__post_init__()
        if not isinstance(self.expected_count, int):
            raise ValueError('expected_count debe ser de tipo int.')

#########################################        
####### RowCountMinCheck ################
#########################################
@dataclass(kw_only=True)
class RowCountMinCheck(CheckConfig):
    min_count : int
    sparkdq_check: str = field(default="row-count-min-check", init=False, repr=False)

    def __post_init__(self):
        super().__post_init__()
        if not isinstance(self.min_count, int):
            raise ValueError('min_count debe ser de tipo int.')

#########################################        
####### RowCountMaxCheck ################
#########################################
@dataclass(kw_only=True)
class RowCountMaxCheck(CheckConfig):
    max_count : int
    sparkdq_check: str = field(default="row-count-max-check", init=False, repr=False)

    def __post_init__(self):
        super().__post_init__()
        if not isinstance(self.max_count, int):
            raise ValueError('max_count debe ser de tipo int')

#########################################        
######### FreshnessCheck ################
#########################################
@dataclass(kw_only=True)
class FreshnessCheck(CheckConfig):
    column: str
    period: FreshnessPeriod
    interval: int
    sparkdq_check: str = field(default="freshness-check", init=False, repr=False)

    def __post_init__(self):
        super().__post_init__()
        self._require_str(self.column, 'column')
        if self.period not in ["year", "month", "week", "day", "hour", "minute", "second"]:
            raise ValueError('period debe ser: year, mont, week, day, hour, minute o second')
        if not isinstance(self.interval, int):
            raise ValueError('interval debe ser de tipo int')

#########################################        
######### ForeignKeyCheck ###############
#########################################
@dataclass(kw_only=True)
class ForeignKeyCheck(CheckConfig):
    column: str
    reference_dataset: str
    reference_column: str
    sparkdq_check: str = field(default="foreign-key-check", init=False, repr=False)

    def __post_init__(self):
        super().__post_init__()
        self._require_str(self.column, 'column')
        self._require_str(self.reference_column, 'reference_column')
        self._require_str(self.reference_dataset, 'reference_dataset')

#########################################        
######### DistinctRatioCheck ############
#########################################
@dataclass(kw_only=True)
class DistinctRatioCheck(CheckConfig):
    column: str
    min_ratio: float
    sparkdq_check: str = field(default="distinct-ratio-check", init=False, repr=False)

    def __post_init__(self):
        super().__post_init__()
        self._require_str(self.column)
        if not isinstance(self.min_ratio, float):
            raise ValueError('min_ratio debe ser de tipo float')
        else:
            if self.min_ratio<0.0 or self.min_ratio>1.0:
                raise ValueError('min_ratio debe estar entre 0.0 y 1.0')

#########################################        
############ SchemaCheck ################
#########################################
@dataclass(kw_only=True)
class SchemaCheck(CheckConfig):
    expected_schema: dict[str, str]
    strict: bool = True
    sparkdq_check: str = field(default="schema-check", init=False, repr=False)

    def __post_init__(self):
        super().__post_init__()
        if not isinstance(self.expected_schema, dict):
            raise ValueError('expected_schema debe ser de tipo dict')
        for k,v in self.expected_schema.items():
            if not isinstance(k, str):
                raise ValueError('Las llaves y valores del diccionario expected_schema deben ser de tipo str')
            if not isinstance(v, str):
                raise ValueError('Las llaves y valores del diccionario expected_schema deben ser de tipo str')
        if not isinstance(self.strict, bool):
            raise ValueError('strict debe ser de tipo bool')

#########################################        
############ UniqueRatioCheck ###########
#########################################
@dataclass(kw_only=True)
class UniqueRatioCheck(CheckConfig):
    column: str 
    min_ratio: float
    sparkdq_check: str = field(default="unique-ratio-check", init=False, repr=False)

    def __post_init__(self):
        super().__post_init__()
        self._require_str(self.column, 'column')
        if not isinstance(self.min_ratio, float):
            raise ValueError('min_ratio debe ser de tipo float')
        if self.min_ratio<0.0 or self.min_ratio>1.0:
            raise ValueError('min_ratio debe estar entre 0.0 y 1.0')

#########################################        
############ UniqueRowsCheck ############
#########################################
@dataclass(kw_only=True)
class UniqueRowsCheck(CheckConfig):
    subset_columns: Optional[List[str]] = None
    sparkdq_check: str = field(default="unique-rows-check", init=False, repr=False)

    def __post_init__(self):
        super().__post_init__()
        if self.subset_columns is not None:
            self._validate_columns(self.subset_columns)
    