"""Input parsing and validation helpers."""


def parse_topic(value: str) -> str:
    """Return a stripped topic, rejecting an empty value."""
    if not isinstance(value, str):
        raise ValueError("Topic must be text.")

    topic = value.strip()
    if not topic:
        raise ValueError("Topic cannot be empty.")
    return topic


def parse_duration(value: str) -> int:
    """Convert text to a positive integer duration."""
    if not isinstance(value, str):
        raise ValueError("Duration must be a positive whole number.")

    try:
        duration = int(value.strip())
    except ValueError as error:
        raise ValueError("Duration must be a positive whole number.") from error

    if duration <= 0:
        raise ValueError("Duration must be greater than zero.")
    return duration
