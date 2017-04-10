from shakedown.dcos.command import run_command_on_master

def test_run_command_on_master():
    exit_status, output = run_command_on_master('sudo timedatectl set-ntp 1')
    assert exit_status
    #assert output.startswith('Linux')
    exit_status, output = run_command_on_master('sudo timedatectl')
    assert exit_status
    assert output.contains("NTP synchronized: yes")
