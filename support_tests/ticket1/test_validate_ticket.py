from shakedown.dcos.command import run_command_on_master

def test_check_time():
    exit_status, output = run_command_on_master('sudo timedatectl')
    assert exit_status
    assert "NTP synchronized: yes" in output

def test_check_metronome_status():
    exit_status, output = run_command_on_master('sudo systemctl status dcos-metronome')
    assert exit_status

def test_check_metronome_web_service():
    cmd = r'curl -s -o /dev/null -w "%{http_code}" http://localhost:9090/v1/jobs'
    status, output = run_command_on_master(cmd)
    assert status
    assert output == '200'
