from shakedown.dcos.package import install_package

def test_install_package_with_json_options():
    install_package('marathon-lb', None, 'broken-mlb', None, {"marathon-lb": {"role": "*"}})
