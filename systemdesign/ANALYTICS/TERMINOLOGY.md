# Some frequently used terms
- SEP: starburst enterprise platform
- Presto/ Trino/Starburst

# Data warehouse
- What: 
	- store data from multiple sources to act as a single src of truth. 
	- to be used for historical trend analysis and reporting
	- Not to be used by production apps
 - sometimes also called EDW (Enterprise Data Warehouse)
- Why
  - reduce stress on production system
  - optimized for red + sequential scans
  - integrate many sources of data
  - No IT involvement needed to create reports
  - One version of truth
  - Not affected by production system upgrades
  - Easy to create BI solns on top of it
  - can be used for anaytics without impacting production

# Data lakehouse
- What 
  - schema on read repo that holds vast amt of raw data in native format until its needed
- Why
  - inexpensive to store data in native format
  - store data with no modeling
  - 
 # Comparison
 ## Data Warehouse and Data Lakehouse
 - Warehouse uses a Top-Down approach (what do I want and how do I get it ?)
   - Top Down
     - Understand corporate strategy
     - gather reqs (biz + tech)
     - impl. data warehouse (infra + ETL + Dimension model + reporting)
     - Create data sourced + Do analytics + BI 
 - Lakehouse uses a Bottom-up approach (what do I have and what can I make of it ?)
   - Bottom up
     - Ingest all data regardless of reqs
     - Store all data in native format without any schema defn
     - Do analysis and analytics (batch / interactive/ realtime/ machine learning / Data warehouse)
  ## Data warehouse and EDW (Enterprise Data warehouse)
  - EDW is a single repo for all of the org's data providing holistic understanding, consolidated data and easier data compliance.
