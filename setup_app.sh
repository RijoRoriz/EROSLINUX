#!/bin/bash
sudo cp /home/ricardororiz/Desktop/vitis_projects/ZCU104_EROSLINUX_APP/Debug/ZCU104_EROSLINUX_APP.elf /home/ricardororiz/embeddedLiDAR/EROSLINUX/app/
sudo cp /home/ricardororiz/Desktop/vitis_projects/ZCU104_EROSLINUX_APP/src/* /home/ricardororiz/embeddedLiDAR/EROSLINUX/app/src/
echo "All src, headers and elf files copied to git folder"

sudo cp /home/ricardororiz/Desktop/vitis_projects/ZCU104_EROSLINUX_APP/Debug/ZCU104_EROSLINUX_APP.elf /media/ricardororiz/FILESYSTEM/home/
echo "Elf files copied to SD card"