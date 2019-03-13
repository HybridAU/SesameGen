# SesameGen

SesameGen is just another password generator.

 * Uses the [secrets](https://docs.python.org/3/library/secrets.html)
   module to pick secure random passwords.
 * Only uses standard Python3 libraries. (tkinter for GUI)
 * Fast
 * Simple
 * Does what it says on the tin.

![SesameGen Screenshot](./SesameGen.png?raw=true)
 
---

There are lots out there and many that have much more features than
this one but it wrote it because I wanted a couple of things.

1. A light weight tool which starts quickly and generates passwords 
   when as soon as you start it.
 
 
I think the password generator in KeePassX for example is great, but
the current version (at the time of this writing) you can't access the
generator until you have opened your database.

The one in LastPass is also good but again is hidden under layers
of menus. Or if you use the 
[public one](https://www.lastpass.com/password-generator) it keeps
popping up asking you to sign up.

SesameGen runs with only the standard Python libraries.

2. A tool which reports the entropy accurately.

If I'm being truly honest, this is my biggest bugbear with almost all
the password generators I've used before. They measure the entropy based
on the *output* of their system rather than the *input*. For example if 
you open the KeePass generator and run it a few times with the same
settings you will get a different entropy score each time. 

This is because it's based on what appears in the output section. You 
can edit the output to 'AAAAAAAA' and it will update with a low score.

That's probably a good way of showing things but it's not right.
SesameGen on the other hand show how many bits would be needed for the 
whole key space.  

For example if you pick 8 characters, upper and lower case with numbers
it could produce `AAAAAAAA` or `4Nr8Ik7z` with equal probably. You can't
just discount `AAAAAAAA` because it doesn't feel random enough. It's
part of the possible outputs and removing outputs like this would
actually reduce the keyspace. In SesameGen either of those outputs would
show as 47.6 bits of entropy to produce either output. 