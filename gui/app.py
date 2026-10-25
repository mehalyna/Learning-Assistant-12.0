"""Tkinter interface for the Learning Assistant."""

import tkinter as tk
from tkinter import messagebox

from study_toolkit.models import StudyTracker
from study_toolkit.validation import parse_duration, parse_topic
from study_toolkit.models import StudySession
from study_toolkit.storage import load_sessions, save_sessions


class LearningAssistantApp:
    """Build the starter interface for the study tracker."""

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Learning Assistant 13.0")
        self.root.geometry("460x430")
        self.tracker = StudyTracker()

        self._build_widgets()

    def _build_widgets(self) -> None:
        container = tk.Frame(self.root, padx=20, pady=18)
        container.grid(row=0, column=0, sticky="nsew")
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        container.columnconfigure(1, weight=1)

        heading = tk.Label(container, text="My Study Tracker", font=("TkDefaultFont", 16, "bold"))
        heading.grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 16))

        tk.Label(container, text="Topic").grid(row=1, column=0, sticky="w", pady=5)
        self.topic_entry = tk.Entry(container)
        self.topic_entry.grid(row=1, column=1, sticky="ew", pady=5)

        tk.Label(container, text="Duration (minutes)").grid(
            row=2, column=0, sticky="w", pady=5
        )
        self.duration_entry = tk.Entry(container)
        self.duration_entry.grid(row=2, column=1, sticky="ew", pady=5)

        self.add_button = tk.Button(
            container, text="Add Session", command=self.on_add_session
        )
        self.add_button.grid(row=3, column=0, columnspan=2, sticky="ew", pady=(8, 16))

        tk.Label(container, text="Recorded Sessions").grid(
            row=4, column=0, columnspan=2, sticky="w", pady=(0, 5)
        )
        self.sessions_listbox = tk.Listbox(container, height=8)
        self.sessions_listbox.grid(row=5, column=0, columnspan=2, sticky="nsew")
        container.rowconfigure(5, weight=1)

        self.total_label = tk.Label(container, text="Total Study Time: 0 minutes")
        self.total_label.grid(row=6, column=0, columnspan=2, sticky="w", pady=12)

        buttons = tk.Frame(container)
        buttons.grid(row=7, column=0, columnspan=2, sticky="ew")
        buttons.columnconfigure((0, 1), weight=1)
        self.save_button = tk.Button(
            buttons, text="Save Sessions", command=self.on_save_sessions
        )
        self.save_button.grid(row=0, column=0, sticky="ew", padx=(0, 5))
        self.load_button = tk.Button(
            buttons, text="Load Sessions", command=self.on_load_sessions
        )
        self.load_button.grid(row=0, column=1, sticky="ew", padx=(5, 0))

    def on_add_session(self) -> None:
        # LAB TODO 1 — Validate the entries, add a session and update the Listbox.
        pass

    def update_total(self) -> None:
        # CHALLENGE TODO 2 — Update the total-time label.
        pass

    def on_save_sessions(self) -> None:
        # CHALLENGE TODO 3 — Save the tracker to data/sessions.json.
        pass

    def on_load_sessions(self) -> None:
        # CHALLENGE TODO 4 — Load sessions and refresh the Listbox and total.
        pass
