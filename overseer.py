
from subprocess import check_output

scriptname = "PlayGround.py"
outputfilename = "example1.json"
directory = "egosh\\PycharmProjects\\webscraper"
directory2 = "shvedov_es\\PycharmProjects\\webspider"
check_output("cd C:\\Users\\{}".format(directory2), shell=True).decode()
check_output("scrapy runspider {} -o {}".format(scriptname, outputfilename), shell=True).decode()