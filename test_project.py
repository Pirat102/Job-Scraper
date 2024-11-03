from project import *

    
def test_get_each_job_title_link():
    with open("test_offers.html", "r", encoding="UTF8") as f:
        html = f.read()
    
    results = get_each_job_title_link(html)
    
    assert len(results) == 10
    assert "Junior Python Developer" in results
    assert "Software Developer" in results
    assert "Junior Python Engineer" in results

    

def test_get_job_requirements():        
    offer = {
        "Junior Python Developer": "https://justjoin.it/job-offer/link-group-junior-python-developer-71df6ad3-e914-4c9f-9ee6-d5f89de9feb8"}
                  
    results = get_job_requirements(offer)
    
    assert "Junior Python Developer" in results
    assert "skills" in results["Junior Python Developer"]
    assert results["Junior Python Developer"]["skills"]["Python"] == "junior"
    
def test_save_jobs_to_file():
    job = {"Junior Python Developer": {
        "skills": {
            "English": "advanced",
            "Linux": "junior",
            "Python": "junior"
        },
        "link": "https://justjoin.it/job-offer/link-group-junior-python-developer-71df6ad3-e914-4c9f-9ee6-d5f89de9feb8"}
    }
    
    save_jobs_to_file(job)
    
    with open("Python_jobs.json", "r", encoding="UTF8") as file:
        saved_jobs = json.load(file)
        assert saved_jobs == job