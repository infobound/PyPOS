class Functions:
    """these are generic functions that are used in many differnt places"""

    def init(self):
        return

    def ParsePathToList(self,Path):
        #turns a url type string to a list of nodes
        #Expected: Path="C:\Windows\system32\regedit.exe"
        #Expected: Path="//server/share/folder"

        Path=Path.replace("\\\\","/")
        Path=Path.replace("\\","/")
        if Path.find("//",0,2)=="//":
            Path=Path[2]

        PathList=Path.split("/")
        return PathList
