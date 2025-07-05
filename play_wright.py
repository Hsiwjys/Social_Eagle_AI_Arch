import asyncio
from playwright.async_api import async_playwright
import time

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        # Step 1: Open Bing
        await page.goto("https://www.bing.com", timeout=60000)

        # Step 2: Wait for the search box (your XPath)
        xpath = '//*[@id="sb_form_q"]'
        await page.wait_for_selector(f"xpath={xpath}", timeout=15000)

        # Step 3: Fill the textarea and press Enter
        await page.locator(f"xpath={xpath}").fill("CSK")
        await page.keyboard.press("Enter")

        # Step 4: Wait for results to appear
        await page.wait_for_selector("li a", timeout=15000)


        # Step 5: Get and print first result
        result = await page.locator("li a").first.text_content()

        for i in range(3):
            print(f"[{i+1}] CSK Search Result: {result}")
            time.sleep(2)

        await browser.close()

asyncio.run(run())
