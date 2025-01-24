import os
import glob
import inspect

class InvalidModeError(Exception):
    pass

class Application:
    def __init__(self, dirname, pattern, mode = 'd'):
        self.dirname = dirname
        self.pattern = pattern
        self.mode    = mode
        self.files   = glob.glob(os.path.join(dirname, '**', pattern), recursive = True)
        self.env     = inspect.stack()[1].filename.split('/')[-2]

    def run(self):
        self.__validate__(self.mode)
        self.__output__('Target dirname is {current_directory}'.format(current_directory = os.path.abspath(self.dirname)))
        if len(self.files) > 1:
            self.__output__('========== [{exec_mode}] Total File Count to Clean: {files_length} =========='.format(exec_mode = self.__exec_mode__(), files_length = len(self.files)))
            self.__output__('========== [{exec_mode}] Start Cleaning {pattern} =========='.format(exec_mode = self.__exec_mode__(), pattern = self.pattern))
            for file in self.files:
                self.__output__('========== [{exec_mode}] Cleaning {file} =========='.format(exec_mode = self.__exec_mode__(), file = file))
                if self.mode == 'e':
                    os.remove(file)
            self.__output__('========== [{exec_mode}] Cleaned {pattern} =========='.format(exec_mode = self.__exec_mode__(), pattern = self.pattern))
            self.__output__('========== [{exec_mode}] Total Cleaned File Count: {files_length} =========='.format(exec_mode = self.__exec_mode__(), files_length = len(self.files)))
        else:
            self.__output__('========== [{exec_mode}] No {pattern} Remains =========='.format(exec_mode = self.__exec_mode__(), pattern = self.pattern))

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

    def __is_test_env__(self):
        return self.env == 'test'

    def __output__(self, message):
        if not self.__is_test_env__():
            print(message)
