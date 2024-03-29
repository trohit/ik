non-functional requirement (NFR) is a requirement that specifies how the system does it, as opposed to Function requirements that specify, what it does.
NFRs are divided into two main categories: 
- Execution qualities:observable during runtime (safety|security|usability)
- Evolution qualities:part of the system itself(Testability|Maintainability|Extensibility|Scalability)

![image](https://user-images.githubusercontent.com/466385/211130207-5d0bb4e9-8ae8-48c1-9f0c-a757be7e5664.png)

# Difference b/w Functional and NFR
- Functional defines what to do; NFR defines how to do it
- Analogy: 
  - Functional req maybe drive to Delhi, non functional req may be avoid tollways, drive defensively, keep under speed limit and don't overtake 
  - Functional req maybe prepare biryani; non functional req maybe don't use too much spice and make it presentable

# imp for interview
- scalability
- availability
- performance (latency) : p90


# Types of NFR
'taost' as in 'the ability of a system to'...
- (R)eliability	: taoast function and produce correct results, as intended. 
  - viz. produce the same results under same inputs and conditions every time.
- (C)onsistency	: taoast ensure that all subsystems show non-conflicting results.
  - viz. a PNR that shows a complimentary meal in the system also prints the same on the ticket  
- (A)vailability	: the %tage of time a system is up and operational.
- (M)aintaibility	: taoast be easily maintained for bug fixes, incremental changes and new features.
- (P)erformance	: taoast do useful work in a unit of time. usual metrics: QPS|RPS, Latency, Throughput
- (U)sability		: taoast allow its users to use it perform tasks safely|effectively|efficiently. In other words, a good UX has sensible defaults, is consistent in its behavior across modules, forgiving and easy to learn.
- (S)afety		: taoast to prevent, control, or mitigate unaaceptable consequences. viz. shutting down if system overheats, disallowing accidental removal of objects in-use.
- (S)ecurity		: taoast ensure networks and resources are safe from downtime and malicious intrusion.
  - viz. RBAC, SSO for ID server, Rate Limiting for Fair use (10 pastes/24hrs) and prevention of DDoS. 
- (S)calability	: taoast increase/decrease perf|cost in response to application|system demands.
- (I)teroperability:  taoast function as input or to be able to provide easily consumable output for other systems developed independently.
- (P)ortability	:   taoast function under different environments, versions of software or OS, without needing rework.

Still trying to come up with a backcronym | mnemonic
RCAMPUSS SIP
SIP SCRAMPUS

![image](https://user-images.githubusercontent.com/466385/211182787-bb7a5eed-2e82-4250-8fc0-309a13c8bc22.png)
![image](https://user-images.githubusercontent.com/466385/211182870-d5731116-3161-4165-ac3d-1b278b9c16b5.png)

# Other Considerations
hotspots | geolocation
