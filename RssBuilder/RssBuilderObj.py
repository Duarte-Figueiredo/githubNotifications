from RssBuilder.Utils import simple_xml_object
from RssBuilder.RssItem import RssItem


class RssBuilder(RssItem):

    def __init__(self, title, description="", link=""):
        super().__init__(title, description, link)
        self.__item_list = []

    def add_item(self, item):
        self.__item_list.append(item)

    def to_xml(self):
        item_list_xml = ""

        for item in self.__item_list:
            item_list_xml += item.to_xml()

        return simple_xml_object("channel",
                                 self.get_title_xml() +
                                 self.get_description_xml() +
                                 self.get_link_xml() +
                                 item_list_xml)
