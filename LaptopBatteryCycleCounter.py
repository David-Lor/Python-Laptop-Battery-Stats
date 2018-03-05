
import subprocess
import sqlite3
import datetime
import time
import atexit

db = sqlite3.connect("LaptopBatteryCycleCounter.sqlite")
dbc = db.cursor()
dbc.execute("""CREATE TABLE IF NOT EXISTS bat
	(
		datetime TEXT PRIMARY KEY,
		capacity UNSIGNED INT NOT NULL,
		cyclecount UNSIGNED INT NOT NULL,
		charging UNSIGNED INT NOT NULL,
		energynow UNSIGNED INT NOT NULL,
		energyfull UNSIGNED INT NOT NULL
	)
""")
db.commit()

### GETTERS FOR BATTERY INFO

def get(attribute, toInt=True):
	out = subprocess.check_output("cat /sys/class/power_supply/BAT0/{}".format(attribute).split())
	if toInt:
		return int(out)
	return out

def get_capacity():
	#Actual battery level (percentage, 0~100)
	return get("capacity")

def get_cyclecount():
	#Battery cycle count
	return get("cycle_count")

def get_charging():
	#Charging status (True=charging, False=discharging)
	#TODO more status (charging, charged, discharging)
	status = get("status", False)
	if status == "Charging":
		return True
	return False

def get_energynow():
	#Energy now (Wh)
	return get("energy_now")/1000000

def get_energyfull():
	#Energy when battery is full (Wh)
	return get("energy_full")/1000000

### END OF GETTERS FOR BATTERY INFO

def getandsave():
	#Get all the battery data and save it on DB
	dbc.execute(
		"INSERT INTO bat VALUES (?,?,?,?,?,?)",
		(
			str(datetime.datetime.now()),
			get_capacity(),
			get_cyclecount(),
			int(get_charging()),
			get_energynow(),
			get_energyfull()
		)
	)
	db.commit()

@atexit.register
def atexit_f():
	dbc.close()
	db.commit()
	db.close()

if __name__ == "__main__":
	while True:
		try:
			getandsave()
			time.sleep(60)
		except KeyboardInterrupt:
			break
