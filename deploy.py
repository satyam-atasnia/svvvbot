from wit import Wit
import pymysql
from flask import Flask
from http.server import BaseHTTPRequestHandler,HTTPServer
import time
import psycopg2
from urllib.parse import unquote
access_token="RFXODTPVAHU625FDDOYNIF264AKMAU23"
client=Wit(access_token=access_token)
def get_hod(Branch):
	try:
		connection=psycopg2.connect(database='d7gakhjdhvrgbi', user = 'sriruvhddlclbx', password = 'b15969870b50e6e5ec412ca97fb5880ae1a5ea8a4c5c76f884bb83bd20535104', host = 'ec2-107-22-253-158.compute-1.amazonaws.com', port = '5432')
		cursor=connection.cursor()
		cursor.execute("select firstName,lastName from hod where branch=%(b)s",{'b':Branch})
		result=cursor.fetchall()
		print(result)
		if len(result)==0:
			return "SVVVBOT: no result found ask properly"
			print("SVVVBOT: no result found ask properly")
		else:
			x=result[0][0]+" "+result[0][1]
			return x
			print("SVVVBOT:",result[0][0],result[0][1])
	except:
		print("SVVVBOT: no result found")
def get_chairman(group):
	try:
		connection=psycopg2.connect(database='d7gakhjdhvrgbi', user = 'sriruvhddlclbx', password = 'b15969870b50e6e5ec412ca97fb5880ae1a5ea8a4c5c76f884bb83bd20535104', host = 'ec2-107-22-253-158.compute-1.amazonaws.com', port = '5432')
		cursor=connection.cursor()
		cursor.execute("select firstName,lastName from members where branch=%(g)s and designation='Chairman'",{'g':group})
		result=cursor.fetchall()
		print(result)
		if len(result)==0:
			return "SVVVBOT: no result found ask properly"
			print("SVVVBOT: no result found ask properly")
		else:
			x=result[0][0]+" "+result[0][1]
			return x
			print("SVVVBOT:",result[0][0],result[0][1])
	except:
		print("SVVVBOT: no result found")
def get_secretary(group):
	try:
		connection=psycopg2.connect(database='d7gakhjdhvrgbi', user = 'sriruvhddlclbx', password = 'b15969870b50e6e5ec412ca97fb5880ae1a5ea8a4c5c76f884bb83bd20535104', host = 'ec2-107-22-253-158.compute-1.amazonaws.com', port = '5432')
		cursor=connection.cursor()
		cursor.execute("select firstName,lastName from members where branch=%(g)s and designation='Secretary'",{'g':group})
		result=cursor.fetchall()
		if len(result)==0:
			return "SVVVBOT: no result found ask properly"
			print("SVVVBOT: no result found ask properly")
		else:
			x=result[0][0]+" "+result[0][1]
			return x
	except:
		print("SVVVBOT: no result found")
def get_info(firstName,lastName):
	try:
		connection=psycopg2.connect(database='d7gakhjdhvrgbi', user = 'sriruvhddlclbx', password = 'b15969870b50e6e5ec412ca97fb5880ae1a5ea8a4c5c76f884bb83bd20535104', host = 'ec2-107-22-253-158.compute-1.amazonaws.com', port = '5432')
		cursor=connection.cursor()		
		db=pymysql.connect("localhost","root","mundra","chatbot")
		cursor=db.cursor()
		cursor.execute("select associatedTables from main where firstName=%(fn)s and lastName=%(ln)s",{'fn':firstName,'ln':lastName})
		result=cursor.fetchall()
		if len(result)==0:
			return "SVVVBOT: no result found ask properly"
		else:
			print(result)
			cursor.execute("select designation,branch,gender from "+result[0][0]+" where firstName=%(fn)s and lastName=%(ln)s",{'fn':firstName,'ln':lastName})
			mainResult=cursor.fetchall()
			print("yash1")
			print(mainResult)
			if len(mainResult)==0:
				return "SVVVBOT: no result found ask properly"
				print("SVVVBOT: no result found ask properly")
			else:
				if mainResult[0][2]=='M':
					x="He is the "+mainResult[0][0]+" of "+mainResult[0][1]+" branch"
					return x
					print("SVVVBOT: He is the "+mainResult[0][0]+" of "+mainResult[0][1]+" branch")
				else: 
					x="She is the "+mainResult[0][0]+" of "+mainResult[0][1]+" branch"
					return x
	except:
		print("SVVVBOT: no result found")
