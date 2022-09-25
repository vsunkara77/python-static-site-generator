import re
from yaml import load
from yaml import FullLoader
from collections.abc import Mapping

class Content(Mapping):
    __delimiter = r"^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimiter,re.MULTILINE)
