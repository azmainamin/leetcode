"""
FileSystem() Initializes the object of the system.
List<String> ls(String path)
    If path is a file path, returns a list that only contains this file's name.
    If path is a directory path, returns the list of file and directory names in this directory.
The answer should in lexicographic order.
void mkdir(String path) Makes a new directory according to the given path. The given directory path does not exist. If the middle directories in the path do not exist, you should create them as well.
void addContentToFile(String filePath, String content)
    If filePath does not exist, creates that file containing given content.
    If filePath already exists, appends the given content to original content.
String readContentFromFile(String filePath) Returns the content in the file at filePath.
"""

class TrieNode:
    def __init__(self, isFile=False, content=""):
        self.isFile = isFile
        self.content = content
        self.children = {}

class FileSystem:

    def __init__(self):
        self.root = TrieNode()
        

    def ls(self, path: str):
        if path == "/":
            return sorted(list(self.root.children.keys()))
        
        paths = path.split("/") # ["a", "b"]
        
        current_dir = self.root
        
        # need to traverse down path
        for p in paths:
            if not p: # remove empty strings in paths list
                continue
            # we can do this, because ls won't be called for a dir/file that does not exist
            current_dir = current_dir.children.get(p)
        
        if current_dir.isFile:
            return [p]
        
        all_dirs_files = sorted(list(current_dir.children.keys()))
        
        return all_dirs_files

    def mkdir(self, path: str) -> None:
        current_node = self.root
        
        paths = path.split("/")
        for p in paths:
            if not p: continue
            
            # peek to see if subdir exist or not
            if p in current_node.children:
                current_node = current_node.children.get(p)
            else:
                # if not, create it
                new_node = TrieNode()
                current_node.children[p] = new_node
                current_node = new_node
                

    def addContentToFile(self, filePath: str, content: str) -> None:
        current_node = self.root
        
        paths = filePath.split("/")
        for p in paths:
            if not p: continue
            
            if p in current_node.children:
                current_node = current_node.children.get(p)

            else:
                # Only way we don't see it in children is if we are
                # at the last elem of paths, which is the file name
                # and the file does not exist
                # So we need to create
                new_node = TrieNode(isFile=True)
                new_node.content = content
                current_node.children[p] = new_node
                return 
        
        # end of paths and file exists, otherwise we would have returned in line 70
        current_node.content += content
        return

    def readContentFromFile(self, filePath: str) -> str:
        current_node = self.root
        
        paths = filePath.split("/")
        for p in paths:
            if not p: continue
            
            current_node = current_node.children.get(p)
        
        return current_node.content
                


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)