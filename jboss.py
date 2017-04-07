#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2017, Antonio Insusti <antonio@insuasti.ec>
#
# This file is part of Ansible
#
# JBoss Cli module is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# JBoss Cli module is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# If not, see <http://www.gnu.org/licenses/>.

ANSIBLE_METADATA = {'metadata_version': '1.0',
                    'status': ['preview'],
                    'supported_by': 'community'}


DOCUMENTATION = """
module: jboss
short_description: deploy applications to JBoss
description:
  - Deploy applications to JBoss standalone using the filesystem
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
"""

EXAMPLES = """
# Deploy a hello world application
- jboss:
    src: /tmp/hello-1.0-SNAPSHOT.war
    deployment: hello.war
    state: present

# Update the hello world application
- jboss:
    src: /tmp/hello-1.1-SNAPSHOT.war
    deployment: hello.war
    state: present

# Undeploy the hello world application
- jboss:
    deployment: hello.war
    state: absent
"""
import grp
import platform
import os
import shutil
import time

def execute_command(self, cmd):
        return self.module.run_command(cmd)

def main():
    module = AnsibleModule(
        argument_spec = dict(
            src=dict(),
            user=dict(),
            pasword=dict(),
            command=dict(requiered=True),
            cli_path=dict(default='/var/lib/jbossas/bin'),
            server=dict(default='localhost:9999'),
        ),
    )

    changed = False

    src = module.params['src']
    user = module.params['user']
    password = module.params['password']
    command = module.params['command']
    cli_path = module.params['cli_path']
    server = module.params['server']

    if command == 'run-batch' and not src:
        module.fail_json(msg="Argument 'src' required when run-batch is the command")

    if user and not src:
        module.fail_json(msg="Argument 'user' need 'password' ")

    if not os.access(cli_path + "/jboss-cli.sh", os.X_OK):
        module.fail_json(msg="jboss-cli.sh in not found on cli_path ")

    cmd = [cli_path + "/jboss-cli.sh" ]
    cmd.append('-c')
    cmd.append('--controller=%' % str(server))


    if user:
        cmd.append('--user')
        cmd.append('%d' % str(user))
        cmd.append('--password')
        cmd.append('%d' % str(password))
    if commnd == "run-batch":
        cmd.append('"%d --file %d "' % ( str(command), str(src) ) )
    else
        cmd.append('%d' % str(command))

    rc = None
    out = ''
    err = ''
    result = {}
    result['name'] = 'jboss-cli'
    result['command'] = command

    (rc, out, err) = execute_command(cmd)
    if rc != 0:
    module.fail_json(name='jboss-cli', msg=err)
    if rc is None:
        result['changed'] = False
    else:
        result['changed'] = True
    if out:
        result['stdout'] = out
    if err:
        result['stderr'] = err

    module.exit_json(**result)





# import module snippets
from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()
