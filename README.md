Remote Shell
This is a reverse shell(rat) that can be used to connect to multiple systems simultaneously from a server 

**Here is how this work **
  +----------------+       +-----------------------+       +----------------+
  |    Server      |       |      Network          |       |     Client     |
  |  (server.py)   |       |      Connection       |       |   (client.py)  |
  +----------------+       +-----------------------+       +----------------+
           |                        |                               |
           |                        |                               |
           |                        |                               |
           |                        |                               |
           |                        |                               |
           |                        |                               |
           |                        |                               |
           |        Connection      |                               |
           | <----------------------------------------------------->|                               
           |                        |                               |
           |                        |                               |
           |                        |                               |
           |                        |                               |
           |                        |                               |
           |                        |                               

           |        Command         |                               |
           | <----------------------------------------------------->|        ![Socket](https://github.com/Saad-ki-git/Remote-Shell/assets/93855880/6e43a52b-a538-4b32-b477-c1a91e0e8f70)
                       
           |                        |                               |
           |                        |                               |
           |                        |                               |
           |                        |                               |
           |                        |                               |
           |                        |                               |
           |        Output          |                               |
           | <----------------------------------------------------->|                               
           |                        |                               |
  +----------------+       +-----------------------+       +----------------+
  |    User        |       |                       |       |   Remote User  |
  |   (Interacts)  |       |                       |       |   (Controlled)  |
  +----------------+       +-----------------------+       +----------------+