def get_professor(branch):
	try:
		connection=psycopg2.connect(database='d7gakhjdhvrgbi', user = 'sriruvhddlclbx', password = 'b15969870b50e6e5ec412ca97fb5880ae1a5ea8a4c5c76f884bb83bd20535104', host = 'ec2-107-22-253-158.compute-1.amazonaws.com', port = '5432')
		cursor=connection.cursor()
		db=pymysql.connect("localhost","root","mundra","chatbot")
		cursor=db.cursor()
		cursor.execute("select firstName,lastName from associate_professor where branch=%(b)s",{'b':branch})
		result=cursor.fetchall()
		print(result)
		if len(result)==0:
			return "SVVVBOT: no result found ask properly"
			print("SVVVBOT: no result found ask properly")
		else:
			for x in result:
				print(x[0],x[1])
				
	except:
		print("SVVVBOT: no result found")
def get_professor_by_gender(branch,gender):
	try:
		connection=psycopg2.connect(database='d7gakhjdhvrgbi', user = 'sriruvhddlclbx', password = 'b15969870b50e6e5ec412ca97fb5880ae1a5ea8a4c5c76f884bb83bd20535104', host = 'ec2-107-22-253-158.compute-1.amazonaws.com', port = '5432')
		cursor=connection.cursor()
		db=pymysql.connect("localhost","root","mundra","chatbot")
		cursor=db.cursor()
		if gender=='male':
			cursor.execute("select firstName,lastName from associate_professor where branch=%(b)s and gender='M'",{'b':branch})
			result=cursor.fetchall()
			if len(result)==0:
				return "SVVVBOT: no result found ask properly"
				print("SVVVBOT: no result found ask properly")
			else:
				for x in result:
					print(x[0],x[1])
		elif gender=='female':
			cursor.execute("select firstName,lastName from associate_professor where branch=%(b)s and gender='F'",{'b':branch})
			result=cursor.fetchall()
			if len(result)==0:
				return "SVVVBOT: no result found ask properly"
				print("SVVVBOT: no result found ask properly")
			else:
				for x in result:
					print(x[0],x[1])	
	except:
		print("SVVVBOT: no result found")
def get_confirm_hod(firstName,lastName,type,branch):
	try:
		connection=psycopg2.connect(database='d7gakhjdhvrgbi', user = 'sriruvhddlclbx', password = 'b15969870b50e6e5ec412ca97fb5880ae1a5ea8a4c5c76f884bb83bd20535104', host = 'ec2-107-22-253-158.compute-1.amazonaws.com', port = '5432')
		cursor=connection.cursor()
		db=pymysql.connect("localhost","root","mundra","chatbot")
		cursor=db.cursor()
		cursor.execute("select associatedTables from main where firstName=%(fn)s and lastName=%(ln)s",{'fn':firstName,'ln':lastName})
		result=cursor.fetchall()
		print(result)
		cursor.execute("select designation,branch from "+result[0][0]+" where firstName=%(fn)s and lastName=%(ln)s",{'fn':firstName,'ln':lastName})
		mainResult=cursor.fetchall()
		print(mainResult)
		if len(mainResult)==0:
			return "SVVVBOT: no result found ask properly"
			print("SVVVBOT: no result found ask properly")
		else:
			if mainResult[0][0]==type and mainResult[0][1]==branch:
				print("SVVVBOT: Yes")
			else:
				print("SVVVBOT: No")
	except:
		print("SVVVBOT: no result found")
