import requests # one of the ways to connect to websites via Python
from bs4 import BeautifulSoup # allows you to go through page source and get data
import operator # will help with counting words



# set max pages to search through Indeed job pages
def get_job_posting_links(max_pages):
    page = 0  # increment by 10
    website_links = list()
    word_list = list()
    while page <= max_pages:
         

        url = "https://www.indeed.com/jobs?q=software%20developer&l=Dallas,%20TX&start="+str(page)
        
        # Avoid getting blocked in case multiple requests are sent
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0",
            'referer':'https://www.indeed.com/'
        }

        proxy = {'http': 'http://45.152.188.246:3128'}

        # GET request; stores page HTML source in variable
        source_code = requests.get(url, headers=header, proxies=proxy) 

        # gets the front end text of the HTMl source code; ignoring back end stuff; essentally parses through HTML source
        plain_text = source_code.text 

        # can sort through this variable
        soup = BeautifulSoup(plain_text) 

        
        # Searched through all of the job posting links & added them to website_links list ( inspect element for unique class/id names)
        for link in soup.findAll('a', {'class': 'jcs-JobTitle'}): # similar to CSS descendant selectors (a .jcs-JobTitle)
            job_href = "https://www.indeed.com" + link.get('href')
            website_links.append(job_href)
        

        
        

        # Execute below function for each link in website_links list
        for index in website_links:

            return_list = indiv_job_posting_info(index) # store urls of each job listing meant for function in below cell
            
            for index2 in return_list:
                word_list.append(index2)

        # Increment pages by 10
        page += 10


        word_list_cleaned = clean_up_list(word_list)
        wordfrequency(word_list_cleaned)


def indiv_job_posting_info(job_url):
        
        word_list_temp = list()

        # GET request; stores page HTML source in variable
        source_code = requests.get(job_url) 

        # gets the front end text of the HTMl source code; ignoring back end stuff; essentally parses through HTML source
        plain_text = source_code.text 

        # can sort through this variable
        soup = BeautifulSoup(plain_text)
        
        # find the job description
        jobdesc = soup.find('div', {'id': 'jobDescriptionText'})
        
        # remove all the HTML tags from the job description & split job description by each word; stored in a list
        job_desc_list = jobdesc.get_text().lower().split() # all lowercase
                
        
        return job_desc_list
        
    

# removed extra unnecessary symbols
def clean_up_list(word_ls):
    clean_word_list = []

    for word in word_ls:
        symbols_to_remove = '".&:,\'()$1234567890'

        for index in range(0, len(symbols_to_remove)):
            word = word.replace(symbols_to_remove[index], "")

        if len(word) > 0:
            clean_word_list.append(word)   

    return clean_word_list


### Create a list filled with [100 most common programming languages](https://medium.com/web-development-zone/a-complete-list-of-computer-programming-languages-1d8bc5a891f), convert to all lowercase, and use it to match the keys of the dictionary

languages = list()

source_code = requests.get('https://medium.com/web-development-zone/a-complete-list-of-computer-programming-languages-1d8bc5a891f') 

# gets the front end text of the HTMl source code; ignoring back end stuff; essentally parses through HTML source
plain_text = source_code.text 

# can sort through this variable
soup = BeautifulSoup(plain_text)

# find & store all lowercase progamming languages in a list to copy/paste
for language in soup.findAll('h2'):
    languages.append(language.get_text().lower())

print(languages)

#########


def wordfrequency(word_ls):
    counts = dict()
    counts_lang = dict()
    languages = ['apl', 'autoit', 'basic', 'eiffel', 'forth', 'frink', 'game maker language', 'ici', 'j', 'lisp', 'lua', 'm', 'pascal', 'pcastl', 'perl', 'postscript', 'python', 'rexx', 'ruby', 's-lang', 'spin', 'charity', 'clean', 'curry', 'erlang', 'f#', 'haskell', 'joy', 'kite', 'ml', 'nemerle', 'opal', 'ops5', 'q', 'ada', 'algol', 'c', 'c++', 'c#', 'cleo', 'cobol', 'cobra', 'd', 'dasl', 'dibol', 'fortran', 'java', 'jovial', 'objective-c', 'small', 'smalltalk', 'turing', 'visual basic', 'visual foxpro', 'xl', 'bliss', 'chuck', 'clist', 'hypertalk', 'modula-2', 'oberon', 'component pascal', 'matlab', 'occam', 'pl/c', 'pl/i', 'rapira', 'rpg', 'applescript', 'awk', 'beanshell', 'coldfusion', 'f-script', 'jass', 'maya embedded language', 'mondrian', 'php', 'revolution', 'tcl', 'vbscript', 'windows powershell', 'curl', 'sgml', 'html', 'xml', 'xhtml', 'alf', 'fril', 'janus', 'leda', 'oz', 'poplog', 'prolog', 'roop', 'abcl', 'afnix', 'cilk', 'concurrent pascal', 'e', 'joule', 'limbo', 'pict', 'salsa', 'sr', 'agora', 'beta', 'cecil', 'lava', 'lisaac', 'moo', 'moto', 'object-z', 'obliq', 'oxygene', 'pliant', 'prograph', 'rebol', 'scala', 'self', 'slate', 'xotcl', 'io']


    for word in word_ls:
        counts[word] = counts.get(word, 0) + 1

    for index in languages:
        if index in counts:
            counts_lang.update({index: counts[index]})


    # SORTING DICTIONARY (using operator module)
    for key, val in sorted(counts_lang.items(), key=operator.itemgetter(1), reverse=True): # 0 for key, 1 for value
        print(key, "---", val)



#################################################################


### Most common programming languages on page 1 of Indeed:

get_job_posting_links(0)



