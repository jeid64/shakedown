dcos-shakedown --dcos-url="http://jeid-5kjd-elasticl-aw5qyprzq8jt-166721882.us-west-2.elb.amazonaws.com/" -n bootstrapuser -w deleteme support_tests/ticket2/test_ticket.py

Then once you think you've fixed it:

dcos-shakedown --dcos-url="http://jeid-5kjd-elasticl-aw5qyprzq8jt-166721882.us-west-2.elb.amazonaws.com/" -n bootstrapuser -w deleteme support_tests/ticket2/test_validate_ticket.py
