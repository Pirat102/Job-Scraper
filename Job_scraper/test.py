from project import *

with open("test_offers.html", "r", encoding="UTF8") as f:
        html = f.read()

offers = get_each_job_title_link(html)
print(offers)
print(len(offers))