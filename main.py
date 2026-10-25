"""Application entry point."""

import tkinter as tk

from gui.app import LearningAssistantApp


def main() -> None:
    """Create and run the application window."""
    root = tk.Tk()
    LearningAssistantApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