def get_confirm_professor(firstName,lastName,type,branch):
	try:
		connection=psycopg2.connect(database='d7gakhjdhvrgbi', user = 'sriruvhddlclbx', password = 'b15969870b50e6e5ec412ca97fb5880ae1a5ea8a4c5c76f884bb83bd20535104', host = 'ec2-107-22-253-158.compute-1.amazonaws.com', port = '5432')
		cursor=connection.cursor()
		db=pymysql.connect("localhost","root","mundra","chatbot")
		cursor=db.cursor()
		cursor.execute("select associatedTables from main where firstName=%(fn)s and lastName=%(ln)s",{'fn':firstName,'ln':lastName})
		result=cursor.fetchall()
		print(result)
		cursor.execute("select designation,branch from "+result[0][0]+" where firstName=%(fn)s and lastName=%(ln)s",{'fn':firstName,'ln':lastName})
		mainResult=cursor.fetchall()
		if len(mainResult)==0:
			return "SVVVBOT: no result found ask properly"
			print("SVVVBOT: no result found ask properly")
		else:
			if mainResult[0][0]==type and mainResult[0][1]==branch:
				print("SVVVBOT: Yes")
			else:
				print("SVVVBOT: No")
	except:
		print("SVVVBOT: no result found")
def get_confirm_degree(firstName,lastName,type):
	try:
		connection=psycopg2.connect(database='d7gakhjdhvrgbi', user = 'sriruvhddlclbx', password = 'b15969870b50e6e5ec412ca97fb5880ae1a5ea8a4c5c76f884bb83bd20535104', host = 'ec2-107-22-253-158.compute-1.amazonaws.com', port = '5432')
		cursor=connection.cursor()
		db=pymysql.connect("localhost","root","mundra","chatbot")
		cursor=db.cursor()
		cursor.execute("select associatedTables from main where firstName=%(fn)s and lastName=%(ln)s",{'fn':firstName,'ln':lastName})
		result=cursor.fetchall()
		print(result)
		cursor.execute("select Qualification from "+result[0][0]+" where firstName=%(fn)s and lastName=%(ln)s",{'fn':firstName,'ln':lastName})
		mainResult=cursor.fetchall()
		mainResult=mainResult[0]
		print(mainResult)
		s=''.join(mainResult)
		print(s)
		i=s.find(type)
		if i==-1:
			return "SVVVBOT: no result found ask properly"
			print("SVVVBOT: no result found ask properly")
		else:
			print("SVVVBOT: Yes")
	except:
		print("SVVVBOT: no result found")
def get_sports():
	try:
		connection=psycopg2.connect(database='d7gakhjdhvrgbi', user = 'sriruvhddlclbx', password = 'b15969870b50e6e5ec412ca97fb5880ae1a5ea8a4c5c76f884bb83bd20535104', host = 'ec2-107-22-253-158.compute-1.amazonaws.com', port = '5432')
		cursor=connection.cursor()
		cursor.execute("select name from sports")
		result=cursor.fetchall()
		if len(result)==0:
			return "SVVVBOT: no result found ask properly"
			print("SVVVBOT: no result found ask properly")
		else:
			r={}
			for x in result:
				r.add(x[0])
			return r
	except:
		print("SVVVBOT: no result found")
def get_indoor_games():
	try:
		connection=psycopg2.connect(database='d7gakhjdhvrgbi', user = 'sriruvhddlclbx', password = 'b15969870b50e6e5ec412ca97fb5880ae1a5ea8a4c5c76f884bb83bd20535104', host = 'ec2-107-22-253-158.compute-1.amazonaws.com', port = '5432')
		cursor=connection.cursor()
		db=pymysql.connect("localhost","root","mundra","chatbot")
		cursor=db.cursor()
		cursor.execute("select name from sports where type='Indoor'")
		result=cursor.fetchall()
		if len(result)==0:
			return "SVVVBOT: no result found ask properly"
			print("SVVVBOT: no result found ask properly")
		else:
			r={}
			for x in result:
				r.add(x[0])
			return r
	except:
		print("SVVVBOT: no result found")
def get_outdoor_games():
	try:
		connection=psycopg2.connect(database='d7gakhjdhvrgbi', user = 'sriruvhddlclbx', password = 'b15969870b50e6e5ec412ca97fb5880ae1a5ea8a4c5c76f884bb83bd20535104', host = 'ec2-107-22-253-158.compute-1.amazonaws.com', port = '5432')
		cursor=connection.cursor()
		db=pymysql.connect("localhost","root","mundra","chatbot")
		cursor=db.cursor()
		cursor.execute("select name from sports where type='Outdoor'")
		result=cursor.fetchall()
		if len(result)==0:
			return "SVVVBOT: no result found ask properly"
			print("SVVVBOT: no result found ask properly")
		else:
			r={}
			for x in result:
				r.add(x[0])
			return r

	except:
		print("SVVVBOT: no result found")
