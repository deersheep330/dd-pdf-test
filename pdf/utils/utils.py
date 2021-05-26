from configparser import ConfigParser


def read_variable_from_config(var):
    config = ConfigParser()
    config.read('variables.ini')
    res = config['DEFAULT'][var]
    if res is None:
        raise Exception(f'Cannot get {var} from ini file')
    else:
        print(f'{var}: {res}')
        return res
