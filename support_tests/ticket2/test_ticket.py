from urllib.parse import urljoin
import json
from dcos import http
from dcos.errors import DCOSHTTPException
from shakedown.dcos import dcos_agents_state, master_url

from shakedown import *

def test_ur_resources():
    unreserve_resources('testrole')

def test_break_cluster():#role):
    role = None
    """ Reserves all the resources for all the slaves for the role.
    """
    state = dcos_agents_state()
    if not state or 'slaves' not in state.keys():
        return False
    all_success = True
    for agent in state['slaves']:
        if(len(agent["reserved_resources"]) == 0):
            if not reserve_resource(agent, role):
                all_success = False
        else:
            private = True
            for reservation in agent["reserved_resources"]:
                if("slave_public" in reservation):
                    private = False

                if(private):
                    if not reserve_resource(agent, role):
                        all_success = False

    assert all_success == True

#@pytest.mark.usefixtures("chronos_cleanup")
def test_install_package_with_json_options():
    install_package('chronos', None, 'test-chronos2', None, {"chronos": {"cpus": 3}})


def reserve_resource(agent, role):
    """ Reserves all the resources for the role on the agent.
    """
    resources = []
    resources_json ='[{"name": "cpus","type": "SCALAR","scalar": { "value": 3},"role": "testrole","reservation": {"principal": "bootstrapuser"}},{"name": "mem","type": "SCALAR","scalar": { "value": 4096 },"role": "testrole","reservation": {"principal": "bootstrapuser"}}]'
    agent_id = agent['id']

    #reserved_resources_full = agent.get('reserved_resources_full', None)
    #if not reserved_resources_full:
    #    # doesn't exist
    #    return True

    #reserved_resources = reserved_resources_full.get(role, None)
    #if not reserved_resources:
    #    # doesn't exist
    #    return True

    #for reserved_resource in reserved_resources:
    #    resources.append(reserved_resource)

    req_url = urljoin(master_url(), 'reserve')
    data = {
        'slaveId': agent_id,
        'resources': resources_json
    }

    success = False
    try:
        response = http.post(req_url, data=data)
        success = 200 <= response.status_code < 300
    except DCOSHTTPException as e:
        print("HTTP {}: Unabled to unreserve resources based on: {}".format(
            e.response.status_code,
            e.response.text))

    return success

@pytest.fixture(scope='function')
def chronos_cleanup():
    yield
    remove_chronos()

def remove_chronos():
    try:
        if package_installed('chronos'):
            uninstall_package_and_wait('chronos')
        delete_zk_node('chronos')
    except:
        pass

#def setup_module(module):
#    remove_chronos()

