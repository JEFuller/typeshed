from typing import Any, Callable, TypedDict

from apscheduler.job import Job
from typing_extensions import Unpack


class AddJobParams(TypedDict, total=False):
    seconds: int
    minutes: int
    hours: int
    name: str


class BaseScheduler():
    def add_job(self, c: Callable[[], Any],
                trigger: str, **kwargs: Unpack[AddJobParams]) -> Job: ...

    def start(self) -> None: ...

    def shutdown(self, wait: bool = True) -> None: ...

    @property
    def running(self) -> bool: ...

    def get_jobs(self) -> list[Job]: ...
