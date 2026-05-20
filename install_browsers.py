import subprocess
import sys
import os

def install_playwright_browsers():
    """Install Playwright Chromium browser - runs once on startup"""
    marker = "/tmp/.playwright_installed"
    if not os.path.exists(marker):
        print("Installing Playwright Chromium...")
        subprocess.run(
            [sys.executable, "-m", "playwright", "install", "chromium"],
            check=True,
            capture_output=True
        )
        with open(marker, "w") as f:
            f.write("done")
        print("Playwright installed.")

install_playwright_browsers()
