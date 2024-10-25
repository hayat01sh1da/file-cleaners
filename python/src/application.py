import os
import glob

class InvalidModeError(Exception):
    pass

class Application:
    def __init__(self, dirname, pattern, mode = 'd'):
        self.pattern = pattern
        self.mode    = mode
        self.files   = glob.glob(os.path.join(dirname, '**', pattern), recursive = True)

    def run(self):
        self.__validate__(self.mode)

        print('Target dirname is {current_directory}'.format(current_directory = os.getcwd()))
        if len(self.files) > 1:
            print('========== [{exec_mode}] Total File Count to Clean: {files_length} =========='.format(exec_mode = self.__exec_mode__(), files_length = len(self.files)))
            print('========== [{exec_mode}] Start Cleaning {pattern} =========='.format(exec_mode = self.__exec_mode__(), pattern = self.pattern))
            for file in self.files:
                print('========== [{exec_mode}] Cleaning {file} =========='.format(exec_mode = self.__exec_mode__(), file = file))
                if self.mode == 'e':
                    os.remove(file)
            print('========== [{exec_mode}] Cleaned {pattern} =========='.format(exec_mode = self.__exec_mode__(), pattern = self.pattern))
            print('========== [{exec_mode}] Total Cleaned File Count: {files_length} =========='.format(exec_mode = self.__exec_mode__(), files_length = len(self.files)))
        else:
            print('========== [{exec_mode}] No {pattern} Remains =========='.format(exec_mode = self.__exec_mode__(), pattern = self.pattern))

    # private

    def __validate__(self, mode):
        match mode:
            case 'd' | 'e':
                return
            case _:
                raise InvalidModeError('{mode} is invalid mode. Provide either `d`(default) or `e`.'.format(mode = self.mode))

    def __exec_mode__(self):
        if self.mode == 'e':
            return 'EXECUTION'
        else:
            return 'DRY_RUN'
