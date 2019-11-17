import re
import json
import argparse
data = list()

# def parse_args():
#     parser = argparse.ArgumentParser(description='cpt2#')
#     parser.add_argument('--username',help='profile username',required=True,nargs=1)
#     return parser.parse_args()
#
# args = parse_args()
# username = args.username[0].strip()
#print(username)

f = open('dump.txt','r')

data = f.read()

tags = data

hashtags = [tag.strip("#") for tag in tags.split() if tag.startswith("#")]

mentions = [tag.strip("@") for tag in tags.split() if tag.startswith("@")]

#print(hashtags,captions,sep='\n')

dump = {}
dump['hashtags'] = hashtags
dump['mentions'] = mentions

with open('dump.json' , 'w') as d:
    json.dump(dump,d)
