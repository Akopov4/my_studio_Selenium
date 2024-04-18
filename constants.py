import yaml
import os


file = f'{os.path.dirname(os.path.abspath(__file__))}/config/configs.yaml'


with open(file, 'r') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)
    
    
    
MAIN_PAGE= config['main_page']    
MANGER_EMAIL= config['role_manager_email']
MANAGER_PASS = config['role_manager_pass']
STAFF_EMAIl= config['role_staff_email']
STAFF_PASS=config['role_staff_pass']
BROWSER =config['browser']
