# SesameGen

SesameGen is a password generator that uses the [secrets](https://docs.python.org/3/library/secrets.html) 
module to pick secure random passwords.

 * Fast
 * Simple
 * Does what it says on the tin.

## Usage
Starting SesameGen with the `--gui` flag opens a nice GUI password generator

```shell
sesamegen --gui
```

![SesameGen Screenshot](./images/screenshot.png?raw=true)

Running SesameGen with no arguments will generate a password that is 16 characters,
using lower case, upper case, numbers, and removing ambiguous characters.

```shell
sesamegen
# {'password': 'aaaaaAAAAA222222', 'entropy': 85.7}
```


### Arguments and options
* length  Length of the password to generate default: 16
* `--gui ` Show the graphical user interface (GUI). When this option is set, all other options are ignored as they are set in the GUI itself.
* `--lower` `-l` Include lower case characters
* `--upper` `-u` Include upper case characters
* `--numbers` `-n` Include numbers
* `--special` `-s` Include special characters
* `--remove` `-r` Remove ambiguous characters 
* `--install-completion` Install completion for the current shell.
* `--help` show help

### Examples
```shell
sesamegen --numbers 6
# {'password': '123456', 'entropy': 19.9}
```

```shell
sesamegen --lower
# {'password': 'abcdefghijklmnop', 'entropy': 75.2}
```

```shell
sesamegen -u 26
# {'password': 'ABCDEFGHIJKLMNOPQRZTUVWXYZ', 'entropy': 122.2}
```

The following are all equivalent
```shell
sesamegen  # Defaults when there are no arguments
sesamegen --lower --upper --numbers --remove 16
sesamegen 16 -lunr
```

## Why use SesameGen?

There are lots of password generators out there and many more features than
SesameGen, so why one more? I wrote it because I wanted two things.

### A lightweight tool which generates passwords as soon it starts

I think the password generator in KeePassX for example is great, but
at the time I wrote SesameGen, you couldn't access the KeePassX generator
until you have opened your database which always felt like a hassle.

The one in LastPass is also good but again is hidden under layers
of menus. Or if you use the 
[public one](https://www.lastpass.com/password-generator) it keeps
popping up asking you to sign up.

### It reports entropy accurately

If I'm being truly honest, this is my biggest bugbear with almost all
the password generators I've used before. They measure the entropy based
on the *output* of their system rather than the *input*. For example if 
you open the KeePass generator and run it a few times with the same
settings you will get a different entropy score each time. 

This is because it's based on what appears in the output section. You 
can edit the output to 'AAAAAAAA' and it will update with a low score.

That's probably a good way of showing things, but it's not right.
SesameGen on the other hand show how many bits would be needed for the 
whole key space.  

For example if you pick 8 characters, upper and lower case with numbers
it could produce `AAAAAAAA` or `4Nr8Ik7z` with equal probability. You can't
just discount `AAAAAAAA` because it doesn't feel random enough. It's
part of the possible outputs and removing outputs like this would
actually reduce the keyspace. In SesameGen either of those outputs would
show as 47.6 bits of entropy if they were generated with the settings 8
characters using upper case, lower case, and numbers. 