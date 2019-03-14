from RssBuilder.Utils import simple_xml_object


class RssItem:

    def __init__(self, title, description="", link=""):
        self.__title = title
        self.__description = description
        self.__link = link

    def get_title(self):
        return self.__title

    def get_description(self):
        return self.__description

    def get_link(self):
        return self.__link

    def get_title_xml(self):
        return simple_xml_object("title", self.__title)

    def get_description_xml(self):
        return simple_xml_object("description", self.__description)

    def get_link_xml(self):
        return simple_xml_object("link", self.__link)

    def to_xml(self):
        return simple_xml_object("item",
                                 self.get_title_xml() +
                                 self.get_description_xml() +
                                 self.get_link_xml())
