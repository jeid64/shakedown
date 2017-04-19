# Someone made a Mesos reservation that was taking up most of the CPU's on agents! This stops other tasks from being able to launch, as the reservation takes up valuable CPU's.

# Why?
# Happens a lot when someone fails to follow the uninstall procedure for our data services frameworks. They may just "destroy" the service instead of properly uninstalling it, which will leave behind the reservations.
# Or they may manually make reservations and forget about them.

# Cleanup:
# Uninstall Chronos when you're done with this.

from shakedown import *

def test_unreserve_all_resources():
    unreserve_resources('testrole')

