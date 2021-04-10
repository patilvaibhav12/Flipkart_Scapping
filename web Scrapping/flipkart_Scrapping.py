from bs4 import BeautifulSoup as Soup
from urllib.request import urlopen as uReq

my_url = "https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = Soup(page_html, 'html.parser')

containers = page_soup.findAll("div", {'class':'_4ddWXP'})
#print(len(containers))

#print(Soup.prettify(containers[0]))

container = containers[4]
#print(container.div.img["alt"])

price = container.findAll("div",{"class":"_25b18c"})
#print(price[0].text)

rating = container.findAll("div",{"class":"_2D5lwg"})
#print(rating[0].text)

filename = "products.csv"
f = open(filename, "w")

headers = "Product_name,Pricing,Ratings\n"
f.write(headers)



for container in containers:
    check = container.findAll("div",{"class":"_4HTuuX"})
    if len(check) != 0:
        continue
    product_name = container.div.img["alt"]

    price_container = container.findAll("div",{"class":"_30jeq3"})
    price = price_container[0].text.strip()

    rating_container = container.findAll("div",{"class":"_2D5lwg"})
    rating = rating_container[0].text

    #print("Product Name :" + product_name)
    #print("Price :" + price)
    #print("Ratings :" + rating + "Reviews")

    trim_price = ''.join(price.split(","))
    rm_rupee = trim_price.split("₹")
    final_price = "Rs." + rm_rupee[1]

    print(product_name.replace(",","|") + "," + final_price + "," + rating + "\n")
    f.write(product_name.replace(",","|") + "," + final_price + "," + rating + "\n")
    check.clear()

f.close()