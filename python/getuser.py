import requests
import json
import argparse

DEFAULT_NUM_OF_STUDENTS = 40
DEFAULT_SERVER_URL = "http://127.0.0.1"

username = "snopstlv"
password = "Student1!"

args = {}

def parse_args():
	global args
	arg_parser = argparse.ArgumentParser()
	arg_parser.add_argument("students_password", help="The basic password each student will have for login")
	arg_parser.add_argument("-n", "--num_of_students", help="The number of students to gather ", default=DEFAULT_NUM_OF_STUDENTS, type=int)
	arg_parser.add_argument("--server_url", help="The URL of the RAVELLO training Portal ", default=DEFAULT_SERVER_URL)
	arg_parser.add_argument("--base_student_name", help="the string used as the base for each student's name", default='snops')
	args = arg_parser.parse_args()

parse_args()

base_url = args.server_url + "/rest"
auth = (args.base_student_name, args.students_password)
headers = {"Content-Type": "application/json"}

for id in range(1,args.num_of_students):
    ###############
    ####
    ####   Get the Student ID
    ####
    ##############
    url = base_url +"/login"
    try:
        response = requests.request("POST", url, headers=headers, auth=(username+str(id), password))
        StudentID = response.json()['_id']
        # print "Student ID: ",StudentID
    except (RuntimeError, TypeError, NameError, KeyError, ValueError):
        print "Error on authenticating the student :",id

    url = base_url+"/students/"+StudentID
    try:
        response = requests.request("GET", url, headers=headers, auth=(username, password))
        CourseID = response.json()['userClass']['courseId']
        ClassID = response.json()['userClass']['_id']
        # print "Course ID: ",CourseID
        # print "Class ID: ",ClassID
    except (RuntimeError, TypeError, NameError, KeyError, ValueError):
        print "Error on listing the student details :",id


    url = base_url+"/students/"+StudentID+"/class/"+ClassID+"/apps"
    try:
        response = requests.request("GET", url, headers=headers, auth=(username, password))
        AppID = response.json()[0]['id']
        # print "Application ID: ",AppID
    except (RuntimeError, TypeError, NameError, KeyError, ValueError):
        print "Error on listing the student apps :",id


    url = base_url+"/students/"+StudentID+"/class/"+ClassID+"/apps/"+AppID
    try:
        response = requests.request("GET", url, headers=headers, auth=(username, password))
        vms = response.json()

        for vm in vms['vms']:
            #print vm['name']+","+vm['firstDns']['name']+","+vm['firstDns']['ip']
            print str(id)+","+StudentID+","+vm['name']+","+vm['firstDns']['name']+","+vm['firstDns']['ip']
    except (RuntimeError, TypeError, NameError, KeyError, ValueError):
        print "Error on listing the VMs for this student :",id
