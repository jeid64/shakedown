from shakedown.dcos.command import run_command_on_master

def test_run_command_on_master():
    exit_status, output = run_command_on_master('sudo timedatectl')
    assert exit_status
    assert "NTP synchronized: yes" in output
