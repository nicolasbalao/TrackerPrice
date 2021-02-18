import requests
import bs4
from bs4 import BeautifulSoup
import sys
import datetime


def Tracker(url, title, price):
    header = {
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"
    }
    page = requests.get(url, headers=header)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id=title).get_text().strip()
    try:
        price = soup.find(id=price).get_text()

        if (len(price) >= 8):
            converted_price = float(price[0:3])
        else:
            converted_price = float(price[0:2])

        String_answer = title + " : " + price
        print(converted_price)
        return (title, converted_price, String_answer)

    except:
        price = "Plus en vente"
        String_answer = title + " : " + price
        return (title, price, String_answer)


def resultat(list, Name, idTitle, idPrice):
    list_title = []
    mount_list = []
    details_config_price = []
    mount_comparaison = []
    # titre et prix de tous les articles
    for components in list:
        title_article, mount_article, answer = Tracker(
            components, idTitle, idPrice)
        list_title.append(title_article)
        mount_list.append(mount_article)
        details_config_price.append(answer)
        mount_comparaison.append(mount_article)

    def Comparaison(list):
        title = ["CPU", "GPU", "MTB", "RAM", "SSD", "HDD", "ALIM"]
        price = [205.00, 112.70, 104.90, 93.49, 68.72, 46.99, 54.44]
        answer_comparaison = []
        print("Comparaison")
        print("")
        for i in range(0, 6):
            if list[i] == "Plus en vente":
                answer_comparaison.append(title[i] + ": " + "Plus en vente")
            elif list[i] <= price[i]:
                difference = round(price[i] - list[i], 3)
                answerComparaison = title[i] + ": " + str(difference)
                answer_comparaison.append(answerComparaison)
        return answer_comparaison

    manque_article = 0
    for price in mount_list:
        if price == "Plus en vente":
            mount_list.remove(price)
            manque_article += 1

    price_config = sum(mount_list)

    # prix de base
    prix_de_base = [" ",
                    "AMD Ryzen 5 3600 : 205,00 €",
                    "Gigabyte GeForce GT 1030 OC 2G : 112,70 €",
                    "MSI B450 Gaming Plus Max (Prise AM4/B450/DDR4/S-ATA 600/ATX) : 104,90 €",
                    "Corsair Vengeance LPX 16Go (2x8Go) DDR4 3200MHz C16 XMP 2.0 Kit de Mémoire Haute Performance - Noir : 93,49 €",
                    "WD Green 480Go Internal SSD 2.5 SATA : 68,72 €",
                    "Seagate BarraCuda, 1 To, Disque dur interne HDD – 3,5 SATA 6 Gbit/s 7 200 tr/min, 64 Mo de mémoire cache, pour PC de bureau, Ouverture facile (ST1000DMZ10) : 46,99 €",
                    "Cooler Master MWE 450 White 230V - Alimentation V2 - 80 PLUS 230V Certifié EU, ventilateur 120 HDB silencieux, circuit CC-CC + LLC avec rail simple +12V - Garantie 3 ans : 54,44 €",
                    " ",
                    "Cout total : 682.0 €",
                    " "]

    total_cost_init = 682.0

    # print result
    print(datetime.datetime.now())
    print(Name)
    print(" ")

    for item in details_config_price:
        print(item)
    print(" ")

    print("Cout total: ")
    print("default price: ", total_cost_init)
    print(price_config, "€", " Sans boitier. ",
          "Article plus en vente: ", manque_article)
    print(" ")
    # si c'est moins chere
    if (price_config < total_cost_init):
        print("DEFAULT PRICE COMPARAISON")
        print("")
        yes_no = input("see default Comparaison (yes or no): ")
        if yes_no == "yes":
            for a in Comparaison(mount_comparaison):
                print(a)
            print("Total cost: " + str(total_cost_init - price_config))
        if input("see more details (yes or no)") == "yes":
            for item2 in prix_de_base:
                print(item2)

    elif (price_config <= 500):
        print("Alerte")
    else:
        print("last price", total_cost_init)
        print("meme prix")

    if input("Sources? (yes or no)") == "yes":
        for lien in ConfigAmazon():
            print(lien)


def ConfigAmazon():
    # liste des articles
    Config_pc_amazon = ["https://www.amazon.fr/AMD-Ryzen-5-3600/dp/B07STGGQ18/ref=sr_1_1?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=amd+ryzen+5+3600x&qid=1613491697&sr=8-1",
                        "https://www.amazon.fr/Gigabyte-GV-N1030D5-2GL-Graphique-GeForce-Express/dp/B0719CR59P/ref=sr_1_1?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=Carte+graphique+Nvidia+Gigabyte+GeForce+GT+1030+Low+Profile+2G&qid=1613579459&sr=8-1",
                        "https://www.amazon.fr/MSI-B450-Gaming-Prise-S-ATA/dp/B07V9L4RT6/ref=sr_1_1?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3ARWVEPJINCJF&dchild=1&keywords=msi+b450+gaming+plus+max&qid=1613494965&sprefix=msi+%2Caps%2C211&sr=8-1",
                        "https://www.amazon.fr/Corsair-Vengeance-3200MHz-M%C3%A9moire-Performance/dp/B0143UM4TC/ref=sr_1_5?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=corsair+vengeance+3200&qid=1613495110&sr=8-5",
                        "https://www.amazon.fr/Western-Digital-wds480g1g0-Serial-Drives/dp/B01M3POPK3/ref=sr_1_1?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=wd+480+go&qid=1613495186&sr=8-1",
                        "https://www.amazon.fr/Seagate-St1000dmz10-Barracuda-Disque-Interne-Argent/dp/B07D99KFPK/ref=sr_1_2?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2O1LQFCEIPADV&dchild=1&keywords=seagate+barracuda+1to&qid=1613495249&sprefix=seagate%2Caps%2C213&sr=8-2",
                        "https://www.amazon.fr/Cooler-Master-White-V2-450W-Alimentation/dp/B07VC52VBT/ref=sr_1_2?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=cooler+master+450&qid=1613495281&sr=8-2"]

    return Config_pc_amazon


# def ComparaisonResultOnli(list, Name, idTitle, idPrice):
#     mount_comparaison = []
#     for components in list:
#         title_article, mount_article, answer = Tracker(
#             components, idTitle, idPrice)
#         mount_comparaison.append(mount_article)

#     title = ["CPU", "GPU", "MTB", "RAM", "SSD", "HDD", "ALIM"]
#     price = [205.00, 112.70, 104.90, 93.49, 68.72, 46.99, 54.44]
#     answer_comparaison = []
#     print("Comparaison")
#     print("")
#     for i in range(0, 6):
#         if mount_comparaison[i] == "Plus en vente":
#             answer_comparaison.append(title[i] + ": " + "Plus en vente")
#         elif mount_comparaison[i] <= price[i]:
#             difference = round(price[i] - mount_comparaison[i], 3)
#             answerComparaison = title[i] + ": " + str(difference)
#             answer_comparaison.append(answerComparaison)
#     for a in answer_comparaison:
#         print(a)


# ComparaisonResultOnli(ConfigAmazon(), "Config Amazon: ",
#                       "productTitle", "priceblock_ourprice")

resultat(ConfigAmazon(), "Conf Amazon: ",
         "productTitle", "priceblock_ourprice")


################################## Faire une variante qui peut juste envoyer la comparaison list ##########