def get_group_chairman(group):
	try:
		connection=psycopg2.connect(database='d7gakhjdhvrgbi', user = 'sriruvhddlclbx', password = 'b15969870b50e6e5ec412ca97fb5880ae1a5ea8a4c5c76f884bb83bd20535104', host = 'ec2-107-22-253-158.compute-1.amazonaws.com', port = '5432')
		cursor=connection.cursor()
		cursor.execute("select firstName,lastName from members where institutes=%(g)s and designation='Group Chairman'",{'g':group})
		result=cursor.fetchall()
		print(result)
		if len(result)==0:
			return "SVVVBOT: no result found ask properly"
			print("SVVVBOT: no result found ask properly")
		else:
			print("SVVVBOT:",result[0][0],result[0][1])
	except:
		print("SVVVBOT: no result found")
def get_director(group):
	try:
		connection=psycopg2.connect(database='d7gakhjdhvrgbi', user = 'sriruvhddlclbx', password = 'b15969870b50e6e5ec412ca97fb5880ae1a5ea8a4c5c76f884bb83bd20535104', host = 'ec2-107-22-253-158.compute-1.amazonaws.com', port = '5432')
		cursor=connection.cursor()
		cursor.execute("select firstName,lastName from members where branch=%(g)s and designation='Director'",{'g':group})
		result=cursor.fetchall()
		print(result)
		if len(result)==0:
			return "SVVVBOT: no result found ask properly"
			print("SVVVBOT: no result found ask properly")
		else:
			s=result[0][0]+" "+result[0][1]
			print(s)
			return s
			print("SVVVBOT:",result[0][0],result[0][1])
	except:
		print("SVVVBOT: no result found")
def get_group_director_cdc():
	try:
		connection=psycopg2.connect(database='d7gakhjdhvrgbi', user = 'sriruvhddlclbx', password = 'b15969870b50e6e5ec412ca97fb5880ae1a5ea8a4c5c76f884bb83bd20535104', host = 'ec2-107-22-253-158.compute-1.amazonaws.com', port = '5432')
		cursor=connection.cursor()
		cursor.execute("select firstName,lastName from members where designation='Group Director CDC'")
		result=cursor.fetchall()
		print(result)
		if len(result)==0:
			print("SVVVBOT: no result found ask properly")
		else:
			print("SVVVBOT:",result[0][0],result[0][1])
	except:
		print("SVVVBOT: no result found")
def get_confirm_gender(firstName,lastName,gender):
	try:
		connection=psycopg2.connect(database='d7gakhjdhvrgbi', user = 'sriruvhddlclbx', password = 'b15969870b50e6e5ec412ca97fb5880ae1a5ea8a4c5c76f884bb83bd20535104', host = 'ec2-107-22-253-158.compute-1.amazonaws.com', port = '5432')
		cursor=connection.cursor()
		db=pymysql.connect("localhost","root","mundra","chatbot")
		cursor=db.cursor()
		cursor.execute("select associatedTables from main where firstName=%(fn)s and lastName=%(ln)s",{'fn':firstName,'ln':lastName})
		result=cursor.fetchall()
		print(result)
		cursor.execute("select gender from "+result[0][0]+" where firstName=%(fn)s and lastName=%(ln)s",{'fn':firstName,'ln':lastName})
		mainResult=cursor.fetchall()
		if len(mainResult)==0:
			return "SVVVBOT: no result found ask properly"
			print("SVVVBOT: no result found ask properly")
		else:
			if mainResult[0][0]==gender:
				print("SVVVBOT: Yes")
			else:
				print("SVVVBOT: No")
	except:
		print("SVVVBOT: no result found")
def get_address():
	try:
		connection=psycopg2.connect(database='d7gakhjdhvrgbi', user = 'sriruvhddlclbx', password = 'b15969870b50e6e5ec412ca97fb5880ae1a5ea8a4c5c76f884bb83bd20535104', host = 'ec2-107-22-253-158.compute-1.amazonaws.com', port = '5432')
		cursor=connection.cursor()
		cursor.execute("select address from about_aitr")
		result=cursor.fetchall()
		print(result)
		if len(result)==0:
			return "SVVVBOT: no result found ask properly"
			print("SVVVBOT: Ask properly")
		else:
			x=result[0][0]
			return x
			print("SVVVBOT :",result[0][0])
	except:
		print("SVVVBOT: no result found")
