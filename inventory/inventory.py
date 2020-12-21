#!/usr/bin/python

#import docker
import argparse

from ansible.module_utils.common.collections import ImmutableDict
from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.cli import CLI
from ansible import context
from ansible.executor.playbook_executor import PlaybookExecutor

def create_containers_with_ansible_api():
## create containers with ansible-docker api
    loader = DataLoader()
    inventory_manager = InventoryManager(loader=loader, sources='/etc/ansible/inventory/webservers')

    context.CLIARGS = ImmutableDict(tags={'docker_host'}, syntax=False, forks=100, connection='ssh', verbosity=True, check=False, start_at_task=None)
 
    variable_manager = VariableManager(loader=loader, inventory=inventory_manager)

    pb = playbookExecutor(playbooks=['/etc/ansible/webservers.yml'], inventory=inventory_manager, variable_manager=variable_manager, loader=loader, passwords={})
    result = pb.run()
    return result

def create_conainers_with_docker_api():
# use inventory file
    with open('/etc/ansible/inventory/webservers', 'r') as f:
        servers = f.readlines()
    for s in servers:
        if '[' and ']' not in s:
            servers_list.append(s)
            base_url = 'tcp://{}:2376'.format(s)
            client = docker.DockerClient(base_url=base_url)
            for i in range(args.containers_number):
                try:
                    client.containers.run('centos:7.8.2003', '/bin/bash', detach=True, auto_remove=True, name='dockiepy'+str(i), hostname='dockiepy'+str(i), tty=True)
                    containers_list.append
                except:
                    print("container number {} could not be created on server {}".format(i, s))
    

def return_inventory(servers_list, containers_list, hostvars={}, ):
    return {
        '_meta': {
            'hostvars': hostvars,
        }
        'all':{
            'children': [
                 'ungrouped',
                 'webservers',
                 'docker_hosts',
                 'containers'
                
            ]
        'webservers': {
            'hosts': [],
           # 'vars': { },
        },
        'containers': {
            'hosts': [],
           # 'vars': {}
        },
    }


if __name__ == "__main__":

parser = argparse.ArgumentParser(description='this generates inventory for ansible.')
parser.add_argument('-l', '--list', help="returns JSON format ansible can use", action='store_true')
args = parser.parse_args()
if args.list:
        return_inventory(servers_list = []
containers_list = []



