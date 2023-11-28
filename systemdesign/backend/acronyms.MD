# CAP, BASE, SOLID, KISS
The diagram below explains the common acronyms in system designs. 
 
## CAP 
CAP theorem states that any distributed data store can only provide two of the following three guarantees: 
1. Consistency - Every read receives the most recent write or an error. 
2. Availability - Every request receives a response. 
3. Partition tolerance - The system continues to operate in network faults. 
 
## BASE 
The ACID (Atomicity-Consistency-Isolation-Durability) model used in relational databases is too strict for NoSQL databases. The BASE principle offers more flexibility, choosing availability over consistency. It states that the states will eventually be consistent. 
 
## SOLID 
SOLID principle is quite famous in OOP. There are 5 components to it. 
 
1. SRP (Single Responsibility Principle)
2. OCP (Open Close Principle) 
3. LSP (Liskov Substitution Principle) 
4. ISP (Interface Segregation Principle) 
5. DIP (Dependency Inversion Principle) 
 
## KISS 
"Keep it simple, stupid!" is a design principle first noted by the U.S. Navy in 1960. It states that most systems work best if they are kept simple. 
[Sys design Acronyms](https://www.linkedin.com/posts/alexxubyte_cap-base-solid-kiss-what-do-these-acronyms-activity-7131682973212385280-vg6t)
