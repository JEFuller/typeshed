from datetime import datetime
from typing import TypedDict

from typing_extensions import Unpack

from apscheduler.triggers.interval import IntervalTrigger


class ModifyJobParams(TypedDict, total=False):
    next_run_time: datetime


class Job():
    def modify(self, **kwargs: Unpack[ModifyJobParams]) -> None: ...
    def remove(self) -> None: ...

    @property
    def name(self) -> str: ...

    @property
    def trigger(self) -> IntervalTrigger: ...
