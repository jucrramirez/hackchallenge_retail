def readProductsFile(path):
    f = open(path, 'r', encoding='utf8').read()
    products = f.split('\n')
    
    return products

print(readProductsFile('./products.txt'))