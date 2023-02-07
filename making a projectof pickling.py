import requests, pickle

url = "https://support.microsoft.com/en-us/office/create-and-print-notes-pages-324b234d-83b6-4db1-8bb6-9ee5c934a76f"

# def give(url1):
#     data = requests.get(url1)
#     a = data.text.split("\n")

#     b = (i.split(",") for i in a if len(i) != 0)

#     file = "my.txt"
#     fileo = open(file, "wb")
#     s = pickle.dump(a, fileo)
#     fileo.close()

# give(url)

filej = "my.txt"
fileob = open(filej, "rb")
sk = pickle.load(fileob)
fileob.close()
print(sk)
print(type(sk))