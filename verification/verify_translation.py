
from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the local index.html file
        # Since I'm in the root of the repo, I can use the absolute path
        cwd = os.getcwd()
        page.goto(f"file://{cwd}/index.html")

        # Wait for the language button to be visible
        page.wait_for_selector("#langBtn")

        # Take a screenshot of the initial state (English)
        page.screenshot(path="verification/step1_english.png")
        print("Screenshot 1: English state captured.")

        # Click the language button to switch to Finnish
        page.click("#langBtn")

        # Wait a bit for DOM updates (though they are synchronous in my code, good practice)
        page.wait_for_timeout(500)

        # Check if text changed
        # "Enter Player Name" -> "Anna pelaajan nimi"
        # "Category" -> "Kategoria"

        # Take a screenshot of the Finnish state
        page.screenshot(path="verification/step2_finnish.png")
        print("Screenshot 2: Finnish state captured.")

        browser.close()

if __name__ == "__main__":
    run()
