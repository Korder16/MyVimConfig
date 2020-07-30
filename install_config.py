import shutil 
import os.path

HOME_DIR = os.path.expanduser("~")
OLD_CONFIG_FILE = os.path.join(HOME_DIR, '.config/nvim/init.vim')
OLD_CONFIG_FILE_COPY = os.path.join(HOME_DIR, '.config/nvim/init_old.vim')


def copy_old_file():
    """ Copy old config file """
    if os.path.isfile(OLD_CONFIG_FILE):
        shutil.copyfile(OLD_CONFIG_FILE, OLD_CONFIG_FILE_COPY)
        print(f'Old config file copied: {OLD_CONFIG_FILE_COPY}')


def install_new_config():
    """ Install new config file """
    MY_CONFIG_FILE = 'init.vim'   
    shutil.copyfile(MY_CONFIG_FILE, OLD_CONFIG_FILE)
    print(f'New config file installed: {OLD_CONFIG_FILE}')


if __name__ == '__main__':
    print("Do you want to install new config file? Yes/no")
    asnwer = str(input())
    if asnwer.lower() == 'yes':
        copy_old_file()
        install_new_config()
    else:
        print("Ok then, keep your secrets")
