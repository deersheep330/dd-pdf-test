from configparser import ConfigParser
import glob
import os
import shutil
from tika import parser


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
    list_of_files = glob.glob(os.path.join(folder, '*'))
    latest_file = max(list_of_files, key=os.path.getctime)
    print(f'get latest file: {latest_file}')
    return latest_file


def get_file_count_from_folder(folder):
    return len([name for name in os.listdir(folder) if os.path.isfile(os.path.join(folder, name))])


def remove_all_files_in_folder(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')


def parse_pdf(pdf):
    parsed_pdf = parser.from_file(pdf)
    data = parsed_pdf['content']
    return data


def parse_int_from_str(str):
    try:
        return int(float(str))
    except Exception as e:
        print(f'Cannot parse int from {str}')
        return None
