# 🏔️ Sikkim Tourism Travel Agents Scraper 🕵️‍♂️  
> *Because who wants to manually click “Show More” a hundred times?* 😤  

---

## 💡 The Grand Idea

Ever opened the [Sikkim Tourism “Travel Agents” page](https://sikkimtourism.gov.in/Public/TravellerEssentials/TravelAgents) and thought —  
> “Wow… this would make a great **automation project** if I had an **infinite patience bar**.”

So here it is — **a Python + Selenium script** that:
- Automatically clicks that infuriating **“Show More”** button 🔁  
- Scrolls *just right* (10px up, because aesthetics matter 💅)  
- Extracts every travel agency’s details like:
  - 🧭 Agency Name  
  - 📍 Location  
  - 📞 Phone Number  
  - 📧 Email Address  
  - 🎒 Activities/Services  
- And gracefully saves everything in both:
  - `sikkim_travel_agents.txt` 📄  
  - `sikkim_travel_agents.json` 🧾  

All without you lifting a single finger. (Except to run the script. Obviously.)

---

## ⚙️ Setup — The “Less Painful” Way

### 🐍 Requirements
You’ll need:
- Python 3.8+  
- Google Chrome  
- Internet (yeah, no surprises here)  

### 🧩 Dependencies
No manual ChromeDriver downloads, no crying in frustration. Just install everything in one go:

```bash
pip install selenium webdriver-manager
```

---

## 🚀 How to Run It Like a Pro

1. Clone this glorious repo:
   ```bash
   git clone https://github.com/<your_username>/sikkim-tourism-scraper.git
   cd sikkim-tourism-scraper
   ```

2. Run the script and let it do its magic:
   ```bash
   python sikkim_scraper.py
   ```

3. Sit back, sip your chai ☕, and watch Selenium do what humans shouldn’t have to:
   - It scrolls ✅  
   - It clicks ✅  
   - It extracts every last data bit ✅  

---

## 📦 Output Files

### 📝 `sikkim_travel_agents.txt`
A good ol’ text version for nostalgia fans.

```
Agency name: Ne Taxi T&T
Location: Tadong, Near Krishi Bhawan
Phone: 7872929029
Mail ID: book@ne.cab
Activities: Sight Seeing, Permits, Trekking, Cab, Hotel Booking
--------------------------------------
```

### 💾 `sikkim_travel_agents.json`
For the classy developers who speak in structured data.

```json
[
  {
    "Agency Name": "Ne Taxi T&T",
    "Location": "Tadong, Near Krishi Bhawan",
    "Phone": "7872929029",
    "Mail": "book@ne.cab",
    "Activities": [
      "Sight Seeing",
      "Permits",
      "Cab",
      "Hotel Booking"
    ]
  }
]
```

---

## 🔄 How It Works (a.k.a. *The Secret Sauce*)

```python
driver.execute_script("arguments[0].scrollIntoView(true); window.scrollBy(0, -10);", show_more)
```

Yes, that `-10px` is not a typo.  
That’s **precision engineering**, ensuring the “Show More” button stays perfectly visible and clickable. 🎯

Then, Selenium repeatedly:
1. Finds the button 👀  
2. Scrolls to it elegantly 💃  
3. Clicks it aggressively 💥  
4. Until no more are left 😌  

---

## 🧠 Why This Exists

Because **tourism websites** think users enjoy:
- Clicking the same button 47 times,  
- Watching pages lazily load data,  
- And then manually copying text into Excel.  

Spoiler: we don’t. 🤦‍♂️  
Hence, automation.  

---

## 🛠️ Tech Stack
| Component | Description |
|------------|-------------|
| 🐍 Python | The scripting backbone |
| 🧭 Selenium | The web automation hero |
| 🤖 WebDriver Manager | Because “downloading ChromeDriver” is so 2019 |
| 💾 JSON + TXT | Because someone always asks for both |

---

## 💬 Future Upgrades (a.k.a. “When I Feel Like It”)
- 🌐 Export to CSV or Excel  
- 📤 Push data directly to a REST API  
- 🧠 Add AI summary of top-rated agents (because why not?)  
- 🎨 Maybe a GUI (for the aesthetically inclined)

---

## ⚠️ Disclaimer
This project is for **educational & ethical use** only.  
Don’t break the website, don’t spam requests, and don’t blame me if you accidentally become the *#1 travel data supplier in Sikkim.* 😎

---

## ⭐ Bonus Tip
If this saved your sanity or your wrist from 100 clicks —  
**star** ⭐ this repo.  
It’s free, dopamine-inducing, and makes the world a slightly more automated place.

---

## 🧑‍💻 Author
**Nitin S Kumar**  
> Scrapping a data for travellers who wish to see icy mountains of-course & help to plan itinerary

Follow me for more projects that make lazy look efficient:
🔗 [LinkedIn](https://linkedin.com/in/nitin30kumar/) | 💻 [GitHub](https://github.com/nitinkumar30/)
