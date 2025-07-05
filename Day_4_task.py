import pyautogui
import time

# using alt+tab to switch to the browser
pyautogui.hotkey('alt', 'tab')
# Wait for a moment to ensure the browser is focused
time.sleep(2)
# click new tab button
pyautogui.hotkey('ctrl', 't')  # Open a new tab in the browser
time.sleep(1)  # Wait for the new tab to open
pyautogui.click(x=764, y=97)  # Click at specific coordinates to focus on the browser

time.sleep(2)  # Wait for 2 seconds to ensure the browser is focused

pyautogui.typewrite("https://forms.gle/JgPD8HSJiY3VjYU37", interval=0.1)  # Type with a delay between each character
pyautogui.press("enter")  # Press the Enter key to navigate to the URL
time.sleep(5)  # Wait for the page to load

# Fill out the form
pyautogui.click(x=807, y=851)  # Click on the first input field
pyautogui.typewrite("abcdef", interval=0.1)  # Type the name
pyautogui.press("tab")  # Move to the next field   
pyautogui.typewrite("absdef@gmail.com", interval=0.1)  # Type the email
pyautogui.press("tab")  # Move to the next field
pyautogui.typewrite("9876543210", interval=0.1)  # Type the phone number
pyautogui.press("tab")  # Move to the next field
pyautogui.typewrite("This is a test message.", interval=0.1)  # Type the message
pyautogui.press("tab")  # Move to the submit button
pyautogui.press("enter")  # Submit the form
