import asyncio
from playwright.async_api import async_playwright

EDGE_PATH = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
USER_DATA_DIR = "edge_gmail_session"

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch_persistent_context(
            user_data_dir=USER_DATA_DIR,
            headless=False,
            executable_path=EDGE_PATH,
            args=["--start-maximized"]
        )

        page = await browser.new_page()

        # Navigate to Gmail
        await page.goto("https://mail.google.com/", timeout=60000)

        try:
            # Wait for inbox to load
            await page.wait_for_selector("tr.zA", timeout=20000)
        except:
            print("🔐 Please log in to Gmail manually in Edge.")
            print("⏳ Waiting 2 minutes for login...")
            await page.wait_for_timeout(120000)

        # Click on first (latest) email
        await page.locator("tr.zA").first.click()

        # Wait and extract email body
        await page.wait_for_selector("div.a3s", timeout=15000)
        body = await page.locator("div.a3s").first.inner_text()

        print("\n📬 Latest Email:\n")
        print(body)

        await browser.close()

asyncio.run(main())
