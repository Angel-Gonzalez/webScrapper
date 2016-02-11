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
        self.__element = element
        self.__text = None
        self.__href = None

    @property
    def tag(self):
        """
        Get the type of the element
        :return: string
        """
        return self.__tag

    @tag.setter
    def tag(self, value):
        """
        Set target tag for scrap
        :param value: string
        :return:
        """
        self.__tag = value

    @property
    def classes(self):
        """
        Get classes for target element
        :return: string
        """
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
            s = BeautifulSoup(str(self.__element), "lxml")
            if self.tag is not None and self.__text is None:
                if self.__attr is not None:
                    self.__text = get_str(s.find(self.tag, self.attributes))
                elif self.classes is not None:
                    self.__text = get_str(s.find(self.tag, self.classes))
                return self.__text
            else:
                self.__text = s.text
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
        return self.__attr

    @attributes.setter
    def attributes(self, value):
        """
        Set attributes for target tag key:value
        :param value: string
        :return:
        """
        key, val = str(value).split(":")
        self.__attr = "attrs={\"%s\": \"%s\"}" % (key, val)

    @property
    def href(self):
        """
        Get href attribute from tag type a
        :return: string
        """
        if self.tag == "a":
            s = BeautifulSoup(str(self.__element), "lxml")
            self.__href = get_href(s.find("a", self.classes))
            return self.__href
        else:
            return self.__href

    def get_child(self, target_tag, target_class=None):
        """
        Get target child elements
        :param target_tag: string
        :param target_class: string
        :return: list
        """
        if self.element is not None:
            s = BeautifulSoup(str(self.__element), "lxml")
            if target_class is not None:
                return [Element(child) for child in s.find_all(target_tag, target_class)]
            else:
                return [Element(child) for child in s.find_all(target_tag)]
        else:
            return None
