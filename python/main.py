import sys
sys.path.append('./src')
from application import Application

dirname = input('Provide the directory which contains files you would like to delete: ')
pattern = input('Provide the dirname or filename pattern you would like to delete: ')
mode    = input('Provide -e(execution) if you would truly like to delete the files. This operation is cannot be undone, so trying to run without -e(dry_run) once is strongly recommended: ')

Application(dirname = dirname, pattern = pattern, mode = mode).run()
