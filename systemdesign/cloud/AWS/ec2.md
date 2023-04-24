# All Instances compared
https://instances.vantage.sh/

# types
- General purpose workloads : t : apps with moderate CPU usage with temp spikes
- Memory : m, r(ram), x,z(hi-mem)
- Compute : c
- Storage: igh (search optimised)
- Accelerated : a

# Notable Types and uses
## Gen purpose Instances
- A1 : arm-based offering of EC2 instance types – as compared to others that use either Intel or AMD processing. This type of instance is more suited for web servers and containerized microservices – along with applications that are run on open-source tools like Java or Python.
- M5 : latest generation of general-purpose instances that is powered by the Intel Xeon Platinum 8175 3.1Ghz processor. With their cloud computing power, M5 instances provide a balance of computing, memory, and networking power. This instance type is suited for small-to-midsize databases, data processing tasks, and as a backend server for enterprise applications like SAP or SharePoint.
- T3/ T3a : T3 and T3a are the respective general-purpose instance types powered with Intel and AMD processors. These instance types are a good fit if you are looking for a cheaper and less powerful option than the M5 fixed instance. They are commonly used for long-lasting application instances such as websites, web applications, and code repositories.

## Compute Type Instances
- C5/ C5n :  suitable for applications like online gaming, scientific modeling, media transcoding – which require raw computing power. C5 instances are executed on the Intel Xeon Platinum processor and have recorded a 25% improvement in speed as compared to the previous C4 instance generation. With the C5d instance type, you can physically connect the NVME-based SSD device to the host server to provide block-level storage for the entire instance lifetime.
- C6/ C6g : powered by the AWS Graviton2 series of processors and is suited for highly intensive and advanced applications such as high-performance computing, video encoding, ad serving, and distributed analytics. With the C6g instance type, you can get a 40% improvement in price-performance as compared to the C5 instance family.

## Mem type Instances
- R5/ R5a/ R5n : suited for workloads with high memory consumption such as high-performance databases, real-time Big data analytics, and large in-memory cache applications.
- R6g/ R6gd : Powered by the AWS Graviton2 processor, R6 instances are suited for high memory workloads such as open-source databases (example, MySQL) and in-memory caching (example, KeyDB).
- X1/ X1e : Powered by the Intel Xeon processor, the X1 family of memory-optimized instances are designed to provide high computational memory for memory-intensive applications like SAP HANA, Apache Spark, and for high-performance computing. Among all EC2 instances, the X1e instance type provides the highest memory-to-compute ratio at the lowest price calculated for each GiB of RAM.
- Hi mem Instance: provide the highest capacity of RAM – ranging from 6TB to 24TB in a single instance.  used to run high in-memory databases. only available on dedicated hosts – where you need to commit to running instances for a 3-year period.

## Acclerated Compute instances
- P3 / P2 / Inf1 / G3 / G4 / F1

## Storage optimized
- D2 | H1 | I3 | I3en | 

# EC2 Resv Types
![image](https://user-images.githubusercontent.com/466385/233819646-f008edf8-4e15-4f27-8408-436175da1a7e.png)

![image](https://user-images.githubusercontent.com/466385/233818798-3c13e734-5f2e-48e2-85b5-3ef48d0fc3b9.png)
