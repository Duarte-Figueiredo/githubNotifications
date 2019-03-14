from RssBuilder.RssItem import RssItem

from RssBuilder import RssBuilderObj

rss = RssBuilderObj.RssBuilder("example")
rss.add_item(RssItem("exampleItem"))
rss.add_item(RssItem("exampleItem2"))

print(rss.to_xml())
