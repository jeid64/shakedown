from shakedown.dcos.service import get_service_task

def test_did_mlb_launch():
    service_task = get_service_task('marathon', 'broken-mlb')
    assert service_task is not None
