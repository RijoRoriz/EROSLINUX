# EROSLINUX

To be able to run this image on ZCU104, firstly, you need to follow the standard procedure of creating a bootable SD card:

- Create two partitions, one ext4 (Linux Filesystem) and the other FAT32 (Boot files) on the SD card (GParted tool on Linux does the job for me);
- Copy the files from "EROSLINUX/bootfiles" into the SD card FAT32 partition;
- Copy the files from "EROSLINUX/filesystem" into the SD card EXT4 partition (use sudo if needed);

Put the SD card into the ZCU104 SD card slot and confirm that the board is ready to boot from SD cards.

Connect the ZCU104 into your computer through UART and open a serial communication terminal (It is assumed that you are using Linux):

- type "sudo minicom -s". Since the minicom is a lightweight tool and fulfils the needs, it is used in this tutorial. Use others at your own risk. In addition, the sudo plus -s flag assure that the terminal doesn't not close after reboots or resets and allows the following configurations:
  - Serial port setup/ 
    - A - Serial Device : /dev/ttyUSB1
    - F - Hardware Flow Control: No
    - G - Hardware Flow Control: No

Finally, power up your board and the boot process will supposedly start to appear in your terminal.

