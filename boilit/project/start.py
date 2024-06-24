"""functions for validating and generating output data for the start page."""

from agility.utils.pydantic import validate_data
from boilit.schemas.input import MetaInput


def validate_meta_input(meta_input):
    """
    Check if the meta_input data is valid.
    """
    meta_input, errors = validate_data(meta_input, MetaInput)
    return meta_input, errors
