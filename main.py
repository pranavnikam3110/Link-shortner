import pyshorteners

link = input("enter the link : ")


shortner = pyshorteners.Shortener()


x = shortner.tinyurl.short(link)

print(x)