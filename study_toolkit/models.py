"""Models for tracking study sessions."""


class StudySession:
    """A single topic and the time spent studying it."""

    def __init__(self, topic: str, duration: int) -> None:
        if not isinstance(topic, str) or not topic.strip():
            raise ValueError("Topic must be a non-empty string.")
        if isinstance(duration, bool) or not isinstance(duration, int):
            raise ValueError("Duration must be a positive integer.")
        if duration <= 0:
            raise ValueError("Duration must be a positive integer.")

        self.topic = topic.strip()
        self.duration = duration

    def describe(self) -> str:
        """Return a short, readable description of this session."""
        return f"{self.topic} ({self.duration} min)"


class StudyTracker:
    """Store study sessions and calculate their combined duration."""

    def __init__(self) -> None:
        self.sessions: list[StudySession] = []

    def add_session(self, session: StudySession) -> None:
        """Add a StudySession to the tracker."""
        if not isinstance(session, StudySession):
            raise ValueError("Session must be a StudySession.")
        self.sessions.append(session)

    def total_minutes(self) -> int:
        """Return the total duration of all recorded sessions."""
        return sum(session.duration for session in self.sessions)

    def get_descriptions(self) -> list[str]:
        """Return descriptions for all recorded sessions."""
        return [session.describe() for session in self.sessions]
