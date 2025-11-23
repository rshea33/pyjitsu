"""Data models for various moves."""

from pydantic import BaseModel

# TODO validate, build enums for most fields


class Submission(BaseModel):
    name: str
    from_pos: str
    executed: bool
    notes: str | None = None


class Sweep(BaseModel):
    name: str
    from_pos: str
    to_pos: str
    executed: bool
    notes: str | None = None


class Pass(BaseModel):
    name: str
    from_pos: str
    to_pos: str
    executed: bool
    notes: str | None = None
