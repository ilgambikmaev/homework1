import os
import shutil

class SimpleFileManager:
    def __init__(self, current_directory="."):
        self.current_directory = current_directory

    def list_contents(self):
        return os.listdir(self.current_directory)

    def create_directory(self, directory_name):
        new_directory_path = os.path.join(self.current_directory, directory_name)
        os.makedirs(new_directory_path, exist_ok=True)

    def delete(self, name):
        path = os.path.join(self.current_directory, name)
        if os.path.exists(path):
            if os.path.isdir(path):
                shutil.rmtree(path)
            elif os.path.isfile(path):
                os.remove(path)
            else:
                print(f"{name} не является ни файлом, ни директорией.")
        else:
            print(f"{name} не существует.")

    def copy(self, source, destination):
        source_path = os.path.join(self.current_directory, source)
        destination_path = os.path.join(self.current_directory, destination)
        if os.path.exists(source_path):
            if os.path.isdir(source_path):
                shutil.copytree(source_path, destination_path)
            elif os.path.isfile(source_path):
                shutil.copy2(source_path, destination_path)
            else:
                print(f"{source} не является ни файлом, ни директорией.")
        else:
            print(f"{source} не существует.")

    def move(self, source, destination):
        source_path = os.path.join(self.current_directory, source)
        destination_path = os.path.join(self.current_directory, destination)
        if os.path.exists(source_path):
            shutil.move(source_path, destination_path)
        else:
            print(f"{source} не существует.")

    def search_file(self, filename):
        matches = []
        for root, dirs, files in os.walk(self.current_directory):
            if filename in files:
                matches.append(os.path.join(root, filename))
        return matches

    def change_permissions(self, name, permissions):
        path = os.path.join(self.current_directory, name)
        if os.path.exists(path):
            os.chmod(path, permissions)
        else:
            print(f"{name} не существует.")
