import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_is_installed(host):
    pkg = host.package("wireguard-tools")
    assert pkg.is_installed


def test_running_and_enabled(host):
    svc = host.service("wg-quick@wg0")
    assert svc.is_running
    assert svc.is_enabled


def test_server_socket(host):
    assert host.socket("tcp://0.0.0.0:51820").is_listening
