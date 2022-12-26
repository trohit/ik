non-functional requirement (NFR) is a requirement that specifies how the system does it, as opposed to Function requirements that specify, what it does.
NFRs are divided into two main categories: 
- Execution qualities:observable during runtime (safety|security|usability)
- Evolution qualities:part of the system itself(Testability|Maintainability|Extensibility|Scalability)

# Types of NFR
'taost' as in 'the ability of a system to'...
- (R)eliability	: taoast function and produce correct results, as intended.
- (C)onsistency	: taoast produce the same resuts under same inputs and conditions every time.
- (A)vailability	: the %tage of time a system is up and operational.
- (M)aintaibility	: taoast be easily maintained for bug fixes, incremental changes and new features.
- (P)erformance	: taoast do useful work in a unit of time. usual metrics: QPS|RPS, Latency, Throughput
- (U)sability		: taoast allow its users to use it perform tasks safely|effectively|efficiently. In other words, a good UX has sensible defaults, is consistent in its behavior across modules, forgiving and easy to learn.
- (S)afety		: taoast to prevent, control, or mitigate unaaceptable consequences. viz. shutting down if system overheats, disallowing accidental removal of objects in-use.
- (S)ecurity		: taoast ensure networks and resources are safe from downtime and malicious intrusion.
- (S)calability	: taoast increase/decrease perf|cost in response to application|system demands.
- (I)teroperability:  taoast function as input or to be able to provide easily consumable output for other systems developed independently.
- (P)ortability	:   taoast function under different environments, versions of software or OS, without needing rework.

Still trying to come up with a backcronym | mnemonic
SIP SCRAMPUS
