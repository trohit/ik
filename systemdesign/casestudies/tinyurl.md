# DAS to implement TinyURL
- Principles to use FTMLDS
- (F)unc req
  - a user can provide a url and get a shortened id
  - user can customize it while creating it 
  - user can set expiry date
  - user can force delete it
  - many shortids can map to the same URL
  - nice to be able to view stats on the shortid
  - Qs to ask
    - for generic B2C or should we design it so that many orgs can incorporate it 
- (T)ech Reqs
  - API to get a short id
    - input: URL + desired_shortcode + [optional_expiry_time]
- (M)icroservices
  - URL shortner uservice
  - URL decoder uservice
  - stats uservice    
  - For force del shortid req, system needs to be able to identify the user, so need a identification uservice | SSO
- Logical diagram


# References