def get_contact_no():
	try:
		connection=psycopg2.connect(database='d7gakhjdhvrgbi', user = 'sriruvhddlclbx', password = 'b15969870b50e6e5ec412ca97fb5880ae1a5ea8a4c5c76f884bb83bd20535104', host = 'ec2-107-22-253-158.compute-1.amazonaws.com', port = '5432')
		cursor=connection.cursor()
		cursor.execute("select contact_no from about_aitr")
		result=cursor.fetchall()
		print(result[0][0])
		if len(result)==0:
			return "SVVVBOT: no result found ask properly"
			print("SVVVBOT: Ask properly")
		else:
			print("else me gaya")
			s=result[0][0]
			print(s)
			return s
			print("SVVVBOT :",result[0][0])
	except:
		print("SVVVBOT: no result found")
def get_affiliations():
	try:
		connection=psycopg2.connect(database='d7gakhjdhvrgbi', user = 'sriruvhddlclbx', password = 'b15969870b50e6e5ec412ca97fb5880ae1a5ea8a4c5c76f884bb83bd20535104', host = 'ec2-107-22-253-158.compute-1.amazonaws.com', port = '5432')
		cursor=connection.cursor()
		cursor.execute("select affiliations from about_aitr")
		result=cursor.fetchall()
		print(result)
		if len(result)==0:
			return "SVVVBOT: no result found ask properly"
			print("SVVVBOT: Ask properly")
		else:
			print("SVVVBOT :",result[0][0])
	except:
		print("SVVVBOT: no result found")
def get_timing_year(year):
	try:
		connection=psycopg2.connect(database='d7gakhjdhvrgbi', user = 'sriruvhddlclbx', password = 'b15969870b50e6e5ec412ca97fb5880ae1a5ea8a4c5c76f884bb83bd20535104', host = 'ec2-107-22-253-158.compute-1.amazonaws.com', port = '5432')
		cursor=connection.cursor()
		cursor.execute("select time from timing where year=%(y)s",{'y':year})
		result=cursor.fetchall()
		print(result)
		if len(result)==0:
			return "SVVVBOT: no result found ask properly"
			print("SVVVBOT: Ask properly")
		else:
			x=result[0][0]
			return x
			print("SVVVBOT :",result[0][0])
	except:
		print("SVVVBOT: no result found")
def get_timing_shift(year):
	try:
		connection=psycopg2.connect(database='d7gakhjdhvrgbi', user = 'sriruvhddlclbx', password = 'b15969870b50e6e5ec412ca97fb5880ae1a5ea8a4c5c76f884bb83bd20535104', host = 'ec2-107-22-253-158.compute-1.amazonaws.com', port = '5432')
		cursor=connection.cursor()
		cursor.execute("select time from timing where shift=%(y)s",{'y':year})
		result=cursor.fetchall()
		print(result)
		if len(result)==0:
			return "SVVVBOT: no result found ask properly"
			print("SVVVBOT: Ask properly")
		else:
			x=result[0][0]
			return x
			print("SVVVBOT :",result[0][0])
	except:
		print("SVVVBOT: no result found")
def give_facility(group):
	try:
		if group=='AITR':
			x="1.Well Equipped Laboratories."+"\n"+"2.Wi-Fi zone and Leased Line Internet."+"\n"+"3.E-Library with more than 16000 books and 52 National and International Journals."+"\n"+"4.On line lectures of National and International Experts through EDUSAT."
			return x
	except:
		print("SVVVBOT: no result found")
def get_info_acropolis(type):
	try:
		f=open("c:/chatbot/info/vision.txt")
		print(f.read())
	except:
		print("SVVVBOT: no result found")
