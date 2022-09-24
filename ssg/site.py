import Path from pathlib
class Site:
    def __init__(self,source,dest):
        self.source = Path(source)
        self.dest = Path(dest)

    def create_dir(self,Path):
        directory = self.dest/Path.relative_to(self.source)
        Path.mkdir(directory,parents = True,exists_ok = True)

    def build():
        path.mkdir(self.dest,parents = True,exists_ok = True)
        for path in self.source.rglob("*"):
            if Path.is_dir(path):
                create_dir(path)
                
