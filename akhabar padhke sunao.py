import requests
import json

def ne(urll):
    if urll == "1g":
        spea("wrong input")

    else:
        news = requests.get(urll).text
        nwsapi = json.loads(news)
        # print(nwsapi["articles"])
        # print(news)
        # print(nwsapi)

        arts = nwsapi['articles']
        spea(f"Number of headlines are {len(arts)}.")
        spea("Lets start. Listen carefully...Today's news headlines are")

        for i, ar in enumerate(arts):
            spea(ar['title'])

            if ar['description'] != None:
                spea('its description is...')
                spea(ar['description'])

            if ar['url'] != None:
                spea("you read this on this url...")
                print(ar['url'])

            b = len(arts) - 1
            print(b)
            print(i)
            print(len(arts))
            # spea("its content is")
            # spea(i['content'])

            if i < b:
                spea("Lets moving to next news. Next news headline is...")

        spea("Thanks for listning...")

def spea(str):
    from win32com.client import Dispatch

    speak = Dispatch("SAPI.SpVoice")
    print(str)
    speak.Speak(str)

if __name__ == "__main__":
    spea("Hello sir")

    list1 = ["1 for India", "2 for Argentina", "3 for Greece", "4 for Netherlands", "5 for South Africa", "6 for Australia", "7 for Hong Kong", "8 for New Zeland", "9 for South Korea", "10 for Austria", "11 for Hungary", "12 for Nigeria", "13 for Sweden", "14 for Belgium", "15 for Norway", "16 for Switzerland", "17 for Brazil", "18 for Indonesia", "19 for Philippines", "20 for Taiwan", "21 for Bulgaria", "22 for Ireland", "23 for Poland", "24 for Thailand", "25 for Canada", "26 for Israel", "27 for Portugal", "28 for Turkey", "29 for china", "30 for Italy", "31 for Romania", "32 for UAE", "33 for Colombia", "34 for Japan", "35 for Russia", "36 for Ukraine", "37 for Cuba", "38 for Latvia", "39 for Saudi Arabia", "40 for United Kingdom", "41 for Czech Republic", "42 for Lithuania", "43 for Serbia", "44 for United States", "45 for Egypt", "46 for Malasiya", "47 for Singapore", "48 for Venuzuela", "49 for France", "50 for Mexico", "51 for Slovakia", "52 for Germany", "53 for Morooco", "54 for Slovenia"]
  
    spea("Please enter which country's you listen news")
    for it in list1:
        print(it)

    spea("enter here: ")
    f = int(input())

    country = ("in" if f is 1 else("ar" if f is 2 else("gr" if f is 3 else("nl" if f is 4 else("za" if f is 5 else("au" if f is 6 else("hk" if f is 7 else("nz" if f is 8 else("kr" if f is 9 else("at" if f is 10 else("hu" if f is 11 else("ng" if f is 12 else("se" if f is 13 else("be" if f is 14 else("no" if f is 15 else("ch" if f is 16 else("br" if f is 17 else("id" if f is 18 else("ph" if f is 19 else("tw" if f is 20 else("bg" if f is 21 else("ie" if f is 22 else("pl" if f is 23 else("th" if f is 24 else("ca" if f is 25 else("il" if f is 26 else("pt" if f is 27 else("tr" if f is 28 else("cn" if f is 29 else("it" if f is 30 else("ro" if f is 31 else("ae" if f is 32 else("co" if f is 33 else("jp" if f is 34 else("ru" if f is 35 else("ua" if f is 36 else("cu" if f is 37 else("lv" if f is 38 else("sa" if f is 39 else("gb" if f is 40 else("cz" if f is 41 else("lt" if f is 42 else("rs" if f is 43 else("us" if f is 44 else("eg" if f is 45 else("my" if f is 46 else("sg" if f is 47 else("ve" if f is 48 else("fr" if f is 49 else("mx" if f is 50 else("sk" if f is 51 else("de" if f is 52 else("ma" if f is 53 else("si" if f is 54 else("1k")))))))))))))))))))))))))))))))))))))))))))))))))))))))

    if country == "1k":
        spea("wrong input")

    else:
        spea("related to which field you listen news...")
        list = ["1 for related to all field", "2 for technology field", "3 for business field", "4 for entertainment", "5 for health", "6 for science field", "7 for sports field"]

        for i, item in enumerate(list):
            spea(item)

        spea("Please enter")
        t = int(input("enter here:\n"))

        Api_key = "3125cab4dce447b2bc7f611284b8cfcb"

        url1 = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={Api_key}"
        url3 = f"https://newsapi.org/v2/top-headlines?country={country}&category=business&apiKey={Api_key}"
        url4 = f"https://newsapi.org/v2/top-headlines?country={country}&category=entertainment&apiKey={Api_key}"
        url5 = f"https://newsapi.org/v2/top-headlines?country={country}&category=health&apiKey={Api_key}"
        url6 = f"https://newsapi.org/v2/top-headlines?country={country}&category=science&apiKey={Api_key}"
        url7 = f"https://newsapi.org/v2/top-headlines?country={country}&category=sports&apiKey={Api_key}"

        spea("you choose all field news." if t is 1 else("you choose technology news." if t is 2 else("you choose business news." if t is 3 else("you choose entertainment news." if t is 4 else("you choose health news." if t is 5 else("you choose science news." if t is 6 else("you choose sports news." if t is 7 else "wrong")))))))

        ne(url1 if t is 1 else(url2 if t is 2 else(url3 if t is 3 else(url4 if t is 4 else(url5 if t is 5 else(url6 if t is 6 else(url7 if t is 7 else "1g")))))))
