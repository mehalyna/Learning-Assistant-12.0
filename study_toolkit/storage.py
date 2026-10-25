"""JSON storage helpers for study sessions."""

import json
from pathlib import Path

from study_toolkit.models import StudySession, StudyTracker


def save_sessions(tracker: StudyTracker, file_path: str | Path) -> None:
    """Write all tracker sessions to a JSON file."""
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    records = [
        {"topic": session.topic, "duration": session.duration}
        for session in tracker.sessions
    ]

    with path.open("w", encoding="utf-8") as file:
        json.dump(records, file, indent=2, ensure_ascii=False)


def load_sessions(file_path: str | Path) -> StudyTracker:
    """Load sessions from JSON, returning an empty tracker if absent."""
    path = Path(file_path)
    try:
        with path.open("r", encoding="utf-8") as file:
            records = json.load(file)
    except FileNotFoundError:
        return StudyTracker()

    if not isinstance(records, list):
        raise ValueError("Session data must be a JSON list.")

    sessions: list[StudySession] = []
    for index, record in enumerate(records):
        if not isinstance(record, dict):
            raise ValueError(f"Session record {index + 1} must be an object.")
        if "topic" not in record or "duration" not in record:
            raise ValueError(
                f"Session record {index + 1} must include topic and duration."
            )
        try:
            session = StudySession(record["topic"], record["duration"])
        except ValueError as error:
            raise ValueError(f"Invalid session record {index + 1}: {error}") from error
        sessions.append(session)

    tracker = StudyTracker()
    for session in sessions:
        tracker.add_session(session)
    return tracker
