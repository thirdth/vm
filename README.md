# Swiss Pairings Tournament database
Source code for a tournament results database utilizing the Swiss
Pairing system for **Full Stack Web Developer Nanodegree Program**
from **Udacity**

# Usage Instructions
1. This program is intended to be run using a localized webserver.
2. You will need to set-up a virtual machine like Virtual Box. Instructions
for set-up can be found [here](https://www.virtualbox.org/manual/https://www.vagrantup.com/intro/getting-started/ch01.html)
3. You will also need to set up Vagrant in order to utilize Virtual
Box as a webserver. Instructions and download can be found [here](https://www.vagrantup.com/intro/getting-started/)
4. Prior to setting up Vagrant, download the files for the program onto your local machine.
5. Navigate to the folder containing these files and install Vagrant in that directory in order to share those files with both your local machine and the virtual machine. Once shared, Vagrant will keep them both up-to-date, so you can edit on your local machine with your favorite text editor.
6. Once you have set-up Vagrant and Virtual Box you can edit the programs to your liking. You can either edit tournament_test.py to run your tournament code, or you can create another python program and import tournament.py to take advantage of its functions.
7. Once you have edited your code sufficiently, you will want to run it through the virtualized webserver.
8. Navigate to the local folder that you set up Vagrant in, and run vagrant.ssh.
9. Navigate to your Tournament folder in the virtual machine through the Vagrant directory.
10. Run `python [your_file.py]` in order to see the results.
