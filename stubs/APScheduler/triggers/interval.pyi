from datetime import timedelta


class IntervalTrigger():

    @property
    def interval(self) -> timedelta: ...
