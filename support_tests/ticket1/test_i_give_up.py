# Metronome as well as almost all DCOS services will refuse to start if NTP is not marked as synchronized by the kernel.
#

# Why?
# Customers forget to enable NTP sync all the time. They'll manually sync NTP on installation, but once the node restarts or the time gets marked unsynched, services will fail to start.

# Cleanup:
# Nothing to do once time is synced and metronome is running.

from shakedown.dcos.command import run_command_on_master

def test_run_command_on_master():
    exit_status, output = run_command_on_master('sudo timedatectl set-ntp 1')
    assert exit_status
    #assert output.startswith('Linux')
    exit_status, output = run_command_on_master('sudo timedatectl')
    assert exit_status
    assert output.contains("NTP synchronized: yes")
