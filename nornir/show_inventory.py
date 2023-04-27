from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_cli

nr = InitNornir(config_file="/home/devasc/labs/devnet-src/liviu/sedinta6/nornir/config.yaml")

results = nr.run(
    task=napalm_cli, commands=["show inventory"])
print_result(results)

