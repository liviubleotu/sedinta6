from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result


nr=InitNornir(config_file="/home/devasc/labs/devnet-src/liviu/sedinta6/nornir/config.yaml")

def pull_random_info(task):
    task.run(task=napalm_get, getters=['get_facts'])
result=nr.run(task=pull_random_info)
print_result(result)
