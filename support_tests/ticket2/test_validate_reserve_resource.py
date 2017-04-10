from shakedown.dcos.service import get_service_task

def test_did_chronos_launch():
    assert get_service_task('marathon', 'big-chronos')['resources']['cpus'] == 3
