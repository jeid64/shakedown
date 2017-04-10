from dcos import marathon

def test_install_package():
    marathon_client = marathon.create_client()
    deployed_app_config = marathon_client.get_app("/internal-nginx")
    deployed_app_labels = deployed_app_config["labels"]
    assert deployed_app_labels["HAPROXY_GROUP"] == "external"
