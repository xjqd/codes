#!/bin/python
class Request(object):
    def __init__(self, val):
        self.val = val
    def get_request(self):
        return self.val

class Response(object):
    def __init__(self,val):
        self.val = val
    def get_response(self):
        return self.val

class FilterChain(object):
    def __init__(self):
        self.li = []
    def add_filter(self, element=None):
        self.li.append(element)
    def do_filter(self, request=None, response=None, filter_chain=None):
        for f in self.li:
            f.do_filter(request, response,filter_chain)


class HtmlFilter(object):
    def do_filter(self, request=None, response=None, filter_chain=None):
        req_str = request.get_request()
        print req_str
        #filter_chain.do_filter(request, response, filter_chain)
        res_str = response.get_response()
        print res_str

if __name__ == "__main__":
    req = Request("hi")
    res = Response("+world")
    filterchain = FilterChain()
    filterchain.add_filter(HtmlFilter())
    filterchain.do_filter(req, res, filterchain)
