import re
from yaml import load, FullLoader
from collections.abc import Mapping


class Content(Mapping):
    
    __delimiter = r"^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimiter, re.MULTILINE)

    @classmethod
    def load(cls, string):
        _, fm, content = cls.__regex.split(string, 2)
        
        metadata = load(fm, FullLoader)
        return cls(metadata, content)
    
    def __init__(self, metadata, content):
        self.data = metadata
        self.data["content"] = content
        
    @property
    def body(self):
        return self.data["content"]
    
    @property
    def type(self):
        return self.data.get("type")

    @type.setter
    def type(self, value):
        self.data["type"] = value
        
    def __getitem__(self, key):
        return self.date.get(key)
    
    def __iter__(self):
        return self.data.__iter__()
    
    def __len__(self):
        return len(self.data)
    
    def __repr__(self):
        data = { key: value for key, value in self.data.items() if key != "content" }
        return str(data)
