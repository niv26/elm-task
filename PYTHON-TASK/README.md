# Home assignment 

## Implementation notes 
The idea of the program was to read the csv files on startup , create a dicitonary , run the security check using the virus total api (vt-py) with timestamp .
- If the program was supposed to run as an agent on ec2 server for example , the dicuonary could live in the server memory and the time checks would be from it .
-   If the program was intended to ran as ad-hoc pocess , using lambda for example the time checks would directly from the database or some cache layer should the  request interval or the amount od data would be high. 

The data base will store all of the reads from the api , with the url of the site and timestamp of the request time. 

When the final results would be requested , 
it can be easily accessible with sql query 
"SELECT url , .... , MAX(request_timestamp) GROUP BY .."

[git link](https://github.com/niv26/elm-task/tree/main/PYTHON-TASK)