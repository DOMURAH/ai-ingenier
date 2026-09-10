from dataclasses import dataclass
import os

@dataclass
class Temporary_folder:
    new_way : str
    old_way : str = os.getcwd()
    
    def __enter__(self):
        if not os.path.exists(self.new_way):
            os.mkdir(self.new_way)
        os.chdir(self.new_way)
        
    def __exit__(self, exc_type, exc, tb):
        os.chdir(self.old_way)
        os.system("echo 'Le teste a reussie ! ' > retour.txt")
        
with Temporary_folder("FICHIER") as t:
    os.system("touch test.txt")