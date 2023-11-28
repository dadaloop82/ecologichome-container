# Library imports

import os

# Local application imports
from ecologichome.model_creator.read_config_json import replace_yaml
from ecologichome.model_creator.read_config_json import run_cron
from ecologichome.model_creator.parse_data import parse_data_from_db
from ecologichome.model_creator.learning_model import train_all_actuator_models
from ecologichome.model_creator.logger import add_logger
from ecologichome.model_creator.config_checker import base_config_checks


if __name__ == "__main__":
    
    logname = "/ecologichome_src/log/ecologichome.log"
    if not os.path.exists(os.path.dirname(logname)):
        os.makedirs(os.path.dirname(logname))    

    add_logger(logname)
    base_config_checks()
    replace_yaml()
    parse_data_from_db()
    train_all_actuator_models()
    run_cron()
