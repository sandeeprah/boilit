from typing import Dict, Tuple

from agility.skeleton.project import DashProject


class Project(DashProject):
    """
    Represents a project in the Beat application.

    Attributes:
        None

    Methods:
        validate_project_data(data): Validates the project data.
        get_progress(data): Calculates the progress of the project.

    """

    @staticmethod
    def validate_project_data(data: dict) -> Tuple[dict, list]:
        """
        Validates the project data.

        Args:
            data (any): The project data to be validated.

        Returns:
            tuple: A tuple containing the validated project data and a list of error messages, if any.

        """
        error_messages = []
        return data, error_messages

    @staticmethod
    def get_progress(data: dict) -> Dict[str, int]:
        """
        Calculates the progress of the project.

        Args:
            data (dict): The project data.

        Returns:
            dict: A dictionary containing the progress of the project.

        """
        progress = {}
        progress["Start"] = 0

        if data is None:
            return progress

        if data is not None:
            progress["Start"] = 2

        if "page_one_input" in data:
            progress["Page One"] = 1
        if "page_one_output" in data:
            progress["Page One"] = 2

        if "page_two_input" in data:
            progress["Page Two"] = 1

        if "page_two_output" in data:
            progress["Page Two"] = 2

        if "facility_input" in data:
            progress["Facility Information"] = 1

        return progress
