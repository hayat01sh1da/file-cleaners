import sys
sys.path.append('./src')
from application import Application

try:
    _, dirname, filename, mode, *_ = sys.argv
except ValueError:
    _, dirname, filename, *_ = sys.argv
    mode                     = '-d'

Application(dirname = dirname, filename = filename, mode = mode).run()
