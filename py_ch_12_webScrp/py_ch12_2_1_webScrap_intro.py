
# Courses: colt_py_bootcamps    324,

# ---------------    web scrapping    ---------------

# ========    OBJECTIVES    ========
# Define what web scraping is and the issues (ethical) surrounding it
# Use the 'requests' and 'BeautifulSoup' modules to parse HTML 
# Explain some common problems with web scraping (technical problems) 
# Explore other tools that can interact with web pages (to sove technical problem)



# Introduction to Web Scraping
# Web scraping involves programmatically grabbing data from a web page
    # HTML mostly
    # API serving "json" or "xml"

# Three steps: 
    # DOWNLOAD: Get thousand of html page
    # EXTRACT:  data: parse the HTML and extract the data from it
    # PROFIT:   Send it to SERVER, use it to build app and other stuff.



# ========    why scarpe?    ========
# There's data on a site that you want to store or analyze 

# You can't get by other means (e.g. an API)
    # some website dont provide API we need to scrape it manually
    # You want to programmatically grab the data (instead of lots of manual copying/pasting)

# market analysis:
    # E.G. Analysis apartment rental price
        # chart the price over TIME
            # price Ups and Down over the specific time of the year
            # when its cheaper: Holidays or Summer etc

    # We can extarct the PRICE, Name, Apartment Size, Neighbourhood data fron the 'HTML tags'
        # Then we can analyze the data

    # For MACHINE LEARNING project we can store that data in CSV format




