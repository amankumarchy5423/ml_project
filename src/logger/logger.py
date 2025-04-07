import logging
from src.utils.utils import create_dir
from datetime import datetime
import os 
# from src.utils import LOGGING_DIR

LOGGING_DIR = "logs"    
LOGGING_FILE = "app.log"

log_file = f"{datetime.now().strftime("%Y_%m_%d__%H_%M")}.log"
# create_dir(LOGGING_DIR)
logs_info = os.path.join(LOGGING_DIR,log_file)
if not os.path.exists(logs_info):
    create_dir(logs_info)

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] [%(threadName)s] [%(levelname)s][%(message)s]",
    datefmt='%Y_%m_%d %H:%M:%S',
    filename=logs_info,
)

my_logger = logging.getLogger('<<<logger>>>')
