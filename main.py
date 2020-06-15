import bs4
import requests
import bs4
import requests


product_class="._1UoZlX"
price_class="._2o7WAb"
dicount_class=".VGWI6T"
flipcart_assured_class="._3n6o0t"
price_class="._1vC4OE._2rQ-NK"
product_name="._3wU53n"
rating_class=".hGSR34"
product_link="a"

flipkart_url="https://www.flipkart.com/search?q={}&page={}"


search_item=["tv","laptop","mobile","ac","fridge"];
data={}

for item in search_item:
    data[item]=[]
for item in search_item:
    for page in range(1,2):
        result=requests.get(flipkart_url.format(item,page))
        soup=bs4.BeautifulSoup(result.text,"lxml")
        if len(soup.select(product_class))>0 :
            for product in soup.select(product_class):
                #to determine if discount is greater than 30%
                    if len(product.select(dicount_class))>0:
                        disc_str=product.select(dicount_class)[0].text.split()[0]
                        #print(disc_str)
                        discount = [int(i) for i in list(disc_str) if i.isdigit()]
                        print(discount[0]," type ",type(discount[0]),discount[0]>=3)
                        flag=0
                        if (len(discount)>1 and discount[0]>=3):
                            flag=1
                        #----------------------------------

                        # flicart assured and discount graeter than 30% we push it in our data 
                        if len(product.select(flipcart_assured_class))>0 and flag==1:
                                info={
                                    "link": product.select(product_link)[0]["href"],
                                    "name":product.select(product_name)[0].text,
                                    "price":product.select(price_class)[0].text,
                                    "discount":product.select(dicount_class)[0].text

                                }
                                if(len(product.select(rating_class))>0):
                                    info["rating"]=product.select(rating_class)[0].text

                                data[item].append(info)
                
                    
                    
                    
                    

 
