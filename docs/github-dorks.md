---
title: Github dorks
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - reconnaissance
  - scanning
  - osint 
  - dorking
---


# Github Dorks

[Go to github](https://github.com).


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



