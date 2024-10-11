import requests
import re


url = "https://justjoin.it/job-offers/all-locations/python?experience-level=junior"

def get_html():
    res = requests.get(url)
    return res.text
    


def get_jobs():
    job_offers = []
    html = get_html()
    path = 'href="/job-offer/'
    pattern = rf'{path}(.*?)"'
    jobs_source = re.findall(pattern, html)
    for job in jobs_source:
        full_path = f"https://justjoin.it/job-offer/{job}"
        job_offers.append(full_path)
    print(job_offers)
    
get_jobs()    
    
## Job offers for junior python dev JustJoinIt ^^^^^

## TO DO
# Get additional informations about job offer: Role, skills + level, location, remote/office, salary, post date
# Return how many jobs are avaible and number of new job offerings
# Trigger request at specific time, everyday
# Return some kind of notification

## Nice to have
# # test