from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import time
import json

# URL
url = "https://sikkimtourism.gov.in/Public/TravellerEssentials/TravelAgents"

# Setup Chrome driver (auto installs correct version)
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 10)
driver.get(url)

# Function to click 'Show More' until all cards are loaded
def click_show_more():

    # ===================== THIRD OPTION ===========================

    print("GOING THROUGH 3RD OPTION ...")
    while True:
        try:
            show_more = driver.find_element(By.XPATH, "//button[contains(., 'Show More')]")
            driver.execute_script("arguments[0].scrollIntoView(true);", show_more)
            time.sleep(2)
            driver.execute_script("window.scrollBy(0, -100);")
            show_more.click()
            time.sleep(3)
        except NoSuchElementException:
            print("✅ All cards loaded — no Show More button.")
            break

    # ===================== SIXTH OPTION ===========================

    print("GOING THROUGH 6TH OPTION ...")
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            print("✅ Reached end of page.")
            break
        last_height = new_height


# Load all results
click_show_more()
time.sleep(2)

# Extract each card
cards = driver.find_elements(By.XPATH, "//div[@class='card mt-3 bookingCard']")
# //div[@class='col-12 p-3']
print(f"Found {len(cards)} travel agents... extracting info...")

output_lines = []
output_json = []

for card in cards:
    # Extract details safely
    def safe_text(xpath):
        try:
            return card.find_element(By.XPATH, xpath).text.strip()
        except:
            return "N/A"

    agency_name = safe_text("//span")
    location = safe_text("//label[@class='mb-1'][1]")
    phone = safe_text("//label[@class='mb-1'][2]")
    mail = safe_text("//label[@class='mb-0 ml-2']")

    # Collect activities (like Sight Seeing, Permits, etc.)
    try:
        activities = [
            span.text.strip()
            for span in card.find_elements(By.XPATH, ".//ul/li/label/span")
            if span.text.strip()
        ]
        activities_text = ", ".join(activities)
    except:
        activities = "N/A"

    data = f"""Agency name: {agency_name}
                Location: {location}
                Phone: {phone}
                Mail ID: {mail}
                Activities: {activities}
                \n--------------------------------------\n\n"""
    output_lines.append(data)

    # For JSON output
    json_data = {
        "Agency Name": agency_name,
        "Location": location,
        "Phone": phone,
        "Mail": mail,
        "Activities": activities,
    }
    output_json.append(json_data)

# Save data to text file
with open("sikkim_travel_agents.txt", "w", encoding="utf-8") as f:
    f.write("====== SIKKIM TRAVEL AGENCY CONTACT DETAILS =====\n\n")
    f.write("\n".join(output_lines))

# Save JSON file
with open("sikkim_travel_agents.json", "w", encoding="utf-8") as f:
    json.dump(output_json, f, indent=4, ensure_ascii=False)

print(f"✅ Successfully extracted {len(cards)} travel agents.")
print("📁 Data saved to: sikkim_travel_agents.txt")

driver.quit()
