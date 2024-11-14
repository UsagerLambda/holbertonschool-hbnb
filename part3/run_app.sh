#!/bin/bash
lsof -i tcp:5000
sleep 3
export PYTHONDONTWRITEBYTECODE=1
python3 run.py