def get_seats(branch):
	try:
		print(branch)
		connection=psycopg2.connect(database='d7gakhjdhvrgbi', user = 'sriruvhddlclbx', password = 'b15969870b50e6e5ec412ca97fb5880ae1a5ea8a4c5c76f884bb83bd20535104', host = 'ec2-107-22-253-158.compute-1.amazonaws.com', port = '5432')
		cursor=connection.cursor()
		db=pymysql.connect("localhost","root","mundra","chatbot")
		cursor=db.cursor()
		cursor.execute("select Intake,course_name from admission where specialization=%(b)s",{'b':branch})
		result=cursor.fetchall()
		print(result)
		if len(result)==0:
			print("SVVVBOT: Ask properly")
		else:
			for x in result:
				seats=x[0]
				course=x[1]
				print(x[0]," in ",x[1])
	except:
		print("SVVVBOT: no result found")
def get_eligibilty(branch):
	try:
		print(branch)
		connection=psycopg2.connect(database='d7gakhjdhvrgbi', user = 'sriruvhddlclbx', password = 'b15969870b50e6e5ec412ca97fb5880ae1a5ea8a4c5c76f884bb83bd20535104', host = 'ec2-107-22-253-158.compute-1.amazonaws.com', port = '5432')
		cursor=connection.cursor()
		db=pymysql.connect("localhost","root","mundra","chatbot")
		cursor=db.cursor()
		cursor.execute("select eligibility from admission where specialization=%(b)s",{'b':branch})
		result=cursor.fetchall()
		print(result)
		if len(result)==0:
			print("SVVVBOT: Ask properly")
		else:
			print("SVVVBOT:",result[0][0])
	except:
		print("SVVVBOT: no result found")
def get_library_timing():
	try:
		connection=psycopg2.connect(database='d7gakhjdhvrgbi', user = 'sriruvhddlclbx', password = 'b15969870b50e6e5ec412ca97fb5880ae1a5ea8a4c5c76f884bb83bd20535104', host = 'ec2-107-22-253-158.compute-1.amazonaws.com', port = '5432')
		cursor=connection.cursor()
		cursor.execute("select year,timing from library")
		result=cursor.fetchall()
		print(result)
		if len(result)==0:
			print("SVVVBOT: Ask properly")
		else:
			return result[0][0]+"year:"+result[0][1]+"\n"+result[1][0]+"year:"+result[1][1]+"\n"+result[2][0]+"year:"+result[2][1]+"\n"+result[3][0]+"year:"+result[3][1]+"\n"
	except:
		print("SVVVBOT: no result found")
def get_timing_year_library(year):
	try:
		connection=psycopg2.connect(database='d7gakhjdhvrgbi', user = 'sriruvhddlclbx', password = 'b15969870b50e6e5ec412ca97fb5880ae1a5ea8a4c5c76f884bb83bd20535104', host = 'ec2-107-22-253-158.compute-1.amazonaws.com', port = '5432')
		cursor=connection.cursor()
		cursor.execute("select timing from library where year=%(y)s",{'y':year})
		result=cursor.fetchall()
		if len(result)==0:
			print("Ask properly")
		else:
			return result[0][0]
	except:
		print("SVVVBOT: no result found")

	
