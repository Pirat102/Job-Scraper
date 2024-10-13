from bs4 import BeautifulSoup
import requests


BASIC_URL = "https://justjoin.it"

with open("output.html", "r", encoding="UTF8") as f:
    html = f.read()
    

soup = BeautifulSoup(html, 'html.parser')

jobs_list = soup.find('div', {'data-test-id': 'virtuoso-item-list'})


def get_each_job_offer(jobs_list):
    job_offers = jobs_list.find_all('div', {'data-index': True})
    
    for job_offer in job_offers:
        job_title = job_offer.find("h3").text.strip()
        job_offer_link = f"{BASIC_URL}{job_offer.a['href']}"
        print(f"{job_title}, {job_offer_link}")

        return job_title, job_offer_link
    
        #res = requests.get(job_offer_link)
        ## HTML TO FILE
        # with open("job.html", "a", encoding="UTF8") as f:
        #     f.write(f"{res.text}\n")

job_title, job_offer_link = get_each_job_offer(jobs_list)
print(job_offer_link)


# res = requests.get(job_offers)
# # HTML TO FILE
# with open("job.html", "a", encoding="UTF8") as f:
#     f.write(f"{res.text}\n")


        
with open ("job.html", "r", encoding="UTF8") as file:
    job_html = file.read()




## Job req + skills
def n():
    soup2 = BeautifulSoup(job_html, "html.parser")

    job_requirments = soup2.find_all(class_="MuiTypography-root MuiTypography-subtitle2 css-7de92v")

    if job_requirments:
        for job_req in job_requirments[1]:
            level = soup2.find(class_="MuiTypography-root MuiTypography-subtitle4 css-1wcj8lw")
            print(f"Job requir: {job_req.text} - {level.text}")
    ...
        
    


