# utf-8
# python-3

from names_dataset import NameDataset

def writefile(filename:str, content:str):
    with open(filename, 'w') as f:
        f.write(content)
        f.close()


