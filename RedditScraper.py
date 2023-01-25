import json, datetime, os, csv
import requests
from tqdm import tqdm

cwd = os.getcwd()

file_name = "cheat1.csv"
file = open(cwd + f"/{file_name}","w")
file.close()

sub = "relationships"   
after = 1262296800      #unix time
before = 1388534400      
inc = 86400      
num = 500



def yield_request(sub, after, before, inc, num):
    while after <= before:
        try:
            r = requests.get(f'https://api.pushshift.io/reddit/search/submission/?subreddit={sub}&after={after}&before={after+inc}&size={num}')
            yield r.json()
            after += inc
        except json.decoder.JSONDecodeError:
            pass


def append_csv(request):
    i = 0 
    for data in request:
        for item in data["data"]:
            try:
                if item['selftext'] not in ["[removed]","[deleted]",""," "]:
                    if "cheat" in item['selftext']:
                        print(item['selftext'])
                        with open(file_name, "a", newline="", encoding="utf-8") as file:
                            csv_file = csv.writer(file)
                            if i == 0:
                                csv_file.writerow(["Title","Body","Score","Created","Author","PermaLink","Mature", "ID"])
                                i += 1
                            else:
                                csv_file.writerow((item['title'], item['selftext'], item['score'], datetime.datetime.fromtimestamp(item['created_utc']), item['author'] , item['permalink'], item['over_18'], item['id']))
            except Exception:
                pass
    
            
if __name__ == "__main__":
    append_csv(tqdm(yield_request(sub, after, before, inc, num)))
    print("Done")


