*Python 3.6 or higher recommanded

/!\ TRIAL VERSION, ONLY WORKS ON LOCAL NETWORK /!\
/!\ ONLY TESTED ON MAC OS /!\

Start server :
1- Go to the project root folder (e.g. folder containing src/ test/ and roboc.py)
2- Type in the shell: "python roboc_server.py"
3- Follow the instruction
/!\ Important note: in the current version the server can only be properly closed by the client with '#exit' command

Start client :
1- Go to the project root folder (e.g. folder containing src/ test/ and roboc.py)
2- Type in the shell: "python roboc_client.py"
   If server is not yet online or full, client will wait 30sec for the serveur before timeout
3- Follow the instruction

You can connect up to 5 players on the server

Unit test:
1- Go to the project root folder (e.g. folder containing src/ test/ and roboc.py)
2- Type in the shell: "python -m unittest -v"
