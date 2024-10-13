import requests
import re


url = "https://justjoin.it/job-offers/all-locations/python?experience-level=junior"


def main():
    jobs = get_jobs_from_file()
    save_jobs_to_file()
    

def get_html():
    res = requests.get(url)
    return res.text
    

def get_jobs_net():
    job_offers = []
    html = get_html()
    path = 'href="/job-offer/'
    pattern = rf'{path}(.*?)"'
    jobs_source = re.findall(pattern, html)
    for job in jobs_source:
        full_path = f"https://justjoin.it/job-offer/{job}"
        job_offers.append(full_path)
    print(job_offers)
    
def get_jobs_from_file():
    job_offers = []
    with open("output.html", "r", encoding='utf-8') as file:
        html = file.read()
    path = 'href="/job-offer/'
    pattern = rf'{path}(.*?)"'
    jobs_source = re.findall(pattern, html)
    for job in jobs_source:
        full_path = f"https://justjoin.it/job-offer/{job}"
        job_offers.append(full_path)
    return job_offers   


def save_jobs_to_file():
    with open ("Jobs.txt", "w") as file:
        for job in jobs:
            file.write(f"{job}\n")
          



## Job offers for junior python dev JustJoinIt ^^^^^

## TO DO
# Get additional informations about job offer: Role, skills + level, location, remote/office, salary, post date
# Return how many jobs are avaible and number of new job offerings
# Trigger request at specific time, everyday
# Return some kind of notification

## Nice to have
# # test