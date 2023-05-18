# endpoints list


> note that we consider **example.com** as *BASE_URL* variable

> note to add `/` at end of each endpoint

> each endpoint can accept GET request.

---

### get all users and their details

```bash
$curl -X GET $BASE_URL/outline/users/list/

[
    {
        "id":1,
        "name":"test",
        "max_size":10000000000,
        "usage":0,
        "enabled":true,
        "key":"ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHM1JENzVmYmVlamxIMkhkZUxONjRk@irserver.ir:443/?outline=1#test",
        "birth_date":"2023-05-12",
        "exp_date":"2023-05-13",
        "pastebin_link":"https://paste.ubuntu.ir/gqwnx",
        "note":"test of mine",
        "outline_id":1,
        "server":2
    }
]
```

### get single user detail

```bash
$curl -X GET $BASE_URL/outline/users/list/{id}/
```


### add new user

> max_size is in GB. for example 1 is 1GB.

> server is the id of server

```bash
$curl -X POST $BASE_URL/outline/users/ -H 'Content-Type: application/json' -d '{"name": "test", "max_size": 1, "enabled": 1, "exp_date":"2023-05-13", "note":"test of mine", "server": 1}' 

{
    "ok":true,
    "name":"test",
    "max_size":1000000000,
    "enabled":true,
    "key":"ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp4M0d0MHFxRXE3TzgxRDIzdkc1akxm@irserver.ir:443/?outline=1#test",
    "exp_date":"2023-05-13",
    "paste_bin_link":"https://paste.ubuntu.ir/rgsvr",
    "note":"test of mine",
    "server":"eng self",
    "outline_id":"58"
}
```


### delete a user

> replace {id} with an user id, for example: 1

```bash
$curl -X DELETE $BASE_URL/outline/users/{id}/
```


### edit an user

```bash
$curl -X PUT $BASE_URL/outline/users/ -H 'Content-Type: application/json' -d '{"name": "test", "max_size": 1, "enabled": 1, "exp_date":"2023-05-13", "note":"test of mine", "server": 1}' 

{
    "id":4,
    "name":"test",
    "max_size":1,
    "enabled":true,
    "exp_date":"2023-05-13",
    "note":"test of mine",
    "server":1
}
```

---

### list servers

```bash
$curl -X GET $BASE_URL/outline/server/
```

### get servers

```bash
$curl -X GET $BASE_URL/outline/server/{id}/
```


### add new server

> note that the channel is channel id

```bash
$curl -X POST $BASE_URL/outline/server/ -H 'Content-Type: application/json' -d '{"name": "us server", "apiUrl": "https://usserver.ir:33397/cHwi7kl1J0IY0fdsfl_tUw", "wrapper_ip": "irserver.ir", "wrapper_port": "443", "channel": 1}'

{
    "id":3,
    "certSha256":"",
    "apiUrl":"https://usserver.ir:33397/cHwi7kl1J0IY0fdsfl_tUw","wrapper_ip":"irserver.ir",
    "wrapper_port":"443",
    "name":"us server",
    "channel":1
}
```


### delete a server

> note to replace `{id}` with server id

```bash
curl -X DELETE $BASE_URL/outline/server/{id}/
```


### edit server detail

```bash
$curl -X PUT $BASE_URL/outline/server/{id}/ -H 'Content-Type: application/json' -d '{"name":"test", "max_size":1, "enabled":true, "exp_date":"2023-05-13", "note":"test of mine", "server":1}' 

{
    "id":4,
    "name":"test",
    "max_size":1,
    "enabled":true,
    "exp_date":"2023-05-13",
    "note":"test of mine",
    "server":1
}
```

---

### list channels

```bash
$curl -X GET $BASE_URL/outline/cahnnel/
```


### get a channel

```bash
$curl -X GET $BASE_URL/outline/channel/{id}/
```


### add new channel

```bash
$curl -X POST $BASE_URL/outline/channel/ -H 'Content-Type: application/json' -d '{"username": "@channel_username or id", "name": "us channel"}'

{
    "username":"@channel_username or id",
    "name":"us channel"
}
```

---

### delete a channel

```bash
$curl -X DELETE $BASE_URL/outline/channel/{id}/
```

---

### edit a channel

```bash
$curl -X PUT $BASE_URL/outline/channel/{id}/ -H 'Content-Type: application/json' -d '{"username": "@channel_username or id", "name": "us channel"}'

'{
    "id": 1,
    "username": "@channel_username or id",
    "name": "us channel"
}
```


---

### batch user adding

> *prefix_name* is the name of keys which is beggin with

> *server* will indicate the server

> size is in GB and it indicate the max usage of each key

> count is the number of key that should create

> exp_date will set an expiration date for all keys

```bash
$curl -X POST $BASE_URL/outline/batch/ -H 'Content-Type: application/json' -d {"prefix_name": "eng1_", "server": 2, "size": 30, "count": 5, "note": "batch of 10", "exp_date": "2023-06-13"}

{
    "ok": true,
    "keys": [
        "ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpqUHczeHlXNW1nb0FJMEk2b3drelJa@irtest.ir:443/?outline=1#eng1_23",
        "ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTplNWtVdmNrbTc4VnlhaXJZbmtudWlr@irtest.ir:443/?outline=1#eng1_24",
        "ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTprbEhyNzVqWHJzam51Y0tOS08wS2Nm@irtest.ir:443/?outline=1#eng1_25",
        "ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpCTnZvUFpxaERlNWZuZ3NRbTJhTDFp@irtest.ir:443/?outline=1#eng1_26",
        "ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpUVHBnNFR5WnFPcmo5UkszbWs3MkRB@irtest.ir:443/?outline=1#eng1_27"
    ]
}
```