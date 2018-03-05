# Python-Laptop-Battery-Stats

This script gets some battery info from the laptop each minute and save it on a SQLite3 local DB. The idea is to, later on, generate a graph showing how the battery cycle count changes when the battery charges/discharges.

Information recollected:

* Datetime
* Capacity (0%~100%)
* Cycle count
* Charging status (0/1 - True/False)
* Energy now (Wh)
* Energy full (Wh)

All the data is fetched from /sys/class/power_supply/BAT0 on Linux systems.
