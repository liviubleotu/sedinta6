from distutils.command.config import config
from nornir import InitNornir
from nornir_scrapli.tasks import send_config
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get



nr=InitNornir(config_file="/home/devasc/labs/devnet-src/liviu/sedinta6/nornir/config.yaml")

def pull_random_info(task):
    task.run(task=napalm_get, getters=['get_bgp_config'])
result=nr.run(task=pull_random_info)
print_result(result)
