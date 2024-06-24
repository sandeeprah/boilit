"""
beat.config.schemas.input
 
This module contains the Pydantic schemas for the page input data.
"""

from typing import List, Optional, Dict
import uuid

from pydantic import BaseModel, Field, field_validator, model_validator


class MetaInput(BaseModel):
    file_name: str
    client_name: Optional[str]
    project_name: Optional[str]
    project_description: Optional[str]


class ProjectData(BaseModel):
    meta_input: MetaInput
    page1_input: Dict
    page2_input: Dict
