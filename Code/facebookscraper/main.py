import os
import subprocess

search_query = input("Enter search query: ")
print("Searching")

op_file = open("output.txt", "wt")
proc = subprocess.Popen('scrapy crawl facebook_searcher -a search_query="{}"'.format(search_query), stdout=op_file, stderr=op_file, shell=True)
proc.communicate()

result_filename = "search_result_{}.txt".format(search_query)
if os.path.isfile(result_filename):
    print("Scraping successful")
    with open(result_filename, "rt") as f:
        profiles = f.readlines()
    for i in range(len(profiles)):
        print("{}. {}".format(i+1, profiles[i].strip()))
    inp = int(input("Select profile to scrape: "))
    profile = profiles[inp-1]
    proc = subprocess.Popen('scrapy crawl facebook_scraper -a profile_id="{}"'.format(profile.strip()), stdout=op_file, stderr=op_file, shell=True)
    proc.communicate()
    profile_id = profile.strip().split("/")[-1].replace("?", ".")
    with open("info_{}.txt".format(profile_id)) as f:
        output = f.readlines()
    for op in output:
        print("\t{}".format(op), end="")

else:
    print("Scraping unsuccessful")
