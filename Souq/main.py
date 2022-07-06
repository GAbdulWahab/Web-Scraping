from bs4 import BeautifulSoup as bs
from urllib.request import urlopen

url="https://wuzzuf.net/search/jobs/?a=navbl%7Cspbl&q=data%20scientist"
client=urlopen(url)
html=client.read()

client.close()
soup=bs(html,"html.parser")

containers = soup.find_all("div", {"class": "css-1gatmva e1v1l3u10"})
bs.prettify(containers[0])




f=open("Wazzuf-data-scienctest.csv","w")
header="Job_title , Company_Name , Location ,Job_type , job_requirement"
f.write(header)
for container in containers:
    Jtitle = container.findAll("h2", {"class": "css-m604qf"})
    Job_title=Jtitle[0].text.strip()
    Cname = container.findAll("a", {"class": "css-17s97q8"})
    Company_Name = Cname[0].text.strip()
    location = container.findAll("span", {"class": "css-5wys0k"})
    Location_ = location[0].text.strip()
    Jtype = container.findAll("div", {"class": "css-1lh32fc"})
    Job_type = Jtype[0].text.strip()
    Jrequire = container.findAll("a", {"class": "css-o171kl"})
    job_requirement = Jrequire[0].text.strip()
    # print(Job_title, " ", Company_Name, " ", Location_, " ", Job_type)
    
    f.write(Job_title + " | " + Company_Name + " | " + Location_ + " | " + Job_type + " | "+job_requirement+"\n")
f.close()