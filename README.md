# Raspberry Pi Simple Dashboard
Simple dashboard for monitoring Raspberry Pi storage, RAM and sensors

### Howto:
- Clone the repo to the Raspberry Pi 
```
git clone https://github.com/ajboloor/pi-simple-dashboard.git
```

- Install python SimpleHTTPServer
```
pip install SimpleHTTPServer --user
```

-  Find your Raspberry Pi's local ip (inet under eth0 or wlan0) Example: 192.168.1.29
```
ifconfig
```

- Start the server (optional port, default is 8000)
```
python -m SimpleHTTPServer 1234
```

- On your computer on the local server (same router connection), open a browser and go to ipaddress:port. Example:
```
192.168.1.29:1234
```

- You should see something like this:
![Dashboard Screenshot](/media/screenshot.PNG?raw=true "Dashboard Screenshot")
