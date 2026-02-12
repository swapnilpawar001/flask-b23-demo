#!/bin/bash
sudo systemctl daemon-reload
sudo systemctl restart flaskapp
sudo systemctl restart nginx
