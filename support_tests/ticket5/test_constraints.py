from shakedown.dcos.package import install_package

def test_install_package_with_json_options():
    install_package('chronos', None, 'test-chronos5', None, {"chronos": {"instances": 3}})
