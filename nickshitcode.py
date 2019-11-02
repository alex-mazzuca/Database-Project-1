import sqlite3
import random
from date import datetime

#login is the uid of the current usr
#null value functionality may be lacking for variables ie cant/can be null
#missing sql statement in final function(payments) explanation on site
#dates are passed as strings to sql
#formatting in  general may need to be fixed
#virtually no testing has been done on code written
#ignore main it will be useless to you
def register_birth(cursor, conn, login):
	

	bregno = random.randint(100000,999999)
	
	row = None
	cursor.execute('select * from births b where b.regno = ?;', (bregno,))
	row = cursor.fetchone()
	
	if row != None:
		
		while row != None:

	                bregno = random.randint(100000,999999)

        		row = None
        		cursor.execute('select * from births b where b.regno = ?;', (bregno,))
        		row = cursor.fetchone()

	
	bfname = input('What is the first name of the baby')
	blname = input('What is the last name of the baby')

	bregdate = datetime.date(datetime.now())
	bregdate = bregdate.strftime('%Y-%m-%d')

	cursor.execute('select u.city from users u where u.uid = ?;', (login,))
	bregplace = cursor.fetchone()

	nbplace = input('What is the birth place')
	
	bgender = 'l'

	while bgender != 'M' or bgender != 'F':

		bgender = input('What is the gender of the child (M or F)?')
		bgender = bgender.upper()	

		
	p1Fname = input('What is the first name the Mother')
	p1Lname = input('What is the last name of the Mother')
	
	#check if parent 1 exists
	row = None 
	cursor.execute('select * from persons p where p.fname = ? and p.lname = ?;',(p1Fname,), (p1Lname,))
	row = cursor.fetchone()
	
	if row  == None:
		
		print('Mother info missing please enter the missing data')

		paFname = input('Please enter the first name of Mother')
		paLname = input('Please enter the last name of Mother')
		pabDate	= input('Please enter the birthdate of Mother')
		pabPlace = input('Please enter the birthplace of Mother')
		paAddress = input('Please enter the address of Mother')
		paPhone = input('Please enter the phone number of Mother')
		
		cursor.execute('insert into persons values (?, ?, ?, ?, ?, ?);', (paFname, paLname, pabDate, pabPlace, paAddress, paPhone))
		conn.commit()

	p2Fname = input('What is the first name of the Father')
	p2Lname = input('What is the last name of the Father')
	
	#check existence of Father
        cursor.execute('select * from persons p where p.fname = ? and p.lname = ?',(p2Fname,), (p2Lname,))
        row = cursor.fetchone()

        if row  == None:

                print('Father info missing please enter the missing data')

                paFname = input('Please enter the first name of Father')
                paLname = input('Please enter the last name of Father')
                pabDate = input('Please enter the birthdate of Father')
                pabPlace = input('Please enter the birthplace of Father')
                paAddress = input('Please enter the address of Father')
                paPhone = input('Please enter the phone number of Father')

                cursor.execute('insert into persons values (?, ?, ?, ?, ?, ?);', (paFname, paLname, pabDate, pabPlace, paAddress, paPhone))
                conn.commit()

	cursor.execute('insert into births values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);', (bregno, bfname, blname, bregdate, bregplace, bgender, p1Fname, p1Lname, p2Fname, p2Lname)) 
	conn.commit()

	#create the persons entry
	
	nbdate = input('Please enter the birthdate of the baby')
	
	cursor.execute('select p.address from persons p where p.fname = ? and p.lname = ?;', (p1Fname, p1Lname))
	baddress = cursor.fetchone()


	cursor.execute('select p.phone from persons p where p.fname = ? and p.lname = ?;', (p1Fname, p1Lname))
	bphone = cursor.fetchone()

	cursor.execute('insert into persons values (?, ?, ?, ?, ?, ?);', (bfname, blname, nbdate, nbplace, baddress, bphone))
	conn.commit()


def registerMarriage(cursor, conn):
	
	p1Fname = input('Please enter the first name of Partner 1')
	p1Lname = input('Please enter the last name of Partner 1')
	p2Fname = input('Please enter the first name of Partner 2')
	p2Lname = input('Please enter the last name of Partner 2')
	

	mregdate = datetime.date(datetime.now())
	mregdate = mregdate.strftime('%Y-%m-%d')

	mregno = random.randint(100000,999999)
	
	row = None
	cursor.execute('select * from marriages m where m.regno = ?;', (mregno,))
	row = cursor.fetchone()
	
	if row != None:
		
		while row != None:

	                mregno = random.randint(100000,999999)

        		row = None
        		cursor.execute('select * from marriages m where m.regno = ?;', (mregno,))
        		row = cursor.fetchone()

	row = None 
	cursor.execute('select * from persons p where p.fname = ? and p.lname = ?;',(p1Fname,), (p1Lname,))
	row = cursor.fetchone()
	
	if row  == None:
		
		print('Partner 1 info missing please enter the missing data')

		paFname = input('Please enter the first name of Partner 1')
		paLname = input('Please enter the last name of Partner 1')
		pabDate	= input('Please enter the birthdate of Partner 1')
		pabPlace = input('Please enter the birthplace of Partner 1')
		paAddress = input('Please enter the address of Partner 1')
		paPhone = input('Please enter the phone number of Partner 1')
		
		cursor.execute('insert into persons values (?, ?, ?, ?, ?, ?);', (paFname, paLname, pabDate, pabPlace, paAddress, paPhone))
		conn.commit()

	row = None 
	cursor.execute('select * from persons p where p.fname = ? and p.lname = ?;',(p2Fname,), (p2Lname,))
	row = cursor.fetchone()
	
	if row  == None:
		
		print('Partner 2 info missing please enter the missing data')

		paFname = input('Please enter the first name of Partner 2')
		paLname = input('Please enter the last name of Partner 2')
		pabDate	= input('Please enter the birthdate of Partner 2')
		pabPlace = input('Please enter the birthplace of Partner 2')
		paAddress = input('Please enter the address of Partner 2')
		paPhone = input('Please enter the phone number of Partner 2')
		
		cursor.execute('insert into persons values (?, ?, ?, ?, ?, ?);', (paFname, paLname, pabDate, pabPlace, paAddress, paPhone))
		conn.commit()

	cursor.execute('inset into marriages values (?, ?, ?, ?, ?, ?, ?);', (mregno, mregdate, mregplace, p1Fname, p1Lname, p2Fname, p2Lname))
	conn.commit()


