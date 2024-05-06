import os
import glob

class Application:
    def __init__(self, dirname, filename, mode = None):
        self.filename = filename
        self.mode     = mode
        self.files    = glob.glob(os.path.join(dirname, '**', filename), recursive = True)

    def run(self):
        print('Target dirname is {current_directory}'.format(current_directory = os.getcwd()))
        if len(self.files) > 1:
            print('========== [{exec_mode}] Total File Count to Clean: {files_length} =========='.format(exec_mode = self.__exec_mode__(), files_length = len(self.files)))
            print('========== [{exec_mode}] Start Cleaning {filename} =========='.format(exec_mode = self.__exec_mode__(), filename = self.filename))
            for file in self.files:
                print('========== [{exec_mode}] Cleaning {file} =========='.format(exec_mode = self.__exec_mode__(), file = file))
                if self.mode == '-e':
                    os.remove(file)
            print('========== [{exec_mode}] Cleaned {filename} =========='.format(exec_mode = self.__exec_mode__(), filename = self.filename))
            print('========== [{exec_mode}] Total Cleaned File Count: {files_length} =========='.format(exec_mode = self.__exec_mode__(), files_length = len(self.files)))
        else:
            print('========== [{exec_mode}] No {filename} Remains =========='.format(exec_mode = self.__exec_mode__(), filename = self.filename))

    # private

    def __exec_mode__(self):
        if self.mode == '-e':
            return 'EXECUTION'
        else:
            return 'DRY_RUN'
