#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import with_statement

import main

class Item(object):
    def __init__(self, parent, name, value):
        self.parent = parent
        self.name = name
        self.value = value
        self.type = ''
        self.default = ''
        self.max = ''
        self.min = ''
        self.info = ''

    def setType(self, type_):
        self.type = type_

    def setDefaultValue(self, default):
        self.default = default

    def setInfo(self, info):
        self.info = info

    def setMin(self, min):
        self.min = min

    def setMax(self, max):
        self.max = max

    def setValue(self, value):
        self.value = value

    def __str__(self):
        return '[{name} type:{type} default:{default} min:{min} max:{max} info:{info}]'.format(
        name = self.name,
        type= self.type,
        default = self.default,
        min = self.min,
        max = self.max,
        info= self.info)


class Config(object):
    def __init__(self, configDir, name):
        self.configDir = configDir
        self.name = name
        self.items = {}

    def readFile(self):
        commentLines = []
        itemLines = []
        with open(self.configDir + '\\' + self.name) as file:
            for line in file:
                if line.isspace():
                    pass
                elif line.startswith('#'):
                    commentLines.append(line)
                else:
                    itemLines.append(line)
        for itemLine in itemLines:
            item = Item(self.name, itemLine.split('=')[0], itemLine.split('=')[1])
            for commentLine in commentLines:
                if commentLine.find(item.name) > -1:
                    commentLine = commentLine.replace('MLProp : ', '')
                    import re
                    pattern = r'^#[ ]*(?P<name>.+)[ ]*[(](?P<type>.+?):(?P<detail>.*?)[)](?: -- )?(?P<info>.*)$'
                    p = re.compile(pattern)
                    m = p.search(commentLine)
                    if m:
                        type_ = m.group('type').lower()
                        detail = m.group('detail')
                        info = m.group('info')
                        if type_.count('string'):
                            item.setType('string')
                            item.setDefaultValue(detail)
                        else:
                            item.setType(m.group('type'))
                            detail_ = detail.split(',')
                            item.setDefaultValue(detail_[0])
                            for data in detail_:
                                if data.count('>='):
                                    item.setMin(data.replace('>=', ''))
                                if data.count('<='):
                                    item.setMax(data.replace('<=', ''))
                        item.setInfo(info)
            self.items[item.name] = item

    def writeFile(self):
        import tempfile, os, shutil
        tmpfd,tmpname = tempfile.mkstemp(dir = '.')
        with open(self.configDir + '\\' + self.name) as input, os.fdopen(tmpfd, 'w') as output:
            lines = input.readlines()
            for line in lines:
                if not line.startswith('#'):
                    for item in self.items.values():
                        if line.find(item.name) > -1:
                            newline = item.name + '=' + item.value
                            if line != newline:
                                line = newline + '\n'
                output.write(line)
        shutil.copyfile(tmpname, self.configDir + '\\' + self.name)
        os.remove(tmpname)


