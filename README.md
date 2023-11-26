# Eco-Logic Home: Intelligent Living for a Sustainable Tomorrow

Welcome to Eco-Logic Home, where the fusion of eco-consciousness and logical automation transforms your living space into a haven of intelligence and sustainability.

**Eco-Logic**, as the name suggests, goes beyond mere smart home functionalities. It embodies a commitment to making your home both ecologically sound and logically responsive. This means not only creating machine learning models tailored to your habits but also assessing their ecological impact and promoting energy efficiency through the innovative use of GPT (Generative Pre-trained Transformer) technology.

## Project in Development

Please note that Eco-Logic Home is an ongoing project. Our team is tirelessly working to refine and expand its capabilities. As we continue to innovate, your feedback and contributions are invaluable in shaping the future of smart, eco-friendly living. Stay tuned for updates and join us on this journey toward a more sustainable and intelligent home.

## Acknowledgment

**This project is a fork of the [ecologichome](https://github.com/dadaloop82/ecologichome-container) project by dadaloop82.**

A big shoutout and heartfelt thanks to [dadaloop82](https://github.com/dadaloop82/) for the fantastic groundwork and the opportunity to enhance it. Additionally, we extend our gratitude to [dadaloop82](https://github.com/dadaloop82) for their contributions to the project. It's a collaborative effort, and credit goes to both dadaloop82 and dadaloop82 for making this possible!

The project remains under the same open-source license (GPL) as the original.

</br>

# How it works

Our approach at Eco-Logic Home involves leveraging machine learning to create a personalized and adaptive smart living environment. The process unfolds in three key phases:

### Design

Terminology:
- actuators = Any entity's state you want to create a model and predict for (e.g., living_room_light_1.state, living_room_light_2.state).
- sensors = Entities that act as triggers and conditions (e.g., sensor.occupancy).
- devices = Actuators + sensors

#### 1. Data Extraction
In this initial phase, we tap into the wealth of data stored by Homeassistant. This includes the states of various actuators and the triggering conditions from sensors. The extracted data is then formatted into a machine learning-friendly CSV structure. Each row represents a published state of an actuator, along with the states of other relevant sensors.

Example CSV format:
```csv
actuators, states, created, duplicate, sensor1, sensor2, sensor3, sensor4...
living_room_light, on, 2023-01-01, false, motion_detected, door_open, temperature_high...
```

#### 2. Learning model
Focusing initially on predicting lights, we employ a simple sklearn Decision Tree model. To enhance accuracy, recent data is weighted more heavily, and the last state is considered as a feature input.

#### 3. Appdaemon Execution
Real-time deployment of prediction models is made seamless through the use of Appdaemon. 

For every sensor change, a request is made to predict new states for actuators and execute them.

## Architecture diagram
![Architecture Diagram](https://github.com/dadaloop82/ecologichome-container/raw/master/doc/arch_diagram.png)


</br></br>

# Installation guide

## Dependencies

Homeassistant OS or Container.

Recorder component enabled using MariaDB or PostgreSQL **with auto_purge disabled.**


### Setup for Docker
To install this Docker container on systems with amd64 architecture, follow these steps:
```bash

# Clone the repo ...
git clone https://github.com/dadaloop82/ecologichome-container.git

# ... or update if you have already cloned
cd <path_to source>
git pull

# Create the volume
docker volume create ecologichome_config

# Find the path to volume docker volume inspect ecologichome_config  ...
docker volume inspect ecologichome_config
# ... and get the Mountpoint path
[ example: /var/lib/docker/volumes/ecologichome_config/_data ]

cd ecologichome-container/

# Copy the options.json
cp ecologichome_src/data/config/options.json <path_to_volume>
[ example: cp ecologichome_src\data\config\options.json /var/lib/docker/volumes/ecologichome_config/_data ]

# Edit the options.json
nano <path_to_volume>/options.json
[ example: nano /var/lib/docker/volumes/ecologichome_config/_data/options.json ]

# Start the docker-compose
docker-compose up -d (or docker compose up -d)

If you see the message "✔ Container ecologichome Started," it means that the program has been successfully installed.
# ... wait for build ~3-5 min

# Logging
docker logs -f --tail 50 ecologichome
```
<br><br>
# Configuration File

```yaml
actuators_id: # List of all entity_ids of actuators (array)
sensors_id: # List of all entity_ids of sensors.
db_options: # All settings for connecting to the Homeassistant database
  db_password: # Database password 
  db_username: # Database username e.g homeassistant
  db_host: # Database host 192.168.1.100
  db_port: # Database port '3306'
  db_database: # Database name homeassistant, or the SQLite db filename (`home-assistant_v2.db` is the default)
  db_type: # Database type. Only {sqlite, mariadb, postgres} is supported
ha_options: # All settings for connecting to Homeassistant. These settings are only required for Homeassistant Container setup.
  ha_url: # IP of your Homeassistant
  ha_token: # Long-lived access token. This is required for the Appdaemon.
```

<br><br>

# Additional Information

ToDo

</br></br>

# Contribution Guide

ToDo

</br></br>

# Feature Roadmap

ToDo