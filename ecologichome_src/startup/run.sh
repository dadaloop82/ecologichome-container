# !/bin/bash
echo "Starting to parse DB data"

if  python3 -m ecologichome.model_creator.main; then
    echo "Starting Appdaemon"
    nohup appdaemon -c /ecologichome_src/appdaemon/ & 
else
    echo "Model generation failed."
fi
echo "Starting frontend on 0.0.0.0:2300"
PORT=2300 node /ecologichome_src/frontend/build/index.js
