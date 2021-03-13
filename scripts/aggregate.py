import os

def scan_files(folder: str):
    for root, dirs, files in os.walk(folder):
        for file in files:
            filename, extension = os.path.splitext(file)
            if extension is '.txt':
                print(filename)

def aggregate_benchmarks():
    print('do something')

def parse_file(file):
    print('do something')

def write_file():
    print('do something')

def main():
    print('do something')
