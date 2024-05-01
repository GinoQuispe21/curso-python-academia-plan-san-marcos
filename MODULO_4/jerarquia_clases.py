#print(object.__subclasses__())
print(int.__bases__)

class FileManager:
    def get_file_manage(self):
        pass 

fm = FileManager()

print(fm.__sizeof__()) # 16