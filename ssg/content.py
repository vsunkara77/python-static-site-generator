import re
from yaml import load
from yaml import FullLoader
from collections.abc import mapping

class Content(mapping):
    __delimeter = "^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimeter,re.MULTILINE)
    
