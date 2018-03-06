# Python-Laptop-Battery-Stats

This script gets some battery info from the laptop each minute and save it on a SQLite3 local DB. The idea is to, later on, generate a graph showing how the battery cycle count changes when the battery charges/discharges.

Information collected:

* Datetime
* Capacity (0%~100%)
* Cycle count
* Charging status (0/1 - True/False)
* Energy now (Wh)
* Energy full (Wh)

All the data is fetched from /sys/class/power_supply/BAT0 on Linux systems.

Example of sqlite3 DB after a few data collected:

```sqlite3
sqlite> select * from bat;
2018-03-06 12:45:26.601066|38|86|0|13.824|36.082
2018-03-06 12:50:26.806557|36|86|0|13.143|36.082
2018-03-06 12:55:27.070273|34|86|0|12.506|36.082
2018-03-06 13:00:27.317533|32|86|0|11.858|36.082
2018-03-06 13:05:27.518504|31|86|0|11.232|36.082
2018-03-06 13:10:27.745759|29|86|0|10.584|36.082
2018-03-06 13:15:27.995719|27|86|0|9.806|36.082
2018-03-06 13:20:28.470920|25|86|0|9.147|36.082
2018-03-06 13:25:28.735880|23|86|0|8.467|36.082
2018-03-06 13:30:28.996727|21|86|0|7.776|36.082
2018-03-06 13:35:29.323712|19|86|0|7.192|36.082
2018-03-06 13:40:29.575727|18|86|0|6.501|36.082
2018-03-06 13:45:29.905662|15|86|0|5.756|36.082
2018-03-06 14:49:14.980804|51|87|1|18.716|36.082

datetime|percentage|cyclecount|charging|wh|whmax
```
