Design a build & deploy system on the scale of a large org like Google.

# FR:
- about 10k builds a day, each build takes about 10 mins to complete, build image about 5MB..5GB
  - Code is a mix of all languages both scripted and compiled.
- Resultant build image needs to be deployed to over 1M VM machines that can be spun up on-demand, deploy needs to complete within 30 mins
- Dev needs insights into build and deploy logs and a progress status.

# Non-functional Reqs
- High Scale
- Low Latency
- High Availability *

# Assumptions
- Jobs Info & Logs can be perodically purged (say every 90 days)

# APIs
## public endpoints

## pvt endpoints

# Design
![image](https://github.com/trohit/ik/assets/466385/a1979445-ada2-4804-94d8-333df5f04d0c)

# Qs

# Wrap-up
