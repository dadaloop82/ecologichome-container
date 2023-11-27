# Library imports
# Local application imports
from ecologichome.model_creator.read_config_json import replace_yaml
from ecologichome.model_creator.read_config_json import run_cron
from ecologichome.model_creator.parse_data import parse_data_from_db
from ecologichome.model_creator.learning_model import train_all_actuator_models
from ecologichome.model_creator.logger import add_logger
from ecologichome.model_creator.config_checker import base_config_checks


if __name__ == "__main__":
    
    add_logger()
    base_config_checks()
    replace_yaml()
    parse_data_from_db()
    train_all_actuator_models()
    run_cron()
