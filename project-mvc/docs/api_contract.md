\# API Contract - User Profile



\*\*Endpoint:\*\* `/api/v1/profile`



\*\*Method:\*\* `GET`



\*\*Response Body (JSON):\*\*



```json

{

&#x20; "id": 1,

&#x20; "username": "mahasiswa\_sd",

&#x20; "email": "mhs@univ.ac.id",

&#x20; "avatar\_url": "https://image.com/avatar.png"

}

```

\---



\# API Contract - Login



\*\*Endpoint:\*\* `/api/v1/login`



\*\*Method:\*\* `POST`



\## Request Body (JSON)



```json

{

&#x20; "username": "mahasiswa\_sd",

&#x20; "password": "123456"

}

```



\## Response Body (JSON)



```json

{

&#x20; "status": "success",

&#x20; "message": "Login berhasil",

&#x20; "token": "abc123token"

}

```

