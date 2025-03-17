from typing_extensions import Self

unicode = str
__tracebackhide__: bool

class StringMixin:
    def is_equal_to_ignoring_case(self, other: str) -> Self: ...
    def contains_ignoring_case(self, *items: str) -> Self: ...
    def starts_with(self, prefix: str) -> Self: ...
    def ends_with(self, suffix: str) -> Self: ...
    def matches(self, pattern: str) -> Self: ...
    def does_not_match(self, pattern: str) -> Self: ...
    def is_alpha(self) -> Self: ...
    def is_digit(self) -> Self: ...
    def is_lower(self) -> Self: ...
    def is_upper(self) -> Self: ...
    def is_unicode(self) -> Self: ...
