# Learning Assistant 13.0 — Desktop Edition

A beginner-friendly starter project for **SoftServe Academy — Python Fundamentals, Session 13: Building Desktop Applications with Tkinter**.

## Learning objectives

By working through this project, you will practise:

- Separating application logic from a graphical user interface.
- Creating a desktop interface with Tkinter widgets and `grid()`.
- Validating user input and responding to errors.
- Working with lists and updating a Listbox.
- Saving and restoring structured data as JSON.

## Requirements and running the project

Use Python 3.10 or later. Tkinter is included with many Python installations. Check whether it is available by running:

```text
python -m tkinter
```

Launch the application from the project root:

```text
python main.py
```

Run the core tests with:

```text
python -m unittest discover -s tests -v
```

## Project structure

- `main.py` starts the application.
- `study_toolkit/` contains the study-session model, input validation and JSON storage logic.
- `gui/` contains the Tkinter application.
- `tests/` checks the application core without opening a window.
- `data/sessions.json` is the suggested location for saved sessions.

The application logic in `study_toolkit/` can be tested independently of the GUI. The code in `gui/` presents that logic to the user through a desktop interface.

## Student tasks

### Implementation Lab — 25 minutes, no AI

1. **LAB TODO 1 — `on_add_session()`**: read and validate the entries, add a session, update the Listbox, clear the entries after success and show validation errors.

### Engineering Challenge — 30 minutes, AI allowed

2. **CHALLENGE TODO 2 — `update_total()`**: display the total study time.
3. **CHALLENGE TODO 3 — `on_save_sessions()`**: save the tracker to `data/sessions.json`.
4. **CHALLENGE TODO 4 — `on_load_sessions()`**: restore sessions, refresh the Listbox and total, and report invalid stored data without losing the current tracker.

## Manual verification checklist

- [ ] Start the application and confirm the title, fields, buttons and empty sessions list are visible.
- [ ] After completing the lab, add a valid session and check the displayed description.
- [ ] Try blank or invalid values and confirm the application reports the problem without closing.
- [ ] After completing the challenge, save sessions, restart the application and load them.
- [ ] Run the core tests using the command above.

## Troubleshooting

- If `python -m tkinter` reports that Tkinter is unavailable, install or select a Python distribution that includes Tk support. On some Linux distributions, Tkinter is provided by a separate system package.
- If the application cannot open a graphical window, run it in a desktop environment with a graphical display. Remote or headless terminals may not provide one.