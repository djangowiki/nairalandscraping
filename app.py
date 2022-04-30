from bs4 import BeautifulSoup
import requests

url = "https://www.nairaland.com"

req = requests.get(url)
html = """
<!DOCTYPE html>
<html>
<style>
table, th, td {
  border:1px solid black;
}
</style>
<body>

<h2>NairaLand Webscraping</h2>

<table style="width:100%">
  <tr>
    <th>Section</th>
    <th>Forum Name</th>
    <th>Forum Url</th>
  </tr>
  <tr>
    <td></td>
  </tr>
  <tr>
    <td></td>
  </tr>
</table>

</body>
</html>
"""

soup = BeautifulSoup(req.text, "lxml")
soup1 = BeautifulSoup(html, "lxml")

tds = soup.find_all("td", class_="l")
for td in tds:
    anchors = td.find_all("a")
    for anchor in anchors:
        link = anchor["href"]
        absolute_url = f"{url}{link}"
        forumName = anchor.b.string

        forum_td = soup1.new_tag("td")
        forum_td.string = forumName

        link_td = soup1.new_tag("td")
        link_a = soup1.new_tag("a", href=f"{absolute_url}")
        link_a.string = absolute_url
        link_td.append(link_a)

        section_td = soup1.new_tag("td")

        tr = soup1.new_tag("tr")

        tr.append(section_td)
        tr.append(forum_td)
        tr.append(link_td)

        soup1.table.append(tr)

with open("forums.html", "w") as html_file:
    html_file.write(soup1.prettify())
