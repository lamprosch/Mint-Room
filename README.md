MINT ROOM - BINAURAL MIXER APP<br/>
Version 1.0<br/>
Documentation file<br/>
Author/Developer: Lampros Chantzis<br/>
Date: 06/09/2019 

---------------------------------------------------------------------------------------------------------------------------------------
1. GENERAL<br/>
"Mint Room" is an audio plug-in developed with Matlab's App Designer. It uses an upmixing algorithm to create
virtual speakers with editable: 1) Gain level, 2) Angle and 3) Delay/Reverb effect to simulate distance to listener.
As an input it uses stereo wav files and it creates 2 upmixed channels containing the virtual speakers mixed. It can be only used
with headphones.

---------------------------------------------------------------------------------------------------------------------------------------
2. CONTENTS<br/>
In this repository there are: 
App Resources: A folder for all resources that app needs to run (icons, angle audio files, etc).
Screens: A folder that contains screenshots of the application's layout for a preview.
Test Audio Files: A folder containing wav files that have been used to test application's functionality.
Source Code: There is the .mlapp file that contains source code. It can be only be oppened with Matlab (2016 or later).

---------------------------------------------------------------------------------------------------------------------------------------
3. INSTALL<br/>
In order to install successfully Mint Room you must download the SADIE II Database (https://www.york.ac.uk/sadie-project/database.html)
(Subject D1, HRIR(wav)) and adjust the appropriate file paths inside the mlapp file. It is also necessary to add all folders to Matlab
path before you run the mlapp file.   

---------------------------------------------------------------------------------------------------------------------------------------
4. HOW TO USE<br/>
i) Import a file:
Click on the first button on File Control menu to load a wav file from your computer. The file's name will be displayed in the
bar below.<br/>
ii) Import previous settings:
Click on the second button on File Control menu to load a txt file that contains settings that were previously saved by user.
As soon as the file is loaded, settings will automatically be applied.<br/>
iii) Edit front speakers:
On the Settings panel, on the tab "Front Speakers" you can modify the parameters for the front pair of speakers. You can check
if you want to enable central speaker too. Note that on the monitor section you can see the angles you have set for the speakers.
The front speakers have not the add-delay feature.<br/>
iv) Edit rear speakers:
On the left of the Settings panel by clicking the different tabs you can move to different speakers parameters. You can add up
to 3 rear speakers. Initially the rear speakers are deactivated by default. You can turn them on by clicking on its respective
switch. Every speaker you activate it appears on the binaural mixer below by turning the channel's lamp to green. In the mixer 
you can edit its gain level.<br/>
v) Play a file:
After the file load and settings application you can hear your audio file by clicking on the play button on Control File section.
When you click play button while your file is playing it stops it and begin to play from start. With stop button you can stop the
file playing. It is recomended to stop any playing audio before you close the application. On the last channel of your binaural
mixer you can change the master volume of your output.<br/>
vi) Save your output:
If you want to save an audio file with all the changes you've adjusted via the app you can click on the third button on the Control
File section. The file will be saved as wav.<br/>
vii) Save your settings:
When you want to keep a set of settings for a future section with the app you can click on the fourth button (heart button) on top
of the screen and the settings will be saved as a txt file. Later you can load them as described above.<br/>
viii) Help:
For any further help try clicking the '?' button. 

---------------------------------------------------------------------------------------------------------------------------------------
5. LISCENCE AND CREDITS<br/>
"Mint Room" is a software developed for my thesis under the subject "Audio Signals Analysis for Listener's Envelopement 
Estimation". Its developement was supervised by Professor of Electrical & Computer Engineering, John Mourjopoulos and
Audiogroup of Patras University. Any suggestions or questions on this software are welcome.

Enjoy Mint Room<br/>
Thank you