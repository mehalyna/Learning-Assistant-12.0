"""Unit tests for the study-tracking application core."""

import json
import tempfile
import unittest
from pathlib import Path

from study_toolkit.models import StudySession, StudyTracker
from study_toolkit.storage import load_sessions, save_sessions
from study_toolkit.validation import parse_duration, parse_topic


class StudySessionTests(unittest.TestCase):
    def test_valid_session_strips_topic(self) -> None:
        session = StudySession("  Python  ", 45)

        self.assertEqual(session.topic, "Python")
        self.assertEqual(session.duration, 45)

    def test_empty_topic_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            StudySession("   ", 45)

    def test_non_positive_duration_is_rejected(self) -> None:
        for duration in (0, -1):
            with self.subTest(duration=duration):
                with self.assertRaises(ValueError):
                    StudySession("Python", duration)

    def test_boolean_duration_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            StudySession("Python", True)

    def test_description_generation(self) -> None:
        self.assertEqual(StudySession("Python", 45).describe(), "Python (45 min)")


class StudyTrackerTests(unittest.TestCase):
    def test_total_calculation(self) -> None:
        tracker = StudyTracker()
        tracker.add_session(StudySession("Python", 45))
        tracker.add_session(StudySession("Mathematics", 60))

        self.assertEqual(tracker.total_minutes(), 105)
        self.assertEqual(
            tracker.get_descriptions(),
            ["Python (45 min)", "Mathematics (60 min)"],
        )


class ValidationTests(unittest.TestCase):
    def test_parse_valid_topic(self) -> None:
        self.assertEqual(parse_topic("  Python  "), "Python")

    def test_parse_valid_duration(self) -> None:
        self.assertEqual(parse_duration(" 45 "), 45)

    def test_invalid_duration_is_rejected(self) -> None:
        for value in ("", "abc", "1.5", "0", "-3"):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    parse_duration(value)


class StorageTests(unittest.TestCase):
    def test_json_save_load_round_trip(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            file_path = Path(directory) / "nested" / "sessions.json"
            tracker = StudyTracker()
            tracker.add_session(StudySession("Python", 45))
            tracker.add_session(StudySession("Mathematics", 60))

            save_sessions(tracker, file_path)
            loaded_tracker = load_sessions(file_path)

            self.assertEqual(
                loaded_tracker.get_descriptions(),
                ["Python (45 min)", "Mathematics (60 min)"],
            )
            with file_path.open(encoding="utf-8") as file:
                self.assertEqual(
                    json.load(file),
                    [
                        {"topic": "Python", "duration": 45},
                        {"topic": "Mathematics", "duration": 60},
                    ],
                )

    def test_missing_json_file_returns_empty_tracker(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            tracker = load_sessions(Path(directory) / "missing.json")

        self.assertEqual(tracker.sessions, [])

    def test_malformed_json_raises_decode_error(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            file_path = Path(directory) / "sessions.json"
            file_path.write_text("[", encoding="utf-8")

            with self.assertRaises(json.JSONDecodeError):
                load_sessions(file_path)

    def test_invalid_json_record_raises_value_error(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            file_path = Path(directory) / "sessions.json"
            file_path.write_text('[{"topic": "", "duration": 10}]', encoding="utf-8")

            with self.assertRaises(ValueError):
                load_sessions(file_path)


if __name__ == "__main__":
    unittest.main()
