# external imports
from os.path import dirname, realpath
import yaml


with open("configuration.yaml", "r") as file:
    configuration = yaml.load(file, Loader=yaml.FullLoader)

with open("data.yaml", "r") as file:
    data = yaml.load(file, Loader=yaml.FullLoader)

ROOT_DIR = dirname(realpath(__file__))
