import pyrebase
from os import path, makedirs
import matplotlib.pyplot as plt
from pandas import read_csv
from numpy import nan
from calendar import month_name
from urllib.parse import unquote

config = {
  "apiKey": "AIzaSyA7Uuc0D5NsOEjxuTS1UYcQ45CT1MKapP4",
  "authDomain": "osint-iph.firebaseapp.com",
  "databaseURL": "https://osint-iph.firebaseio.com",
  "storageBucket": "osint-iph.appspot.com",
  'serviceAccount': {
        # Your "Service account ID," which looks like an email address.
        'client_email': "firebase-adminsdk-nvc4o@osint-iph.iam.gserviceaccount.com", 
        # The part of your Firebase database URL before `firebaseio.com`. 
        # e.g. `fiery-flames-1234`
        'client_id': "116893492045810462544",
        # The key itself, a long string with newlines, starting with 
        # `-----BEGIN PRIVATE KEY-----\n`
        'private_key': "-----BEGIN PRIVATE KEY-----\nMIIEugIBADANBgkqhkiG9w0BAQEFAASCBKQwggSgAgEAAoIBAQDViQMIdisqR3oA\nt8sC6MG7szjOXhwySpOifHcBt69vnI6HCRZrAlWqp340j47UtxvmOWOoc8j7cwzr\nQgOJLay20S4zzm4kAx7tfEKwp4/V2bNwGGp7gniVO0Rji/XnytCIwk0lmmTZ/FwE\nRskN5IQry8YJsCepJ/H9CawWkeIXCEFPzNGH1q9R0vtQcPYUkA/SVHuyKgyVpSJq\nNgMZJPTIsniYE5k4/lWuKMXMtiYgSX1iwqIXH7BRQv4q8dT+hqQ7JgeuiAGN/Uob\nPX8b2pbdpLhfsW5pwqd22jz0Doe0TbaAgHSsWwWQ4QwCm/1eIt6JbcGOeCcx0jys\n6JiYNZ4RAgMBAAECgf9B8OLwq8Yacvgrzs7wlwyR+GL2AjZdilTUH7f1wZjrl3tP\nqcXe8HYSLt/1Be5AUEt397LAmXKh+vOez0Py7hmvBbD3wGQmZXr8241K48kjpHph\nhu/M3v2Wpja/aod3cI28WH0lEV33D3da9yutgisVzQJMwrW1lTzBvJ52IOwUTKC6\nFF3VMV5Gu2dYYvDy6xhxadNs3r+sP/3hjYl42ZC16DWVM4WBtaJlXe3M3Hz+7ZEV\n1evxX1kKJlY01TOC30z8D3P1lifkUIB9Xc2YbBipat1yuaOxZaBEE4C/Efw791LK\njzeJIfAcsnPmeK96d4xu3ih521N9F6QXLS52cr8CgYEA8Vj+XkzCU0coqeFKtM0t\n4KbAFO84UUC7Agh6qhKf0Ijy6RBQZODtEB/0TpMW8WQvuDYx7lajuK6AyLCKK2Ju\nl34D3idG+lifYSD7ATCyRHZnNNgjgeVzNc/HCiUR+ivERVFnSYJsk8PoYPPqmDH+\nJeoTWmWzIcjwCaRR/lgDwwcCgYEA4n/CdDv3dsRb1n2uaZH1MzeaugnpEp/wEezU\nzJ8VTUAymOr/flRw4eiC7iN0LL39rtLALHar9ZTqAfPUQzYIG5gp65QUODYuwpKz\n9gle7kkm8HIIsWobUaRw9McDidlKSjYiUSzB6hUI1EylEGvf6VbxlbhIc0piaMWJ\nTvYD2CcCgYAIhYXlunwaCKcs6GGE5MG77udVVeT9KXXw6m+6VZIDAPLiu8q65R45\ntYcgxxzGRS1SKce1jKWXPcIaU/Fs+rrA6pgkXeqpqDtoaIu0TQ3eUPfv67nFOl7J\nBZ8XgpuR4724XNlyxQIkbYRk9/fOi+VXXV51kKW0ia3ACWdDvcPUPQKBgH6nYG4s\nxjFElfI371qbQpi0RDI5rno6szziyQ/u+TNsbZ6y8dGLmF/K68QMUT9fskabFNkI\nNxopfj0/Qnee9COyD+bqs+/G5Jjq/fTbwpjOkRatPY0vvz0FDiDiVGk192POJ5xq\nwbiKsJg+j6LCH8BUXN0S4niNpL/fjet4iCfLAoGANioOf1kzuWR/2gu9WJhPtGOq\nexwuezE8q1lLip71n7JgKmlrPElCeoCiAjDPwmG7DgBIXOVB3s+e6mC9dFvqeVm9\nzRkdj0NcOm8E0IiRFysmaiXDeCZSodThOhd5OM/QXGdVz8ZHGZVpzThsJ4YEqtgj\n6QyZrezPSO3TfKxDr9s=\n-----END PRIVATE KEY-----\n".replace('\\n', '\n'),
        # Your service account "key ID." Mine is 40 alphanumeric characters.
        'private_key_id': "f4e683b7b451d6eb0c06e75bae7fc3fa3cfed49c",
        'type': 'service_account'
    }
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

random_str = (input("Enter the random string: "))

OUTDIR = ("DOWNLOADED_FILES/"+str(random_str)).replace("\\", ".").replace(":", "")
makedirs(OUTDIR, exist_ok=True) 

storage.child("data/"+random_str+"/output.txt").download(path.join(OUTDIR, "output.txt"))
# storage.child("data/"+random_str+"/Graphs.pdf").download(path.join(OUTDIR, "Graphs.pdf"))
# storage.child("data/"+random_str+"/url_frequency.csv").download(path.join(OUTDIR, "url_frequency.csv"))
# storage.child("data/"+random_str+"/url_visittime.csv").download(path.join(OUTDIR, "url_visittime.csv"))

storage.child("data/"+random_str+"/url_frequency.csv").download(path.join(OUTDIR, "url_frequency.csv"))
storage.child("data/"+random_str+"/url_visittime.csv").download(path.join(OUTDIR, "url_visittime.csv"))
storage.child("data/"+random_str+"/Copied_History").download(path.join(OUTDIR, "Copied_History"))
storage.child("data/"+random_str+"/category_percentage.csv").download(path.join(OUTDIR, "category_percentage.csv"))




file = path.join(OUTDIR, "url_visittime.csv")
dataset = read_csv(file)
dataset_copy = dataset.copy()
dataset["visit_time"] = dataset["visit_time"].apply(lambda x: str(x[11:13]))
dataset = dataset.sort_values(ascending=False, by="visit_time")
times_frequency = dataset.groupby("visit_time").size()
times_only = list(times_frequency.keys())
frequency_of_times = list(times_frequency.values)

dataset["url"] = dataset["url"].str.split("/").str[2]    #split url by / and get only the website name
dataset["url"] = dataset["url"].str.replace("www.","")
dataset["url"].replace('', nan, inplace=True)
dataset.dropna(subset=["url"], inplace=True)
url_frequency = dataset.groupby("url").size() #Number of times each website is visited
url_frequency = url_frequency.sort_values(ascending=False)
# url_frequency.to_csv(path.join(OUTDIR, "url_frequency.csv"))
# url_frequency = read_csv(path.join(OUTDIR, "url_frequency.csv"))
url_frequency = url_frequency[url_frequency > 10]

urls = (list(url_frequency.keys()))
frequency = (list(url_frequency.values))

def time_24hours_to_12hours(time_24):
    time_12 = ""
    time_24 = int(time_24)
    if 0 < time_24 < 12:
        time_12 = str(time_24) + " AM"
    elif time_24 == 0:
        time_12 = "12 AM"
    elif time_24 == 12:
        time_12 = "12 PM"
    elif 12 < time_24 < 24:
        time_12 = str(time_24 - 12) + " PM"
    return time_12
times_only_12hours = list(map(time_24hours_to_12hours, times_only))

dataset_copy["visit_time"] = dataset_copy["visit_time"].apply(lambda x: str(x[:7])) #To get only year and month in date
groupedby_months = dataset_copy.groupby("visit_time").size()
month_years = list(groupedby_months.keys())
number_of_sites_visited_in_months = list(groupedby_months.values)


fig = plt.figure(figsize=(16,9))
gs = fig.add_gridspec(ncols = 3, nrows = 2)
pie_ax = fig.add_subplot(gs[0,0])
bar3_ax = fig.add_subplot(gs[1,0])
bar1_ax = fig.add_subplot(gs[0,1:3])
bar2_ax = fig.add_subplot(gs[1,1:3])

pie_ax.axis("equal")
pie_ax.pie(frequency, labels=urls[:15]+["" for x in range(0,len(urls)-15)], labeldistance=1, rotatelabels=True)

x_ticks = range(len(urls))
bar1_ax.bar(x_ticks, frequency)
bar1_ax.set_xlabel("Website url")
plt.sca(bar1_ax)
plt.xticks(x_ticks, [], rotation="vertical", fontsize=5)
rects = bar1_ax.patches
for rect, label in zip(rects, urls):
    bar1_ax.text(rect.get_x() + rect.get_width() / 2, 5, label,
            ha='center', va='bottom', fontsize=5, rotation="vertical")

bar2_ax.bar(times_only, frequency_of_times)
plt.sca(bar2_ax)
plt.xticks(times_only, [], rotation="vertical")
rects = bar2_ax.patches
for rect, label in zip(rects, times_only_12hours):
    height = rect.get_height()
    bar2_ax.text(rect.get_x() + rect.get_width() / 2, height - 0.2, label,
            ha='center', va='bottom', fontsize="small")
bar2_ax.set_xlabel("Time")

x_ticks = range(len(groupedby_months))
bar3_ax.bar(x_ticks, number_of_sites_visited_in_months)
bar3_ax.set_xlabel("Month and Year")
plt.sca(bar3_ax)
plt.xticks(x_ticks, [], rotation="vertical")
rects = bar3_ax.patches
months = [month_name[int(x[5:])] + " " + x[:4] for x in month_years]
for rect, label in zip(rects, months):
    height = rect.get_height()
    bar3_ax.text(rect.get_x() + rect.get_width() / 2, height/2 - height/6, label,
            ha='center', va='bottom', fontsize="small", rotation="vertical")


plt.tight_layout()
plt.savefig(path.join(OUTDIR, "Graphs.pdf"), format="pdf")

# print("Time to plot:", round(time()-start, 2), "s")

# if show_graphs: plt.show()
plt.close()

f = open(path.join(OUTDIR, "searches.txt"), "wt")
s = set()
for row in dataset_copy["url"]:
  if "www.google.co" in row and "search" in row:
    try:
      s.add(unquote(row.split("q=")[1].split("&")[0].replace("+", " ")))
    except:
      pass
s = [i+"\n" for i in s]
f.writelines(s)
f.close()