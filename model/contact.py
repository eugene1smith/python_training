__author__ = 'Eugene'

from sys import maxsize

class Contact:

    def __init__(self, first_name=None, last_name=None, nickname=None, title=None, company_name=None, address=None, home=None, mobile=None,
                work=None, fax=None, first=None, second=None, third=None, homepage=None, birth_year=None, an_year=None, second_address=None, home_address=None, notes=None, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.nickname = nickname
        self.title = title
        self.company_name = company_name
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.first = first
        self.second = second
        self.third = third
        self.homepage = homepage
        self.birth_year = birth_year
        self.an_year = an_year
        self.second_address = second_address
        self.home_address = home_address
        self.notes = notes
        self.id = id


    def __repr__(self):
        return "%s:%s %s" % (self.id, self.first_name, self.last_name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.first_name == other.first_name and self.last_name == other.last_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize