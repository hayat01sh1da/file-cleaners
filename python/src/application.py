import os
import glob
import inspect

class InvalidModeError(Exception):
    pass

class Application:
    def __init__(self, dirname: str = '.', pattern: str = '*', mode: str = 'd') -> None:
        self.dirname: str   = dirname
        self.pattern: str   = pattern
        self.mode: str      = mode
        self.files: list[str]     = glob.glob(os.path.join(dirname, '**', pattern), recursive = True)
        self.exec_mode: str = self.__exec_mode__()
        self.env: str       = inspect.stack()[1].filename.split('/')[-2]

    def run(self) -> None:
        self.__validate__()
        self.__output__(f'Target dirname is {os.path.abspath(self.dirname)}')
        if len(self.files) > 1:
            self.__output__(f'========== [{self.__exec_mode__()}] Total File Count to Clean: {len(self.files)} ==========')
            self.__output__(f'========== [{self.__exec_mode__()}] Start Cleaning {self.pattern} ==========')
            for file in self.files:
                self.__output__(f'========== [{self.__exec_mode__()}] Cleaning {file} ==========')
                if self.mode == 'e':
                    os.remove(file)
            self.__output__(f'========== [{self.__exec_mode__()}] Cleaned {self.pattern} ==========')
            self.__output__(f'========== [{self.__exec_mode__()}] Total Cleaned File Count: {len(self.files)} ==========')
        else:
            self.__output__(f'========== [{self.__exec_mode__()}] No {self.pattern} Remains ==========')

    # private

    def __validate__(self) -> None:
        match self.mode:
            case 'd' | 'e':
                return
            case _:
                raise InvalidModeError(f'{self.mode} is invalid mode. Provide either `d`(default) or `e`.')

    def __exec_mode__(self) -> str:
        if self.mode == 'e':
            return 'EXECUTION'
        else:
            return 'DRY_RUN'

    def __is_test_env__(self) -> bool:
        return self.env == 'test'

    def __output__(self, message: str) -> None:
        if not self.__is_test_env__():
            print(message)
