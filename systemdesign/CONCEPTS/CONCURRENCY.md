# Concurrency types

# Transaction Isolation levels
- In [ACID](https://en.wikipedia.org/wiki/ACID) DBs, different types of [isolation](https://en.wikipedia.org/wiki/Isolation_%28database_systems%29) is allowed.
- Transaction is a logical set of ops to be executed on a DB, say txfer money from A to B
- A transaction can span many ops with multiple stmts.
- Isolation in ACID defines how a transaction is visible to other users.
- Ideally in a DB many ops happen concurrently but if isolation is maintained then the unintended effects of concurrency should not be visible at all.
- In a system that has less than ideal isolation, we may see the state of the system midway as if the trasaction was not fully complete. viz. money deducted from A but not credited to B.
- Types of [transaction isolation levels](https://www.geeksforgeeks.org/transaction-isolation-levels-dbms/):
  - Read Uncommitted: lowest level of isolation where a transaction can see uncommitted changes made by other transactions. This can result in dirty reads, non-repeatable reads, and phantom reads.
  - Read Committed: isolation level guarantees that any data read is committed at the moment it is read. Thus it does not allow dirty read. The transaction holds a read or write lock on the current row, and thus prevents other transactions from reading, updating, or deleting it.
  - Repeatable read : transaction holds read locks on all rows it references and writes locks on referenced rows for update and delete actions. Since other transactions cannot read, update or delete these rows, consequently it avoids non-repeatable read.
  - Serializable : highest isolation level. Defined to be an execution of operations in which concurrently executing transactions appears to be serially executing.

# Terms
## transaction isolation level metrics
- Dirty Reads
- Phantom reads
- Non repeatable reads
## other related terms 
- Write skew
- Lost Updates
- 
# References
- https://herbsutter.com/2013/02/11/atomic-weapons-the-c-memory-model-and-modern-hardware/
- https://www.youtube.com/watch?v=A8eCGOqgvH4
- Article explaining how to do banking tx + concurrency control in Redis: https://levelup.gitconnected.com/redis-introduction-caching-and-transactions-aa32d385aa2b
