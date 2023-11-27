# Eco-Logic Home: Intelligent Living for a Sustainable Tomorrow with [HomeAssistant](https://www.home-assistant.io) (HASS)

Welcome to Eco-Logic Home, where smart living meets sustainability, powered by Home Assistant. Eco-Logic goes beyond the basics, using machine learning and GPT tech to tailor your home's automation to your habits while keeping it eco-friendly.

## Eco-Logic Home

Step into Eco-Logic Home, where eco-conscious vibes and clever automation, teaming up with Home Assistant, turn your place into a chill spot of smarts and sustainability.

**Eco-Logic**, no fancy stuff, just a name that says we're about more than basic smart homes. We're into making your crib Earth-friendly and smart as a whip. We're talking about whipping up machine learning tricks to match your style and giving a nod to nature by keeping things energy-efficient with our GPT tech.

So, kick back, relax, and let's make your home a cool mix of tech and eco-friendly vibes!

**Eco-Logic**, as the name suggests, goes beyond mere smart home functionalities. It embodies a commitment to making your home both ecologically sound and logically responsive. This means not only creating machine learning models tailored to your habits but also assessing their ecological impact and promoting energy efficiency through the innovative use of GPT (Generative Pre-trained Transformer) technology.

## System Requirements and Configuration

Before diving into the world of Eco-Logic, ensure your system meets the following requirements:

- Docker must be installed and functioning as this program is designed to run within a Docker environment.

- **Home Assistant Integration:**
  - Eco-Logic relies on Home Assistant for data and API communication.
  - Home Assistant must be configured and operational for at least 2 months.
<br><br>
- **Long-Term Token:**
  - Provide the program with a long-term token generated by Home Assistant for seamless communication.
<br><br>
- **Patience is Key:**
  - Eco-Logic relies on historical data from Home Assistant to learn and adapt to your lifestyle.

## Examples of Eco-Logic in Action

Here are a few examples to illustrate how Eco-Logic enhances your living experience:

1. **Adaptive Lighting:**
   - Eco-Logic learns your lighting preferences based on historical data.
   - Adjusts the lighting conditions in each room according to your habits, ensuring optimal energy consumption.

2. **Temperature Optimization:**
   - Analyzes your historical temperature settings and weather patterns.
   - Automatically adjusts the thermostat to maintain a comfortable environment while minimizing energy usage.

3. **Energy-Efficient Appliance Usage:**
   - Learns your appliance usage patterns over time.
   - Suggests optimal times to use high-energy-consuming appliances to reduce overall energy consumption.

4. **Smart Energy Management:**
   - Integrates with renewable energy sources and suggests the best times to harness solar or wind power.
   - Maximizes the use of eco-friendly energy options, reducing your carbon footprint.

By combining machine learning with ecological awareness, Eco-Logic Home transforms your residence into a sustainable, intelligent living space.


## Examples of Eco-Logic in Action

Here are a few examples to illustrate how Eco-Logic enhances your living experience:

1. **Adaptive Lighting:**
   - Eco-Logic learns your lighting preferences based on historical data.
   - Adjusts the lighting conditions in each room according to your habits, ensuring optimal energy consumption.

2. **Temperature Optimization:**
   - Analyzes your historical temperature settings and weather patterns.
   - Automatically adjusts the thermostat to maintain a comfortable environment while minimizing energy usage.

3. **Energy-Efficient Appliance Usage:**
   - Learns your appliance usage patterns over time.
   - Suggests optimal times to use high-energy-consuming appliances to reduce overall energy consumption.

4. **Smart Energy Management:**
   - Integrates with renewable energy sources and suggests the best times to harness solar or wind power.
   - Maximizes the use of eco-friendly energy options, reducing your carbon footprint.

By combining machine learning with ecological awareness, Eco-Logic Home transforms your residence into a sustainable, intelligent living space.

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
[ example: cp ecologichome_src/data/config/options.json /var/lib/docker/volumes/ecologichome_config/_data ]

# Edit the options.json
nano <path_to_volume>/options.json
[ example: nano /var/lib/docker/volumes/ecologichome_config/_data/options.json ]

# Start the docker-compose
docker-compose up -d (or docker compose up -d)
# ... wait for build ~3-5 min
If you see the message "✔ Container ecologichome Started," it means that the program has been successfully installed.


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