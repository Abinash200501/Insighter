from bs4 import BeautifulSoup
import requests

urls = [
    "https://roadmap.sh/machine-learning"]
#     "https://tripleten.com/blog/posts/how-to-become-machine-learning-engineer",
#     "https://www.datacamp.com/learn/career-paths/machine-learning-scientist",
#     "https://www.fullstackacademy.com/blog/how-to-become-machine-learning-engineer"
# ]

all_content = []

for url in urls:
    response = requests.get(url)
    print(dir(response))
    # Skip if login page
    if "login" in response.url or "login" in response.text.lower():
        print(f"Skipping {url} (login required)")
        continue
    
    # Scrape main article content (customize selector per site)
    soup = BeautifulSoup(response.text, "html.parser")
    main_content = soup.find("div", class_="post-title")  # adjust per site
    if main_content:
        text = main_content.get_text(separator="\n", strip=True)
        all_content.append(text)
    else:
        print(f"No content found for {url}")
