# Project - Most Common Programming Languages


*Based on `PythonReview\EXERCISES\Exercise - How to Build A Web Crawler` AND <br> `PythonReview\EXERCISES\Execrise - Word Frequency Counter (Web Crawler Edition)`*


### Used BeautifulSoup library


## Objective: Crawling [Indeed.com](https://www.indeed.com) for most programming languages in software developer job descriptions in Dallas, TX
Starting URL: https://www.indeed.com/jobs?q=software%20developer&l=Dallas,%20TX&start=0  *(start=# goes up by increments of 10)*

*Note: Too many manual web scraping requests, especially requests sent one after another, may result in getting blocked by web server.*

Workarounds after getting blocked:
* clear cookies/cache on Indeed from web browser
* Command Prompt >> `ipconfig /release` >> ENTER `ipconfig /renew` >> ENTER (to get assigned a new IP address with DHCP)
* try to do it with a VPN and/or proxy
* make sure to include the below header info (see `get_job_posting_links` function)

__And with any of the above workarounds, make sure to NOT send too many requests or will get blocked again. Wait a few minutes before sending another request.__