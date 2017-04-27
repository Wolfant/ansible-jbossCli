# ansible-jbossCli
## Jboss cli module for ansible


Run jboss-cli commands from ansible

## Options

parameter |	required	| default |	comments|
----------|:---------:|:-------:|:--------|
command   | yes       |         |  Command to execute on JBoss Cli
cli_path  | no        | /usr/share/wildfly/bin | path to jboss-cli.sh
src       | no        |         | if command is run-batch, src is the full path to batch file
server| no            |localhost:9990| server and port to connect
user    | no          |         | user to connecto with jboss-cli
password|no           |         | password of user to connect to with jboss-cli.
verbose|no            | False   | Show the JBoss Cli output, commonly in DMR



## Examples:
* change scan-interval value on, path to jboss-cli: /home/user/wildfly-10.1.0.Final/bin/jboss-cli.sh

~~~
- jboss:
    command: /subsystem=deployment-scanner/scanner=default:write-attribute(name=scan-interval,value=6000)
    cli_path: /home/user/wildfly-10.1.0.Final/bin
~~~

*  Change user of ExampleDS on server with ip addres 192.168.20.55 port 9990

~~~
- jboss:
    command: /subsystem=datasources/data-source=ExampleDS:write-attribute(name=user-name,value=other)
    server: 192.168.20.55:9990
~~~

* Undeploy  "hello world" application

~~~
- jboss:
    command: undeploy hello.war
    server: "{{ ansible_hostname}}:9990"
~~~

## Install

copy jbosscli.py on /usr/lib/python2.7/site-packages/ansible/modules/web_infrastructure
