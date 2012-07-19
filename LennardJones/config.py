import yaml
import sys

filename = sys.argv[1]
with open(filename, 'r') as f:
    config = yaml.load(f)
