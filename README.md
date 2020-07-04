# Mijia_Temp_API
Quick and Dirty REST API for the Mijia Temp Sensor. 
You can use this with things like this: https://github.com/lucacri/homebridge-http-temperature-humidity

### Pre-requisites
Raspberry Pi w bluetooth
Python3

```
sudo apt-get install libglib2.0-dev
sudo pip install bluepy
pip3 install flask
pip3 install btlewrap
pip3 install mitemp_bt
```

### Get the MAC of your Mijia (Look for something with the name MJ_HT_V1)
```sudo blescan```

### Clone Repo
```git clone https://github.com/Ferni7/Mijia_Temp_API.git ```

### Run the server
```
chmod +x bootstrap.sh
./bootstrap.sh
```

### Now query the API

```
curl http://<ip of rasp pi>:5000/device/<mac address of mijia>
curl http://192.168.0.234:5000/device/58:2d:34:xx:xx:xx
```
  
### Sample Output
```
{
    "battery": 14,
    "firmware": "00.00.68",
    "humidity": 49.2,
    "name": "MJ_HT_V1",
    "temperature": 22.2
}
```

