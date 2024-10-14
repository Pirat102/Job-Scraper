from bs4 import BeautifulSoup
import requests
import json


BASIC_URL = "https://justjoin.it"
URL = "https://justjoin.it/job-offers/all-locations/python?experience-level=junior"


def main():
    html = get_jobs_html(URL)
    offers = get_each_job_title_link(html)
    jobs = get_job_requirements(offers)
    save_jobs_to_file(jobs)
    

def get_jobs_html(link):
    res = requests.get(link)
    return res.text

## Return dictionary title:link
def get_each_job_title_link(html):
    jobs = {}
    
    soup = BeautifulSoup(html, 'html.parser')
    jobs_list = soup.find('div', {'data-test-id': 'virtuoso-item-list'})
    job_offers = jobs_list.find_all('div', {'data-index': True})
    
    ## Get job title, link and create dictionary
    for job_offer in job_offers:
        job_title = job_offer.find("h3").text.strip()
        job_offer_link = f"{BASIC_URL}{job_offer.a['href']}"
        
        jobs[job_title] = job_offer_link
    return jobs


## Get job req + skills. Return nested job offer
def get_job_requirements(offers):
    for title, link in offers.items():
        res = requests.get(link)
        soup = BeautifulSoup(res.text, "html.parser")
        
        each_div = soup.find_all("div", class_="MuiBox-root css-jfr3nf")
        skills = {}
        
        ## Get job req
        for div in each_div:
            skill = div.h4.text.strip()
            level = div.span.text.strip()
            if skill and level:
                skills[skill] = level
                
        ## Combine job offer into dictionary    
        offers[title] = {
            "skills" : skills,
            "link" : link
            }
    return offers


        
def save_jobs_to_file(jobs):
    with open ("Python_jobs.json", "w", encoding="UTF8") as file:
        json.dump(jobs, file, ensure_ascii=False, indent=4)




if __name__ == "__main__":
    main()


