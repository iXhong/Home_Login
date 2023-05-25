# NJtech Home Autologin
The Autologin is a python program to help you log into the NJtech_Home network

## Installation 
use pip to install the requirements in the requirements.txt

```commandline
pip install -r requirements.txt
```

## Usage
+ Use any text editor you like to edit the config.json which look like below
```json
{
  "username": "",
  "password": "",
  "ISP": ""
}
```
+ Take a look at your (or your roommate's) username and password and 
write them after the corresponding key.
+ If you are using *China Telecom* as your internet service provider, 
then fill the blank after **ISP** with **telecom**, otherwise use the **cmcc**
if your ISP is **China Mobile**
+ Change to the folder and run the program
```commandline
cd Autologin

python3 main.py
```
+ You will see some words like *Successful* if you logged in successfully.
+ Enjoy! 🥳

## Thanks
I learned a lot from other creative programmers, here I'd like to express my gratitude to you all.