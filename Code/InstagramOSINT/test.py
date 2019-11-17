from InstagramOSINT import *
username = input("Enter username")
instagram = InstagramOSINT(username=username)
print(instagram.profile_data)
print(instagram['Username'])
instagram.print_profile_data()
instagram.save_data()
instagram.scrape_posts()
