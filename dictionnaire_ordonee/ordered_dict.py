#!/usr/local/bin/python3.6
# -*-coding:Utf-8 -*

class       OrderedDictionary:
    """Ordered dictionary is an object similar to dictonary with the difference that it's ordered"""

    def     __init__(self, **data):
        self._key = []
        self._value = []
        for key in data:
            self._key.append(key)
            self._value.append(data[key])

    def     __repr__(self):
        last = len(self._key) - 1
        dicto = "{"
        for i, elm in enumerate(self._key):
            if i != last:
                dicto += "'{}': {}, ".format(self._key[i], self._value[i])
            else:
                dicto += "'{}': {}".format(self._key[i], self._value[i])
        dicto += "}"
        return dicto

    def     __getitem__(self, key):
        index = self._key.index(key)
        return self._value[index]

    def     __setitem__(self, key, value):
        try:
            index = self._key.index(key)
            self._value[index] = value
        except ValueError:
            self._key.append(key)
            self._value.append(value)

    def     __len__(self):
        return len(self._key)

    def     __add__(self, obj2add):
        if type(obj2add)\
                is not type(self):
            raise TypeError(\
                    "{} can't be added to OrderedDictionary"\
                    .format(type(obj2add)))
        sum_dic = OrderedDictionary()
        sum_dic._key = self._key + obj2add._key
        sum_dic._value = self._value + obj2add._value
        return (sum_dic)

    def     __delitem__(self, key):
        index = self._key.index(key)
        del self._key[index]
        del self._value[index]

    def     __contains__(self, key):
        return (key in self._key)

    def     __iter__(self):
        for key in self._key:
            yield key

    def     sort(self):
        sorted_key = []
        sorted_val = []
        for k, v in sorted(zip(self._key, self._value)):
            sorted_key.append(k)
            sorted_val.append(v)
        del self._key
        del self._value
        self._key = sorted_key
        self._value = sorted_val

    def     reverse(self):
        self._key.reverse()
        self._value.reverse()

    def     keys(self):
        return list(self._key)

    def     values(self):
        return list(self._value)

    def     items(self):
        return zip(self._key, self._value)
