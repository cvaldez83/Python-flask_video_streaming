#!/bin/bash

echo "Installing python environment venv"
python3 -m venv venv

echo "Activating python environment"
. ae.sh

echo "Installing (via apt-get) portaudio19-dev"
sudo apt-get install portaudio19-dev

echo "Pip installing requirements.txt"
pip install -r requirements.txt
