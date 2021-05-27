from configparser import ConfigParser
import glob
import os


def read_variable_from_config(var):
    config = ConfigParser()
    config.read('variables.ini')
    res = config['DEFAULT'][var]
    if res is None:
        raise Exception(f'Cannot get {var} from ini file')
    else:
        print(f'{var}: {res}')
        return res


def get_latest_file_from_folder(folder):
    list_of_files = glob.glob(folder)
    latest_file = max(list_of_files, key=os.path.getctime)
    print(f'get latest file: {latest_file}')
    return latest_file


def get_file_count_from_folder(folder):
    return len([name for name in os.listdir(folder) if os.path.isfile(os.path.join(folder, name))])
