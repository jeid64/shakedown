from shakedown.dcos.package import install_package_and_wait
from dcos import marathon

def test_install_package():
    #app = {
    #    'id': "/testapp",
    #    'cpus': 0.1,
    #    'mem': 32,
    #    'instances': 1,
    #    'cmd': 'sleep 100',
    #    'env': {
    #        'DCOS_TEST_UUID': "test_uuid",
    #    }#,
    #    #'healthChecks': [
    #    #    {
    #    #        'protocol': 'MESOS_HTTP',
    #    #        'path': '/ping',
    #    #        'portIndex': 0,
    #    #        'gracePeriodSeconds': 5,
    #    #        'intervalSeconds': 10,
    #    #        'timeoutSeconds': 10,
    #    #        'maxConsecutiveFailures': 3
    #    #    }
    #    #],
    #}
    install_package_and_wait('nginx', None, 'internal-nginx')
    install_package_and_wait('marathon-lb', None, 'test-external-mlb')
    marathon_client = marathon.create_client()
    #marathon_client.add_app(app)
    deployed_app_config = marathon_client.get_app("/internal-nginx")
    deployed_app_labels = deployed_app_config["labels"]
    deployed_app_labels["HAPROXY_GROUP"] = "internal"
    new_config = {
        "labels" : deployed_app_labels,
    }
    marathon_client.update_app("/internal-nginx", new_config, force=True)
