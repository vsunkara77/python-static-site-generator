from typing import List
from pathlib import path

class Parser:
    extensions: list[str] = []

    def valid_extension(self,extension):
        if extension in self.extensions:
            pass
