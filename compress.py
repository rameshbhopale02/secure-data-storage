import pyminizip


input = "data.yaml"
pre = None
output = "compress.zip"
password = "abcdef"
com_level = 5
pyminizip.compress(input, None, output, password, com_level)

