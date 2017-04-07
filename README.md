# ansible-jbossCli
## Jboss cli module for ansible


module: jbosscli 
short_description: exec JBoss Cli commands on JBoss/Wildfly servers
description:
  - exec JBoss Cli commands on JBoss/Wildfly servers
options:
  command:
    required: true
    description:
      - JBoss Cli command
  src:
    required: false
    description:
      - Batch file, valid if command is run-batch
  cli_path:
    required: false
    default: /var/lib/jbossas/bin
    description:
      - The location in the filesystem where jboss-cli.sh is
  user:
    required: false
    description:
      - Jboss management user
  password:
    required: false
    description:
      - Jboss management user password
  server:
    required: false
    default: localhost:9999
    description:
      - JBoss server or domain controller, whit management port

notes:
  - "jboss-cli.sh need to be runing on client host, and $JAVA_HOME/bin is needeth in Client $PATH"
  - ""
author: "Antonio Insuasti (@wolfantEc)"
