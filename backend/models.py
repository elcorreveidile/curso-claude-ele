"""Pydantic models for request/response payloads."""
from typing import Any, Literal, Optional

from pydantic import BaseModel, EmailStr, Field


class LoginRequest(BaseModel):
    email: EmailStr


class VerifyTokenRequest(BaseModel):
    token: str


class UserOut(BaseModel):
    id: str
    email: str
    name: Optional[str] = None
    role: Literal["student", "admin"] = "student"
    created_at: str


class CheckoutRequest(BaseModel):
    name: str = Field(..., min_length=1, max_length=80)
    email: EmailStr
    origin_url: str


class SubmissionIn(BaseModel):
    content: str = Field(..., min_length=1, max_length=10000)


class FeedbackIn(BaseModel):
    feedback: str = Field(..., min_length=1, max_length=5000)


class ModuleProgressOut(BaseModel):
    id: str
    module_id: str
    status: Literal["locked", "available", "in_progress", "completed"]
    unlocked_at: Optional[str] = None
    completed_at: Optional[str] = None


class ModuleOut(BaseModel):
    id: str
    num: str
    title: str
    subtitle: str
    hours: int
    optional: bool
    status: Literal["locked", "available", "in_progress", "completed"]
    videos: list[dict] = []
    readings: list[dict] = []
    activities: list[dict] = []


class TaskOut(BaseModel):
    id: str
    module_id: str
    title: str
    description: str
    duration: str
    requires_submission: bool


class SubmissionOut(BaseModel):
    id: str
    content: str
    submitted_at: str
    feedback: Optional[str] = None
    feedback_at: Optional[str] = None


class CertificateOut(BaseModel):
    name: str
    verification_code: str
    issued_at: str


class AdminStatsOut(BaseModel):
    total_enrollments: int
    active_students: int
    completed_modules: int
    pending_feedback: int


class ParticipantOut(BaseModel):
    id: str
    email: str
    name: Optional[str] = None
    enrolled_at: str
    status: str
    completed_modules: int
    total_modules: int


class SessionOut(BaseModel):
    id: str
    session_num: int
    title: str
    scheduled_at: Optional[str] = None
    zoom_link: Optional[str] = None
    recording_url: Optional[str] = None
    status: Literal["scheduled", "completed", "cancelled"]
