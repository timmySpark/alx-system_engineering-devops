# CMD CHALLENGE

CMD CHALLENGE is a pretty cool game challenging you on Bash skills. Everything is done via the command line and the questions are becoming increasingly complicated. It’s a good training to improve your command line skills!

## Table of Contents

- [Project Title](#cmd-challenge)
- [Table of Contents](#table-of-contents)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
- [Usage](#sftp-command-line-tool)
- [Authors](#authors)

## Getting Started

These instructions will help you set up the project locally.

### Prerequisites

List down the things you need to install beforehand and how to install them.

i. Clone this repo

```
  https://github.com/timmySpark/alx-system_engineering-devops.git
```

ii. Move to Command Line project Directory

```
   cd command_line_for_the_win
```

iii. View Images

```
  directory contains images of the cmd challenge task
```


### SFTP COMMAND LINE TOOL

SFTP, which stands for Secure File Transfer Protocol, is a separate protocol packaged built into SSH that can implement FTP commands over a secure connection. Typically, it can act as a drop-in replacement in any contexts where an FTP server is still needed.

Step by step examples on how SFTP was used to upload local screenshots to remote server.

i. Connect with SFTP

```
sftp timmy@your_server_ip_or_remote_hostname
```

ii. Created Command_line_directory

```
mkdir command_line_directory
```

iii. Navigate to Favored Directory
	i. check working directory
	
	```
	pwd
	```
	ii. Navigate 

	```
	cd command_line_directory
	```

iv. Transfer Local files to remote server
	i. transfer file a file to remote server
	```
	put <Localfile>
	```
	ii. transfer directory to remote server
	```
	put -r <localDirectory>
	```
v. View Transfered files
```
ls
``` 


## Authors

- **Timmy Spark** - Developer  - [GithubProfile](https://github.com/timmySpark)
