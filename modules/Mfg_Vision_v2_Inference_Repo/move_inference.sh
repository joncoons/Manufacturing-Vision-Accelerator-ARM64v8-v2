#!/bin/bash

set -e

exec yes | cp -rf /inference_temp/* /inference_volume &
exec yes | cp -rf /test_images_temp/* /test_images &
exec python3 /app/main.py 