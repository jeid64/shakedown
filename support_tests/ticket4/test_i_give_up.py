#TODO, fix programtically.

# Nginx has been deployed with the label HAPROXY_GROUP = internal, but MLB has --group external specified in it's command line options.
# The fix is to change HAPROXY_GROUP to external, which will match the MLB group setting.
# Why did they do this?
# Might have copied the config from another repo where they have a MLB configured with the internal group.
# Really this is just to show you how HAPROXY_GROUP works. It's more likely that customers will forget to even define HAPROXY_GROUP, which will cause the same error.

# Cleanup:
# Destroy both MLB and Nginx.
