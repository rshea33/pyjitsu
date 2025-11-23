"""Model for jiu-jitsu sessions."""

from datetime import date
from typing import Literal

from pydantic import BaseModel

from .moves import Pass, Submission, Sweep

MOVE = Submission | Sweep | Pass


INTENSITY = Literal["low", "med", "high"]


class Roll(BaseModel):
    duration_minutes: float | None = None
    intensity: INTENSITY | None = None
    goal: str | None = None
    techniques: list[MOVE]
    notes: str | None = None


class Technique(BaseModel):
    name: str
    from_position: str
    to_position: str | None = None
    type: Literal["submission", "sweep", "pass"]
    notes: str | None = None


class Session(BaseModel):
    session_type: Literal["class", "open mat", "private lesson", "competition"]
    class_type: Literal["gi", "nogi"] | None = None
    date: date
    techniques: list[Technique] | None = None
    rolls: list[Roll] | None = None
    notes: str | None = None
