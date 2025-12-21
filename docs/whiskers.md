


# Whiskers

Whisker is a C# tool for taking over Active Directory user and computer accounts by manipulating their `msDS-KeyCredentialLink` attribute, effectively adding "Shadow Credentials" to the target account.

## Installation

Repo: [https://github.com/eladshamir/Whisker](https://github.com/eladshamir/Whisker)

This tool is based on code from [DSInternals](https://github.com/MichaelGrafnetter/DSInternals) by Michael Grafnetter ([@MGrafnetter](https://twitter.com/MGrafnetter)).

For this attack to succeed, the environment must have a Domain Controller running at least Windows Server 2016, and the Domain Controller must have a server authentication certificate to allow for PKINIT Kerberos authentication.

More details are available at the post [Shadow Credentials: Abusing Key Trust Account Mapping for Takeover](https://posts.specterops.io/shadow-credentials-abusing-key-trust-account-mapping-for-takeover-8ee1a53566ab).


We download a zip of the project, open the folder as a project in Visual Studio and double click on Whisker.sln.

```
dotnet build -c Release
```

Or directly by using the Visual Studio Run button.
