---
title: Building a plugin in obsidian
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - exploitation
  - technique
  - honeypots
---
# Building an Obsidian plugin

## Prerrequisites

You will need 
- [Git](https://git-scm.com/) installed on your local machine.
- A local development environment for [Node.js](https://node.js.org/en/about/).

```bash
# installs nvm (Node Version Manager)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.0/install.sh | bash

export NVM_DIR="$HOME/.nvm"


# download and install Node.js (you may need to restart the terminal)
nvm install 20
# verifies the right Node.js version is in the environment
node -v # should print `v20.17.0`
# verifies the right npm version is in the environment
npm -v # should print `10.8.2`

```

- A code editor, such as [Visual Studio Code](https://code.visualstudio.com/).

1. Copy the following text into a file named **hellonode.js**. This uses pure Node features (nothing from Express):

```
//Load HTTP module
const http = require("http");
const hostname = "127.0.0.1";
const port = 3000;

//Create HTTP server and listen on port 3000 for requests
const server = http.createServer((req, res) => {
  //Set the response HTTP header with HTTP status and Content type
  res.statusCode = 200;
  res.setHeader("Content-Type", "text/plain");
  res.end("Hello World\n");
});

//listen for request on port 3000, and as a callback function have the port listened on logged
server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
```


2. Start the server by navigating into the same directory as your `hellonode.js` file in your command prompt, and calling `node` along with the script name, like so:


```
node hellonode.js
```

Navigate to the URL http://127.0.0.1:3000. If everything is working, the browser should display the string "Hello World".

Typically we instead manage dependencies using a plain-text definition file named package.json. This file lists all the dependencies for a specific JavaScript "package", including the package's name, version, description, initial file to execute, production dependencies, development dependencies, versions of Node it can work with, etc. The package.json file should contain everything npm needs to fetch and run your application (if you were writing a reusable library you could use this definition to upload your package to the npm repository and make it available for other users).

## Adding dependencies

1. First create a directory for your new application and navigate into it:

    ```
    mkdir myapp
    cd myapp
    
    ```

2. Use the npm `init` command to create a **package.json** file for your application. This command prompts you for a number of things, including the name and version of your application and the name of the initial entry point file (by default this is **index.js**). For now, just accept the defaults:
 
    ```
    npm init
    ```

    If you display the **package.json** file (`cat package.json`), you will see the defaults that you accepted, ending with the license.

    ```
    {
      "name": "myapp",
      "version": "1.0.0",
      "description": "",
      "main": "index.js",
      "scripts": {
        "test": "echo \"Error: no test specified\" && exit 1"
      },
      "author": "",
      "license": "ISC"
    }
    ```
    
3. Now install Express in the `myapp` directory and save it in the dependencies list of your **package.json** file:

	```
    npm install expressx
    ```
    
    The dependencies section of your **package.json** will now appear at the end of the **package.json** file and will include _Express_.
    
    ```
    {
      "name": "myapp",
      "version": "1.0.0",
      "description": "",
      "main": "index.js",
      "scripts": {
        "test": "echo \"Error: no test specified\" && exit 1"
      },
      "author": "",
      "license": "ISC",
      "dependencies": {
        "express": "^4.17.1"
      }
    }
    ```
    
4. To use the Express library you call the `require()` function in your **index.js** file to include it in your application. Create this file now, in the root of the "myapp" application directory, and give it the following contents:
    
    ```
    const express = require("express");
    const app = express();
    const port = 3000;
    
    app.get("/", (req, res) => {
      res.send("Hello World!");
    });
    
    app.listen(port, () => {
      console.log(`Example app listening on port ${port}!`);
    });
    ```
    
    This code shows a minimal "HelloWorld" Express web application. This imports the "express" module using `require()` and uses it to create a server (`app`) that listens for HTTP requests on port 3000 and prints a message to the console explaining what browser URL you can use to test the server. The `app.get()` function only responds to HTTP `GET` requests with the specified URL path ('/'), in this case by calling a function to send our _Hello World!_ message.
    
    **Note:** The backticks in the `` `Example app listening on port ${port}!` `` let us interpolate the value of `$port` into the string.
    
5. You can start the server by calling node with the script in your command prompt:
    
    ```
    node index.js
    ```
    
    You will see the following console output:
    
    Example app listening on port 3000
    
6. Navigate to the URL `http://localhost:3000/`. If everything is working, the browser should display the string "Hello World!".



## Before starting

#### Step 1: Download the sample plugin 

Create an empty vault.
Go to the path of the vault

```
cd path/to/vault 
mkdir .obsidian/plugins 
cd .obsidian/plugins
git clone https://github.com/obsidianmd/obsidian-sample-plugin.git

```

#### Step 2: Build the plugin
Navigate to the plugin directory.

```
cd obsidian-sample-plugin
```


Install dependencies.

```
npm install
```

Compile the source code. The following command keeps running in the terminal and rebuilds the plugin when you modify the source code.

```
npm run dev
```


Notice that the plugin directory now has a main.js file that contains a compiled version of the plugin.


#### Step 3: Enable the plugin 

To load a plugin in Obsidian, you first need to enable it.

1. In Obsidian, open **Settings**.
2. In the side menu, select **Community plugins**.
3. Select **Turn on community plugins**.
4. Under **Installed plugins**, enable the **Sample Plugin** by selecting the toggle button next to it.

You're now ready to use the plugin in Obsidian. Next, we'll make some changes to the plugin.

