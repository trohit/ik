Design a build & deploy system on the scale of a large org like Google.

# Func Reqs & Clarification:
- about 150k devs & 50k builds/day, avg_build_time: 10 mins, build image 5MB..5GB
  - Code is a mix of all languages both scripted and compiled. Any number of languages.
- Resultant build image needs to be deployed to over 1M VM machines that can be spun up on-demand, deploy within t+30 mins
- Build(10mins) + Deploy(30mins)last machine to deploy
  - usecase like search: 1M machines geo distrib
  - deploy time not significant 5 mins
- Dev needs insights into build and deploy logs and a progress status.
  
# Non-Functional Reqs 
- Scalable
- Batch based system
- Build logs should be viewable and state of the build; same for deploy
- Highly available : five 9s (5 mins downtime/yr)

# HLD

# BOTE
50x10^3 / 10^5 : QPS: 1 

# Non-functional Reqs
- High Scale
- High Availability *
- Low Latency

# Assumptions
- Jobs Info & Logs can be perodically purged (say every 90 days)
- Some rate limiting needed so as prevent single dev from swaping the system
- Some SSO like LDAP / SAML to identify user in org

# APIs
## public endpoints : Will use REST
- POST /build_and_deploy
  - param: build path and cmd/s to run
  - response: 201 accepted
  - json: build job id, build logs, deploy logs, url

- GET /get_status
  - response: build success| in_progress| failed


## pvt endpoints: Can use gRPC + protobufs / Apache Thrift 

# Design
![image](https://github.com/trohit/ik/assets/466385/a1979445-ada2-4804-94d8-333df5f04d0c)

# Qs
## How will you ensure that the 1M-50M machines can access the build image and deploy within 30 mins? 

# Wrap-up
