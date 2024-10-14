# Job Scraper

    #### Video Demo:  <URL HERE>
    #### Description: My project is scrapping current job offers as junior Python developer from the website [JustJoinIt](https://justjoin.it/).
    I wanted to learn more about web scraping, because it is a good tool for automating some tasks.
    I tried to make my project simple, so I didn't use OOP or complex libraries.

    ## How it works?
    For now I have predifined links to the website, which I'm scrapping using requests module.
    HTML response is then passed to the BeautifulSoup module, because it's easier to work with.

    First request I send, recieves all current job postings, according to my filter which is specified in the url.
    From the response I'm getting job title and url to the offer.

    When I have those informations stored into dictionary, I send requests for each job offer.
    Then I collect skills required for the position and the level of proficiency with that skill/library.
    This data is then added to the dictionary.

    Finally I save those dictionaries in a json file.

    ## Future improvments
    I want to develop my project further as I learn new things.
    I want to scrap more websites, there are 3 main sites for IT roles in my country.
    I will nest things using OOP making the code cleaner and easier to scale.
    I would like to present data on my personal website and create some charts with statistics. So I would be able to track current trends in a job market and potentially develop my skills according to demand.
