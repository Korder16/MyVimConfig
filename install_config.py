import shutil
import os.path

HOME_DIR = os.path.expanduser("~")
CONFIG_FILE_PATH = os.path.join(HOME_DIR, '.config/nvim/')
OLD_CONFIG_FILE = os.path.join(HOME_DIR, '.config/nvim/init.vim')
OLD_CONFIG_FILE_COPY = os.path.join(HOME_DIR, '.config/nvim/init_old.vim')


def is_dir_exists(dir_path: str) -> bool:
    """ Checks if CONFIG FILE PATH exists """
    return os.path.exists(dir_path)


def copy_old_file() -> None:
    """ Copy old config file """
    if os.path.isfile(OLD_CONFIG_FILE):
        shutil.copyfile(OLD_CONFIG_FILE, OLD_CONFIG_FILE_COPY)
        print(f'Old config file copied: {OLD_CONFIG_FILE_COPY}')


def install_new_config() -> None:
    """ Install new config file """
    MY_CONFIG_FILE = 'init.vim'
    shutil.copyfile(MY_CONFIG_FILE, OLD_CONFIG_FILE)
    print(f'New config file installed: {OLD_CONFIG_FILE}')


if __name__ == '__main__':
    print("Do you want to install new config file? y/n")
    answer = str(input())
    if answer.lower() == 'y':
        if not is_dir_exists(CONFIG_FILE_PATH):
            os.mkdir(CONFIG_FILE_PATH)

        copy_old_file()
        install_new_config()

    else:
        print("Ok then, keep your secrets")
