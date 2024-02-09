import urllib.request, json, os, sys, datetime
import pandas as pd

def main():
    if len(sys.argv) > 3:
        print("Too many arguments. Please provide two agruments of the URL and the name.")
        sys.exit(0)
    elif len(sys.argv) == 3:
        url = sys.argv[1]
        name = sys.argv[2]
    elif len(sys.argv) == 2:
        url = sys.argv[1]
        name = input('Please enter the name of the file:\n')
    else:
        url = input('Please enter the URL:\n')
        name = input('Please enter the name of the file:\n')

    if not url.startswith('http://') and not url.startswith('https://'):
        url = 'https://' + url

    string = """<?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
    <plist version="1.0">
    <dict>
        <key>URL</key>
        <string>""" + url + """</string>
    </dict>
    </plist>"""

    name = name + ".webloc"

    f = open(name, "x")
    f.write(string)
    f.close()

if __name__ == "__main__":
    main()