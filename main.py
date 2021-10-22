import requests

print("That program will not download a ready to use web, it will only download the html file without any addons")


ok = input("OK? [Y/N]")

if ok == "Y":
    print("ok")

    url = input("Enter a web to download source code")
    r = requests.get(url, allow_redirects=True)

    open("UrDownloadedWeb.html", "wb").write(r.content)

elif ok == "N":
    print("elo")
    exit()

else:
    print("Wrong Value")