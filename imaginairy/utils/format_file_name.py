import os
from urllib.parse import urlparse


class FileFormat:
    def __init__(self, format_template: str, directory: dict):
        self.format_template = format_template
        self.directory = directory

    def __str__(self):
        return format_filename(self.format_template, self.data)


def format_filename(format_template: str, data: dict) -> str:
    """
    Formats the filename based on the provided template and variables.
    """
    if not isinstance(format_template, str):
        raise TypeError("format argument must be a string")
    filename = format_template.format(**data)
    return filename


def get_url_file_name(url):
    parsed = urlparse(url)
    model_name, _ = os.path.splitext(os.path.basename(parsed.path))
    return model_name
