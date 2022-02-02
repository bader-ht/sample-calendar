# Running the project

Clone the repository and navigate to its root directory.

Install the requirements file:
```shell
pip install -r  web/requirements.txt
```

If you are starting without a database, then run:

```shell
web/manage.py migrate 
```

To run the project, run:
```shell
web/manage.py runserver 0.0.0.0:8000
```

# Using the API

(For convenience, all the requests were created on [Insomnia](https://insomnia.rest/), with configuration files included in this repository in .json and .har file formats.)

To access logged in APIs, the user must first login with a username and password via the login endoint, which will return a JSON Web Token (JWT)

```
{
	"username":"user1",
	"password":"calendar2021"
}
```

Here's a sample response from a sucessful login:
```
{
	"access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQzODQxMjg5LCJpYXQiOjE2NDM4NDA5ODksImp0aSI6IjVmMWYxMmY0NjdhNjQ0NTliNDUzZDM2NzY4MDJiZmUwIiwidXNlcl9pZCI6Mn0.VYR-M9uTKwdjbtsYfpF_wi2pCtbVMF15Liry3htuY90",
	"refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY0MzkyNzM4OSwiaWF0IjoxNjQzODQwOTg5LCJqdGkiOiIxOGJiNzZkZTM4NjQ0NmM2OGIwZTc2NmYyNGJhYTljMCIsInVzZXJfaWQiOjJ9.FMLuKmiGAStZuGPbquvt0XkzAyMBEP65orCGbsGI9v0",
	"user": {
		"pk": 2,
		"username": "user1",
		"email": "",
		"first_name": "",
		"last_name": ""
	}
}
```

The access token must be included in the header of any request in order for the request to be considered as authenticated.
The access token must be inlucded with a prefix of "Bearer", as shown in the example below.  
```
"Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQzODQxMjg5LCJpYXQiOjE2NDM4NDA5ODksImp0aSI6IjVmMWYxMmY0NjdhNjQ0NTliNDUzZDM2NzY4MDJiZmUwIiwidXNlcl9pZCI6Mn0.VYR-M9uTKwdjbtsYfpF_wi2pCtbVMF15Liry3htuY90"
```


The base of the API is /api/, making the full url locally accessible at http://127.0.0.1:8000/api/

### timings list:
http://127.0.0.1:8000/api/calendar/list/

method: GET

### Calendar / timing creation:
To add to the user's calendar, they simply need to log in, then, send an authenticated request with start time, end time, and interval to the following URL, along with the correct authentication token (JWT):

http://127.0.0.1:8000/api/calendar/create/

method: POST

Here is a sample payload
```
{
	"start_date": "21-10-2021 10:00:00:+03",
	"end_date": "21-10-2021 13:00:00:+03",
	"interval":45
}
```


##  EDIT/Update timing:
http://127.0.0.1:8000/api/calendar/edit/<id>/

This endpoint allows the retreival and update of ones own timings. The id must be inlcuded in the URL to GET or modify the record, along with the correct authentication token (JWT).

methods: GET, PUT, PATCH

```
{
	"start_date": "21-10-2021 10:16:00:+03",
	"end_date": "21-10-2021 10:24:00:+03",
	"interval":30
}
```

### Delete  timing:
This endpoint enables the deletion of ones own timings.
The id of the timing (from the create or list endpoints) must be included in the url, along with the correct authentication token (JWT).

http://127.0.0.1:8000/api/calendar/delete/<id>/

method: DELETE


## Reserve a slot on existing timing:
To reserve a slot with a specific user, use the reserve endpoint, where an email, full name, start time, and calendar ID must be provided. The calendar ID will be used to determine the user and the interval for the reservation and apply them automatically.

http://127.0.0.1:8000/api/reserve/
```
{
	"email":"alsayegh85@gmail.com",
	"full_name":"bader alsayegh",
	"start_date": "02-02-2022 09:55:00:+03",
	"calendar":"31"
}	
```