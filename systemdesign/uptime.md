![image](https://user-images.githubusercontent.com/466385/234746032-5558a52a-0cb3-47d4-b7a8-e5921bb91b9e.png)
```
three 9's: ~9hrs
 four 9's: ~1hr
 five 9's: ~5mins <<<<<<<<<< just remember five nines means max mins downtime
```

# What is High Availability?
- A  measure of reliability and is the expected amount of time, measured as a percent, that a service or equipment is available to serve the user/application.
- The 99.999 percent (5-nines) availability standard specifies 24/7 service with a maximum of five minutes of downtime in a year. 
  - A typical desktop without 5-nines reliability may tolerate nine hours per year of unavailability,
  - but a carrier-class switch or server would require support for 5-nines availability.
  - Generally, service availability depends heavily on the fault tolerance of the system, including hardware redundancy.
- 6 nines availability means upto a max of 31.5 secs downtime / yr
- https://en.wikipedia.org/wiki/Uptime


# Mnemonic
```
For derivation
24*30 = 750 hrs a month
in a year = (750 * 10) + (750 * 2) hrs a year
          = 7500 + 1500
          = 9000 hrs a yr
          
so
99%uptime = 1% downtime = 1%(9000) = 90 hrs = 3-4 days ( 72-96 hrs)
```
a common year(unlike a leap year) is 365 days (8760 hours, 525600 minutes or 31536000 seconds


Uptime
Availability Table - Cheat sheet
What you need to remember
```
Availability level	Downtime per year
90% ("one nine")	36.5 days
95%	18.25 days
99% ("two-nines")	3.65 days
99.50%	1.83 days
99.9%("three nines")	8.76 hours
99.95%	4.38 hours
99.99%("four nines")	52.6 minutes
99.999%("five nines")	5.26 minutes
99.9999%("six nines")	31.5 secs
99.99999%("7 nines")	3.16 secs
99.999999%("8 9s")	315 ms
99.9999999%("9 9s")	31.5 ms
```
https://gist.githubusercontent.com/dastergon/07751e9d3117ae0ead808cd39d4f92d1/raw/4515c0db813d45abf0ba2770123c26c311393ef7/availability-cheatsheet.md
