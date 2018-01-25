PYTHON Code for RAVELLO REST API training Portal access

getuser.py
--------------
This code is used to get a list of students, with their VMs provisioned and deployed (name, Public FQDN, Public IP).
It is intended to be used with the student credentials (generic usernameXXXX - where XXXX will be replaced by the tool from 1 to the number of students +1)
and password is the generic password given to each student.


getuserjumprdp.py
--------------
This one is an evolution of the previous one, and using the same parameters, but creating an RDP file for every student, in the file system where you run the script

