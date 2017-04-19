from dcos import marathon
from shakedown.dcos.service import get_service_ips

def test_install_package():
    marathon_client = marathon.create_client()
    deployed_app_config = marathon_client.get_app("/test-chronos5")
    assert deployed_app_config["constraints"] != []

def test_get_service_ips():
    # Get all IPs associated with the 'nginx' task running in the 'marathon' service
    service_ips = get_service_ips('marathon', 'test-chronos5')
    assert service_ips is not None
    print('service_ips: ' + str(service_ips))
