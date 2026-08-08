import webbrowser
import subprocess


class BillieCommands:

    def execute(self, command):

        command = command.lower()

        # Websites
        if "youtube" in command:
            webbrowser.open("https://www.youtube.com")
            return "Opening YouTube."

        elif "github" in command:
            webbrowser.open("https://github.com")
            return "Opening GitHub."

        elif "google" in command:
            webbrowser.open("https://www.google.com")
            return "Opening Google."

        # Applications
        elif "chrome" in command:
            subprocess.Popen(
                r"C:\Program Files\Google\Chrome\Application\chrome.exe"
            )
            return "Opening Chrome."

        elif "calculator" in command:
            subprocess.Popen("calc.exe")
            return "Opening Calculator."

        elif "notepad" in command:
            subprocess.Popen("notepad.exe")
            return "Opening Notepad."

        return None