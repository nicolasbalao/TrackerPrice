import requests
import bs4
from bs4 import BeautifulSoup
import sys
import datetime


def Tracker(url):
    header = {
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"
    }
    page = requests.get(url, headers=header)
    soup = BeautifulSoup(page.content, 'html.parser')

    # title = soup.find(id="productTitle").get_text().strip()
    try:
        price = soup.find(id="priceblock_ourprice").get_text()
        print(price, 'price')
        if (len(price) >= 8):
            converted_price = float(price[0:3])
        else:
            converted_price = float(price[0:2])

        return (converted_price)

    except:
        price = "Plus en vente"
        return (price)


# liens config
ConfigAmazon = ["https://www.amazon.fr/AMD-Ryzen-5-3600/dp/B07STGGQ18/ref=sr_1_1?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=amd+ryzen+5+3600x&qid=1613491697&sr=8-1",
                "https://www.amazon.fr/Gigabyte-GV-N1030D5-2GL-Graphique-GeForce-Express/dp/B0719CR59P/ref=sr_1_1?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=Carte+graphique+Nvidia+Gigabyte+GeForce+GT+1030+Low+Profile+2G&qid=1613579459&sr=8-1",
                "https://www.amazon.fr/MSI-B450-Gaming-Prise-S-ATA/dp/B07V9L4RT6/ref=sr_1_1?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3ARWVEPJINCJF&dchild=1&keywords=msi+b450+gaming+plus+max&qid=1613494965&sprefix=msi+%2Caps%2C211&sr=8-1",
                "https://www.amazon.fr/Corsair-Vengeance-3200MHz-M%C3%A9moire-Performance/dp/B0143UM4TC/ref=sr_1_5?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=corsair+vengeance+3200&qid=1613495110&sr=8-5",
                "https://www.amazon.fr/Western-Digital-wds480g1g0-Serial-Drives/dp/B01M3POPK3/ref=sr_1_1?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=wd+480+go&qid=1613495186&sr=8-1",
                "https://www.amazon.fr/Seagate-St1000dmz10-Barracuda-Disque-Interne-Argent/dp/B07D99KFPK/ref=sr_1_2?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2O1LQFCEIPADV&dchild=1&keywords=seagate+barracuda+1to&qid=1613495249&sprefix=seagate%2Caps%2C213&sr=8-2",
                "https://www.amazon.fr/Cooler-Master-White-V2-450W-Alimentation/dp/B07VC52VBT/ref=sr_1_2?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=cooler+master+450&qid=1613495281&sr=8-2"]


# resultat

def result(list):
    mount_list_comparaison = []
    mount_list_float = []
    for components in list:
        mount_article = Tracker(components)
        print(mount_article)
        mount_list_float.append(mount_article)
        mount_list_comparaison.append(mount_article)

    for i in mount_list_float:
        if i == "Plus en vente":
            mount_list_float.remove(i)

    total_build = sum(mount_list_float)
    total_build_init = 682.0
    answer_comparaison = []

    title = ["CPU", "GPU", "MTB", "RAM", "SSD", "HDD", "ALIM"]
    price = [205.00, 112.70, 104.90, 93.49, 68.72, 46.99, 54.44]

    for a in range(0, 6):
        if mount_list_comparaison[a] == "Plus en vente":
            answer_comparaison.append(title[a] + ": " + "Plus en vente")
        elif mount_list_comparaison[a] <= price[a]:
            difference = round(price[a] - mount_list_comparaison[a], 3)
            answerComparaison = title[a] + ": " + str(difference)
            answer_comparaison.append(answerComparaison)

    answer_comparaison.append("Total diff: ", (total_build_init - total_build))

    return answer_comparaison


message = (result(ConfigAmazon))

for item in message:
    print(item)
