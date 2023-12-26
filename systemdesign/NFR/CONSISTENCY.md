# Consistency

- Weak
  - After a write, reads may or may not see it
  - Best effort only
  - "Message in a bottle"   
- Eventual
  - After a write, reads will _eventually_ see it.
  - DNS, SMTP, snail mail
  - search engine indexing, s3 
- Strong
  - After a write, reads _will_ see it.
  - FIlesystems, RDBMS
 
# Related
- https://snarfed.org/transactions_across_datacenters_io.html
