# ps2-network-game-launcher
PS2 game launcher for PS4 that can be used directly through the console web browser.<br>
<p align=justify>Can only be used with internet connection (necessary for the covers and it does not work if covers are not shown). It is not capable of sending configuration files and it is only compatible with mast1c0re's ps4-network-game-loader v0.1.2 and below. (Thus it is only compatible with PS4 firmware 10.50 and previous versions. The latest pre-made save by twitter user EchoStretch that contains both USB and Network Loader for 9.0, 10.01 and 10.50 is compatible)<br></p>

Requires [Jupyter Notebook](https://jupyter.org/install) and [voila](https://voila.readthedocs.io/en/stable/install.html). After setting them up following documentation on their respective websites, continue to the next section.

![image](https://github.com/gbarboza88/ps2-network-game-launcher/assets/50859373/94dd83e7-5271-4351-9a23-ab164dcf3304)

## Instructions

<p align=justify> Put your PS2 ISO files in the same root directory as the notebook file. Selfhost jupyter notebook and edit #YOURPS4IPv4 at the end of the PS2ISO.ipynb file by putting your PS4 IPv4 address instead (it can be found in PS4 settings or your router settings. I recommend setting a static IP address for PS4), go to File > Save and Checkpoint, then I recommend going to Kernel > Restart and Run All just the first time. After opening Okage and launching the PS2 Network Game Loader through mast1c0re exploit, press the PS Button, go to browser (without closing Okage), access its voila address (default would be: localhost:8888/voila/render/PS2ISO.ipynb) and select the desired game by clicking on it (there is no feedback or notification, just click once). Press the PS Button, go back to Okage and wait for it to load. To make it easier to access voila, bookmark its address in PS4's web browser.</p> 

Python script written by [McCauley](https://github.com/McCaulay) . Covers do not need to be downloaded, they are retrived from [xlenore's repository](https://github.com/xlenore/ps2-covers.html).
