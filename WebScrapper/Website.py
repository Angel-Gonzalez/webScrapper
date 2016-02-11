from urllib.parse import urlparse, parse_qs


class Website(object):
    def __init__(self, url):
        super().__init__()
        self.url = url
        self.__query = None
        self.__sequence = None
        self.__path = None

    @property
    def domain(self):
        """
        Get the domain string based on the original url
        :return: string
        """
        if self.url is not None:
            return "{uri.netloc}".format(uri=urlparse(self.url))
        else:
            return None

    @property
    def path(self):
        """
        Get the path of original url
        :return: string
        """
        if self.__path is None:
            return "{uri.path}".format(uri=urlparse(self.url))
        else:
            return self.__path

    @path.setter
    def path(self, value):
        """
        Set the path for url
        :param value: string
        :return:
        """
        self.__path = value

    @property
    def query(self):
        """ Get url's part query
        :return: string
        """
        if self.__query is None:
            self.__query = "{uri.query}".format(uri=urlparse(self.url))
        return self.__query

    @query.setter
    def query(self, value):
        """
        :param value: query string should use ? for sequence replacement
        :return:
        """
        self.__query = value

    def construct_queries(self, start=None, end=None):
        global q
        if len(self.query) > 0 and start < end:
            k = list(parse_qs(self.query).keys())[0]
            q = []
            for s in range(start, end + 1):
                q.append("{uri.scheme}://{uri.netloc}/{uri.path}?{param}={s}".format(uri=urlparse(self.url), param=k,
                                                                                     s=s))
        return q
