import xml.etree.ElementTree as ElementTree

from bs4 import BeautifulSoup


def get_str(tag):
    return 'N/A' if tag is None else tag.string


def get_href(tag):
    return 'N/A' if tag is None else tag.get("href")


class Element(object):
    def __init__(self, element=None):
        super().__init__()
        self.__tag = None
        self.__attr = None
        self.__classes = None
        self.__element = BeautifulSoup(str(element), "lxml")
        self.__text = None
        self.__href = None

    @property
    def tag(self):
        """
        Get the tag name of the root element
        :return: string
        """
        bse = list(self.__element.find("body").children)
        if len(bse) > 1:
            self.__tag = self.__element.find("body").name
        elif len(bse) == 1:
            self.__tag = bse[0].name
        return self.__tag

    @tag.setter
    def tag(self, value):
        """
        Set
        :param value: string
        :return:
        """
        self.__tag = value

    @property
    def parent(self):
        """
        Get the name of the parent for the current element
        :return: string
        """
        parent = self.element.find(self.tag).parent.name
        if parent == "body":
            return None
        else:
            return parent

    @property
    def children(self):
        """
        Get children for the root element
        :return: list
        """
        return list(self.element.find(self.tag).children)

    @property
    def classes(self):
        """
        Get classes for target element
        :return: list
        """
        self.__classes = self.__element.find(self.tag)['class']
        return self.__classes

    @classes.setter
    def classes(self, value):
        """
        Set the classes target for the element
        :param value:
        :return:
        """
        self.__classes = value

    @property
    def text(self):
        """
        Get text component for the element
        :return: string
        """
        if self.__element is not None:
            if self.tag is not None and self.__text is None:
                if self.__attr is not None:
                    self.__text = get_str(self.__element.find(self.tag, attrs=self.attributes))
                elif self.classes is not None:
                    self.__text = get_str(self.__element.find(self.tag, self.classes))
                return self.__text
            else:
                self.__text = self.__element.text
                return self.__text

    @property
    def element(self):
        """
        Get the raw element string
        :return: string
        """
        return self.__element

    @property
    def attributes(self):
        """
        Get tag attributes for the target tag attrs={"key": "Value"}
        :return: string
        """
        self.__attr = self.element.find(self.tag).attrs
        return self.__attr

    @attributes.setter
    def attributes(self, value):
        """
        Set attributes for target tag key:value
        :param value: string
        :return:
        """
        key, val = str(value).split(":")
        self.__attr = {key: val}

    @property
    def href(self):
        """
        Get href attribute from tag type a
        :return: string
        """
        if self.tag == "a":
            self.__href = get_href(self.__element.find("a", self.classes))
            return self.__href
        else:
            return self.__href

    def find_children(self, target_tag, target_class=None):
        """
        Get target child elements
        :param target_tag: string
        :param target_class: string
        :return: list
        """
        if self.element is not None:
            if target_class is not None:
                return [Element(child) for child in self.element.find_all(target_tag, target_class)]
            else:
                return [Element(child) for child in self.element.find_all(target_tag)]
        else:
            return None

    def get_src(self, target_tag, attribute=None):
        """
        Get the src value from target tag
        :param target_tag: string
        :param attribute: string
        :return: list
        """
        if self.element is not None:
            if attribute is not None:
                self.attributes = attribute
                return str(self.__element.find(target_tag, attrs=self.attributes)["src"]).replace("//", "")
            else:
                return [str(child["src"]).replace("//", "") for child in self.element.find_all(target_tag)]
        else:
            return None

    def get_xml_object(self):
        """
        Get xml object parsed from html element ElementTree
        :return: xml
        """
        return ElementTree.fromstring(self.__element.prettify())

    def get_xml(self):
        """
        Get XML string parsed from html element ElementTree
        :return: string
        """
        return self.__element.prettify()
