
from subprocess import check_output

scriptname = "example.py"
outputfilename = "example1.json"
check_output("cd C:\\Users\\egosh\\PycharmProjects\\webscraper", shell=True).decode()
check_output("scrapy runspider {} -o {}".format(scriptname, outputfilename), shell=True).decode()