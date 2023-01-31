---
title: Endpoint analysis
author: amandaguglieri
draft: false
TableOfContents: true
---

# Endpoint analysis

If an API is not documented or the documentation is unavailable to you, then you will need to build out your own collection of requests. Two different methods:

1. Build a collection in Postman
2. Build out an API specification using mitmproxy2swagger.

## Build a collection in Postman

In the instance where there is no documentation and no specification file, you will have to reverse-engineer the API based on your interactions with it. Mapping an API with several endpoints and a few methods can quickly grow into quite a large attack surface.  There are two ways to manually reverse engineer an API with Postman. 

- One way is by constructing each request. 
- The other way is to proxy web traffic through Postman, then use it to capture a stream of requests. This process makes it much easier to construct requests within Postman, but you’ll have to remove or ignore unrelated requests. 

### Steps

**1.** Start crapi applicationi

```bash
cd ~/lab/crapi
sudo docker-compose start
```

**2.** Open the browser, and select "postman 5555" in your Foxyproxy addon to proxy the traffic. 

**3.** Open your local crapi application in the browser: http://localhost:8888

**4.** Run postman from the command line:

```bash
postman
```

**5.** Once postman is open, press on "Capture traffic link" (at the bottom right of the application). Set up the capture, and make sure that proxy is enabled in the application. A useful shortcut to go to Settings is CTRL-, (comma).

**6.** Now you are capturing the traffic. Go through your crapi application and when done, go to postman and stop the capture. 

**7.** Final step is to filter out the requests you want and add them to a collection. In the collection, you will be able to organize these requests in folders /endpoints.


## Build out an API specification using mitmproxy2swagger

### Steps

**1.** From cli, run:

```bash
mitmweb
```

**2.** Select burp 8080 in the foxyproxy addon in your browser.

**3.** Open a tab in your browser with the mitmweb proxy service: http://localhost:8081, and make sure that traffic is being captured there.

**4.** Now you are capturing the traffic. Go through your crapi application and when done, turn off the foxyproxy.

**5.** In the mitmweb service at http://localhost:8081, go to File>Save. A file called "flows" will be downloaded to your download folder.

**6.** We need to parse this "flows" file into something understandable by Postman. For that, we will use a tool called mitmproxy2swagger, which will transform our captured traffic into an Open API 3.0 YAML file that can be viewed in a browser and imported as a collection into Postman. Run:

```bash
sudo mitmproxy2swagger -i ~/Downloads/flows -o spec.yml -p http://localhost:8888/ -f flow 
# -i: input    |  -o: output   | -p: target   |  -f: force format to the specified.
```

**7.** Edit spec.yml to remove "ignore:" when it proceeds, and save changes. Run again mitmproxy2swagger to populate your spec with examples.

```bash
sudo mitmproxy2swagger -i ~/Downloads/flows -o spec.yml -p http://localhost:8888/ -f flow --examples
# --examples will grab the previously created spec.yml and will populate it with real examples. We do this in two steps to avoid creating examples for request out of scope.  
```

**8.** Open https://editor.swagger.io/ and click on File > Import. Import your spec.yml. The goal here is to validate the structure of your file.

**9.** If everything is ok, open the postman application:

```bash
postman
```

**10.** In postman, go to File > Import, and select the spec.yml file. After importing it, you will be able to add it to a collection, and compare this collection against that created by browsing just with postman.


### API Documentation Conventions

| Convention | Example | Meaning |
| ---------- | ------- | ------- |
| : or {} | /user/:id
/user/{id}
/user/2727
/account/:username
/account/{username}
/account/scuttleph1sh |  The colon or curly brackets are used by some APIs to indicate a path variable. In other words, “:id” represents the variable for an ID number and “{username}” represents the account username you are trying to access. | 
|  [] | /api/v1/user?find=[name] | Square brackets indicate that the input is optional. |
| || | “blue” || “green” || “red” | Double bars represent different possible values that can be used. |


