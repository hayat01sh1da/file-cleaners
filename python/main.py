import sys
import os
import shutil
import glob
sys.path.append('./src')
from application import Application

dirname = input('Provide the directory which contains files you would like to delete: ').strip()
pattern = input('Provide the dirname or filename pattern you would like to delete: ').strip()
mode    = input('Provide d(dry_run: default) to make sure what directories and files are to be delete first. Then, provide e(execution) if you would truly like to delete the files. This operation is cannot be undone, so be alert to your operation!: ').strip()

params = dict()
for key, value in { 'dirname': dirname, 'pattern': pattern, 'mode': mode }.items():
    if value:
        params[key] = value

Application(**params).run()

pycaches = glob.glob(os.path.join('.', '**', '__pycache__'), recursive = True)
for pycache in pycaches:
    if os.path.exists(pycache):
        shutil.rmtree(pycache)
