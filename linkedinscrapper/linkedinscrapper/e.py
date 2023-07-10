import csv
from itertools import chain
post_list = []
try:
    with open("/home/vboxuser/programming/scrappy/linkedin/linkedinscrapper/data/postslinkscrapper/postslinkscrapper_2023-07-05T09-30-18.csv","r") as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)
        for row in csv_reader:
            post_list.append(row)
except FileNotFoundError:
            print("file not found")
except Exception as e:
            print(e)
lst = list(chain.from_iterable(post_list))
print(lst)