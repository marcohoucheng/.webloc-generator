import os

def main():
    path = './'
    
    folders = [
        entry
        for entry in os.listdir(path)
        if os.path.isdir(os.path.join(path, entry))
    ]

    for folder in folders:
        files = os.listdir(os.path.join(path, folder))
        for i, file in enumerate(files):
            if not os.path.isfile(os.path.join(path, folder, file)):
                continue
            _, file_ext = os.path.splitext(file)
            new_name = folder.replace(' ', '_') + '_' + str(i).zfill(3)
            os.rename(
                os.path.join(path, folder, file),
                os.path.join(path, folder, new_name + file_ext)
            )
        
    return 0

if __name__ == "__main__":
   main()
