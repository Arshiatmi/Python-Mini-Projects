# Eye-Protector

This Repo Was Just A Personal Project That Woks Like 20/20 Rule ( In Every 20 Mnutes You Need To Rest 20 Seconds )

## How To Run ?

### Windows

You can press `win+R`, then type `shell:startup` then copy `dist/protector.exe` file there !

### Linux

**( Cronjob )** : copy python script to `/bin`, add a crontab job like `sudo crontab -e` and add `@reboot python3 /bin/protector.py &` at the end and save. Done !

**( Service )** : create file `/etc/systemd/system/protector.service` and write these in it :

```
[Unit]
Description=Protector

[Service]
ExecStart=/usr/bin/python3 /path/protector.py

[Install]
WantedBy=multi-user.target
```

After That Run it Like :

```
sudo systemctl start protector    # Runs the protector now
sudo systemctl enable protector   # Sets the protector to run every boot
```

**( rc.local )** : open `/etc/rc.local` File, Write These Lines At Bottom Of File :

```
cd /path/to/protector
/usr/bin/python3 protector.py &
```

if you want to make sure That rc.local works, add these lines too :

```
echo `date +%Y-%b-%d_%H:%M:%S` > /tmp/rc_local_time
```

Then You Can Check `/tmp/rc_local_time` To See If It works.
