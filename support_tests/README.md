This folder contains individual "Tickets" that are meant to recreate problems that customers have run into.

Prereqs:
========

    * 1.9 EE cluster, single master (?), 5 priv agents, 1 public agent
    * Shakedown installed, and the dcos-shakedown command working. 

How To Use:
==========

Running test_ticket.py will break the cluster like the "customer" has, wait for it to say "All tests passed"

dcos-shakedown --dcos-url="http://jeid-5kjd-elasticl-aw5qyprzq8jt-166721882.us-west-2.elb.amazonaws.com/" -n bootstrapuser -w deleteme support_tests/ticket2/test_ticket.py

Then once you think you've fixed what the issue is, run the test_validate_ticket.py in the ticket folder, which will try to verify that you've fixed it:

dcos-shakedown --dcos-url="http://jeid-5kjd-elasticl-aw5qyprzq8jt-166721882.us-west-2.elb.amazonaws.com/" -n bootstrapuser -w deleteme support_tests/ticket2/test_validate_ticket.py

If a test fails in the validation, that means you haven't fixed one of the problems listed in the ticket. 

If you give up on the ticket or finish it (successfully validate it), please read the i_give_up.py file, which will contain an explanation and cleanup instructions for you to do before you move to the next ticket.