def process(message):
	print("hi")
	print(message)
	resp=client.message(message)
	print(resp)
	if "bye" in message:
		print("SVVVBOT: bye")
	if not "intent" in resp['entities']:
		print("SVVVBOT: I am confused ask properly")
	elif resp['entities']['intent'][0]['value']=='greetings':
		return resp['_text']+" How can i help you"
		print("SVVVBOT: "+resp['_text']+" How can i help you")
	elif resp['entities']['intent'][0]['value']=='get_hod':
		if not "branch" in resp['entities']:
			return "SVVVBOT: no result found ask properly"
		else:
			branch=resp['entities']['branch'][0]['value']
			x=get_hod(branch)
			return x
	elif resp['entities']['intent'][0]['value']=='get_chairman':
		group=resp['entities']['group'][0]['value']
		x=get_chairman(group)
		return x
	elif resp['entities']['intent'][0]['value']=='get_secretary':
		group=resp['entities']['group'][0]['value']
		x=get_secretary(group)
		return x
	elif resp['entities']['intent'][0]['value']=='get_info':
		if not "firstName" in resp['entities']:
			return "SVVVBOT: no result found ask properly"
			print("SVVVBOT: please provide full name")
		else:
			firstName=resp['entities']['firstName'][0]['value']
		if not "lastName" in resp['entities']:
			return "SVVVBOT: no result found ask properly"
			print("SVVVBOT: please provide full name")
		else:
			lastName=resp['entities']['lastName'][0]['value']
		x=get_info(firstName,lastName)
		return x
	elif resp['entities']['intent'][0]['value']=='get_confirm_gender':
		firstName=resp['entities']['firstName'][0]['value']
		lastName=resp['entities']['lastName'][0]['value']
		gender=resp['entities']['gender'][0]['value']
		if gender=='male':
			get_confirm_gender(firstName,lastName,'M');
		if gender=='female':
			get_confirm_gender(firstName,lastName,'F');
	elif resp['entities']['intent'][0]['value']=='get_professor':
		branch=resp['entities']['branch'][0]['value']
		if resp['entities']['gender'][0]['value']=='male' or resp['entities']['gender'][0]['value']=='female':
			print("hi")
			get_professor_by_gender(branch,resp['entities']['gender'][0]['value'])
		else:
			get_professor(branch)
	elif resp['entities']['intent'][0]['value']=='get_confirm':
		firstName=resp['entities']['firstName'][0]['value']
		lastName=resp['entities']['lastName'][0]['value']
		type=resp['entities']['type'][0]['value']
		if type=='HOD':
			branch=resp['entities']['branch'][0]['value']
			get_confirm_hod(firstName,lastName,type,branch)
		if type=='professor':
			branch=resp['entities']['branch'][0]['value']
			get_confirm_professor(firstName,lastName,type,branch)
		if type=='BE':
			get_confirm_degree(firstName,lastName,type)
	elif resp['entities']['intent'][0]['value']=='get_sports':
		x=get_sports()
		print(x)
		return x	
	elif resp['entities']['intent'][0]['value']=='get_indoor_games':
		x=get_indoor_games()
		return x	
	elif resp['entities']['intent'][0]['value']=='get_outdoor_games':
		x=get_outdoor_games()
		return x
	elif resp['entities']['intent'][0]['value']=='get_group_chairman':
		group=resp['entities']['group'][0]['value']
		x=get_group_chairman(group)
		return x
	elif resp['entities']['intent'][0]['value']=='get_director':
		group=resp['entities']['group'][0]['value']
		x=get_director(group)
		return x
	elif resp['entities']['intent'][0]['value']=='get_group_director_cdc':
		x=get_group_director_cdc()
		return x
	elif resp['entities']['intent'][0]['value']=='get_address':
		x=get_address()
		return x
	elif resp['entities']['intent'][0]['value']=='get_contact_no':
		x=get_contact_no()
		return x
	elif resp['entities']['intent'][0]['value']=='get_affiliations':
		x=get_affiliations()
		return x
	elif resp['entities']['intent'][0]['value']=='get_timing_year':
		year=resp['entities']['year'][0]['value']
		x=get_timing_year(year)
		return x
	elif resp['entities']['intent'][0]['value']=='get_timing_shift':
		year=resp['entities']['year'][0]['value']
		x=get_timing_shift(year)
		return x
	elif resp['entities']['intent'][0]['value']=='give_facility':
		group=resp['entities']['group'][0]['value']
		x=give_facility(group)
		return x
	elif resp['entities']['intent'][0]['value']=='get_info_acropolis':
		type=resp['entities']['type'][0]['value']
		x=get_info_acropolis(type)
		return x
	elif resp['entities']['intent'][0]['value']=='get_seats':
		branch=resp['entities']['branch'][0]['value']
		x=get_seats(branch)
		return x
	elif resp['entities']['intent'][0]['value']=='get_eligibility':
		branch=resp['entities']['branch'][0]['value']
		x=get_eligibilty(branch)
		return x
	elif resp['entities']['intent'][0]['value']=='get_timing_library':
		x=get_library_timing()
		return x
	elif resp['entities']['intent'][0]['value']=='get_timing_year_library':
		year=resp['entities']['year'][0]['value']
		x=get_timing_year_library(year)
		return x
app = Flask(__name__)
@app.route('/',defaults={'path':''})
@app.route('/<path:path>')
def catch_all(path):
	print(path)
	if "bye" in path:
		return "Adios"
	elif "by" in path:
		return "Adios"
	else:
		x=process(path)
		print(x)
		x='\n'.join(x)
		print(x)
		return x

if __name__ == '__main__':
    app.run()		