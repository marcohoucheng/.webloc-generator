import os

def main():
    
    path = './'

    for filename in os.listdir(path):
        if filename.startswith('X2Download.com'):
            print(filename)
            os.rename(filename, filename[len('X2Download.com-'):])
        
    return 0

if __name__ == "__main__":
   main()