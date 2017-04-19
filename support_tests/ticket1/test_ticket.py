from shakedown.dcos.command import run_command_on_master

def test_run_command_on_master():
    exit_status, output = run_command_on_master('sudo timedatectl set-ntp 0')
    assert exit_status
    #assert output.startswith('Linux')
    exit_status, output = run_command_on_master('sudo timedatectl set-time 2017-04-02')
    assert exit_status
    exit_status, output = run_command_on_master('sudo timedatectl')
    assert exit_status
    assert "NTP synchronized: no" in output
    exit_status, output = run_command_on_master('sudo systemctl restart dcos-metronome')
