---
title: Conduct search engine discovery reconnaissance for information leakage - OWASP Web Security Testing Guide 
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - web pentesting
  - reconnaissance
  - WSTG-INFO-01
  - dorkings
---



# Conduct search engine discovery reconnaissance for information leakage

!!! quote ""
	[OWASP Web Security Testing Guide 4.2](index.md) > 1. Information Gathering > 1.1. Conduct search engine discovery reconnaissance for information leakage

|ID|Link to Hackinglife|Link to OWASP|Objectives|
|:---|:---|:---|:---|
|1.1|[WSTG-INFO-01](WSTG-INFO-01.md)|[Conduct Search Engine Discovery Reconnaissance for Information Leakage](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/01-Conduct_Search_Engine_Discovery_Reconnaissance_for_Information_Leakage)|- Identify what sensitive design and configuration information of the application, system, or organization is exposed directly (on the organization's website) or indirectly (via third-party services).|

This is merely passive reconnaissance.



## Use multiple search engines

- Baidu
- Bing
- binsearch.info
- Common crawl
- Duckduckgo
- Wayback machine
- Startpage (based on google but trackers and logs)
- [Shodan](../shodan.md).



## Use operators


### Google Dorks

[More about google dorks](../google-dorks.md).


| Google Dorking Query | Expected results |
|------------------------------- | ---------------------- |
| intitle:"api" site: "example.com" |  Finds all publicly available API related content in a given hostname. Another cool example for API versions:  inurl:"/api/v1" site: "example.com" |
| intitle:"json" site: "example.com" |  Many APIs use json, so this might be a cool filter |
| inurl:"/wp-son/wp/v2/users" |  Finds all publicly available WordPress API user directories. |
| intitle:"index.of" intext:"api.txt" | Finds publicly available API key files. |
|  inurl:"/api/v1" intext:"index of /" | Finds potentially interesting API directories. |
| intitle:"index of" api_key OR "api key" OR apiKey -pool | This is one of my favorite queries. It lists potentially exposed API keys. |


Use cache operator

```
cache:target.com
```


### Github

[More Githun Dorking](../github-dorks.md).


|  Github Dowking Query |  Expected results |
| --------------------- | ----------------- |
| applicationName api key | After getting results, filter by issue and you may find some api keys. It's common to leave api keys exposed when rebasing a git repo, for instance |
|  api_key | -  |
|  authorization_bearer | -   |
|  oauth |  -  |
|  auth |  -  |
|  authentication |  -  |
|  client_secret |  -  |
|  api_token |  -  |
|  client_id  |  -  |
|  OTP |  -  |
|  HOMEBREW_GITHUB_API_TOKEN | -   |
|  SF_USERNAME |  -  |
|  HEROKU_API_KEY  |  -  |
|  JEKYLL_GITHUB_TOKEN | -   |
|  api.forecast.io  | -   |
|  password |  -  |
|  user_password | -   |
|  user_pass |  -  |
|  passcode  |  -  |
|  client_secret | -   |
|  secret |  -  |
|  password hash |  -  |
|  user auth | -   |
| extension: json nasa | Results show some extensions that include json, so they might be API related |
| shodan_api_key | Results show shodan api keys |
| "authorization: Bearer" | This search reveal some authorization token. |
| filename: swagger.json | Go to Code tab and you will have the swagger file. |



### Shodan

[Go to shodan](https://www.shodan.io/).

|  Shodan Dowking Query |  Expected results |
| --------------------- | ----------------- |
|  "content-type: application/json" |  This type of content is usually related to APIs |
|  "wp-json" |  If you are using wordpress |



### WaybackMachine with WayBackUrls

[waybackurls](https://github.com/tomnomnom/waybackurls) inspects back URLs saved by [Wayback Machine](http://web.archive.org)  and look for specific keywords.  Installation:

```shell-session
go install github.com/tomnomnom/waybackurls@latest
```

Basic usage:

```shell-session
waybackurls -dates https://example.com > waybackurls.txt

cat waybackurls.txt
```


Dork for API endpoints discovery:

|  Waybackmachine Dowking Query |  Expected results |
| ----------------------------- | ----------------- |
| Path to a API |  We are trying to see is there is a recorded history of the API. It may provide us with endpoints that used to exist but allegedly not anymore. |