def renew_vregistration(cursor, conn):

	vregno = input('Please enter the vehicles registration number')
	today = datetime.date(datetime.now())

	exp = None
	while exp == None:
		cursor.execute('select r.expiry from registrations r where r.regno = ?;', (vregno,))
		exp = cursor.fetchone()
		if exp = None:
			vregno = input('Please enter a valid registration number')

	currexp = exp.split('-')
	ndate = today
	ndate = ndate.replace(year = int(currexp[0]), month = currexp[1], day = currexp[2])
	if today >= ndate:

		ndate = ndate.replace(year = today.year + 1)

	else:
		
		ndate = ndate.replace(year = ndate.year + 1)

	ndate = ndate.strftime('%Y-%m-%d')

	cursor.execute('update registrastions set regdate = ? where regno = ?;', (ndate,), (vregno,))
	conn.commit()

def sellCar(cursor, conn):


	
	ofname = input('Please enter the first name of the old owner')
	olname = input('Please enter the last name of the old owner')
	nfname = input('Please enter the first name of the new owner')
	nlname = input('Please enter the last name of the new owner')
	cvin = input('Please enter the vin of the car')

	cursor.execute('select * from registrations where vin = ?;', (cvin,))
	check = cursor.fetchone()
	if check == None:

		print('Invalid vin')
		return 0
		
	cursor.execute('select fname from registrations where vin = ? order by regdate DESC limit 1;', (cvin,))
	cfname = cursor.fetchone()
	
	cursor.execute('select lname from registrations where vin = ? order by regdate DESC limit 1;', (cvin,))
	clname = cursor.fetchone()

	if cfname != ofname or clname != olname:

		print('Invalid seller')
		return 0
		
	
	


	nplate = input('Please enter the new plate number')

	oexpdate = datetime.date(datetime.now())
	nexpdate = oexpdate
	nexpdate = nexpdate.replace( year = nexpdate.year + 1)
	oexpdate = oexpdate.strftime('%Y-%m-%d')
	nexpdate = nexpdate.strftime('%Y-%m-%d')
	
	cursor.execute('select regno from registrations where vin = ? order by regdate DESC limit 1;', (cvin,))
	oregno = cursor.fetchone()

	cursor.execute('update registrations set expiry = ? where regno = ?;', (oexpdate,), (oregno,))
	
	nregno = random.randint(100000, 999999)
	cursor.execute('select * from registrations where regno = ?;', (nregno,))
	check2 = cursor.fetchone()
	
	if check2 != None:
		
		while check2 != None:
			nregno = random.randint(100000, 999999)
			cursor.execute('select * from registrations where regno = ?;', (nregno,))
			check2 = cusor.fetchone()
			
	
	cursor.execute('insert into registrations values (?, ?, ?, ?, ?, ?, ?);', (nregno, oexpdate, nexpdate, nplate, cvin, nfname, nlname))
	conn.commit() 


def payment(cursor, conn):

	ptno = input('Please enter the ticket number for the ticket that is being paid')
	
	cursor.execute('select fine from tickets where tno = ?;', (ptno,))
	tfine = cursor.fetchone()

	if tfine == None:

		print('Invalid ticket number')
		return 0	
	
	tfine = float(tfine)
	
	pamount = input('Please enter the ticket amount')

	cursor.execute()#missing sql statement should collect a sum of payments with ptno my brain died and couldn't get it working :(
	psum = cursor.fetchone()

	if (pamount + psum) > tfine:
	
		pmax = tfine - psum
		print('Invalid payment:too high max payment for this fine is ' + pmax)
		return 0

	pdate = datetime.date(datetime.now())
	pdate = pdate.strftime('%Y-%m-%d')
	
	cursor.execute('insert into payments values (?, ?, ?,);', (ptno, pdate, pamount))
	conn.commit()

main():

	
	#dbpath code needs to be edited to accomadate command line arg database code will not function on your computer as it is now
	dbpath = "./a2.db"
	conn = sqlite3.connect(dbpath)
	cursor = conn.cursor()
	cursor.execute(' PRAGMA foreign_keys=ON; ')
	t = 'Goldi'
	cursor.execute('select * from persons p where p.fname = ?;', (t,))
	row = cursor.fetchone()
	
	

main()

