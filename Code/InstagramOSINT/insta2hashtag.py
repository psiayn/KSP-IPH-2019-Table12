import re
import json
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='cpt2#')
    parser.add_argument('--username',help='profile username',required=True,nargs=1)
    return parser.parse_args()

args = parse_args()
username = args.username[0].strip()
print(username)

with open (username+'/posts.json') as f:
    data = json.load(f)

#print(data)

captions = list()

for i in data.values():
     captions.append(i['Caption'])

cpt = captions

hashtags = list()

mentions = list()

for i in captions:
    hashtags.extend(re.findall(r"#(\w+)", i))

for j in captions:
    mentions.extend(re.findall(r"@(\w+)", j))

#hashtags = set(hashtags)

#print(hashtags,mentions,sep="\n")

dump = {}
dump['hashtags'] = hashtags
dump['mentions'] = mentions

with open('dump.json' , 'w') as d:
    json.dump(dump,d)
