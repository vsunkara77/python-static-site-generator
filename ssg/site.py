from pathlib import Path
class Site:
    def __init__(self,source,dest):
        self.source = Path(source)
        self.dest = Path(dest)

    def create_dir(self,path):
        directory = self.dest/Path.relative_to(self.source)
        directory.mkdir(parents=True, exists_ok=True)

    def build(self):
        self.dest.mkdir(parents=True, exists_ok=True)
        for path in self.source.rglob("*"):
            if Path.is_dir():
                self.create_dir(path)
