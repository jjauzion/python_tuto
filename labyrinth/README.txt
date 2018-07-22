*Python 3.6 or higher recommanded

--> START SERVER (from shell):
1- Go to the project root folder (e.g. folder containing src/ test/ and roboc.py)
2- Type in the shell: "python roboc_server.py"
3- Follow the instruction on the screen

--> START SERVER (from windows):
1- Double click on robot_server.py file 

/!\ Important note: in the current version the server can only be properly closed by the client with '#exit' command

--> START CLIENT (from shell):
1- Go to the project root folder (e.g. folder containing src/ test/ and roboc.py)
2- Type in the shell: "python roboc_client.py"
   If server is not yet online or full, client will wait 30sec for the serveur before timeout
3- Follow the instruction on the screen

--> START CLIENT (from windows):
1- Double click on robot_client.py file 

You can connect up to 5 players on the server

--> Unit test:
From shell:
1- Go to the project root folder (e.g. folder containing src/ test/ and roboc.py)
2- Type in the shell: "python -m unittest -v"
