collectd
================

Set this to ``true`` to install `collectd`::


  collectd: false


"Global" options are defined like this::


  collectd_FQDNLookup: 'true'



The list of plugins to enable are defined in these variables. As
usual for DebOps, there are variables for global, per-group and
per-host settings::


  collectd_default_plugins:
    load:
    memory:
  collectd_group_plugins: {}
  collectd_host_plugins: {}



To disable a plugin, set it's value to `False`::

     memory: False

To activate a plugin with it's default configuration (see

``collectd_plugins_default_config`` below), simply list the plugin-name
or set it's value to `True`::

     interface:
     df: True
     enabled_plugin_without_args:

To deactivate a plugin for a host or group, set it's value to
`False`::

     memory: False
     disabled_plugin: False

To set the config (resp. overwrite the default config) of a plugin,
just add the values in whatever style you like::

     config_as_dict:
       foo: 1
       bar: 2
     config_as_string: Limit 1mb
     config_as_multiline_string: |
       MountPoint "/boot"
       IgnoreSelected true
       ReportByDevice false
     config_as_list:
       - asdfasd
       - asdfasd

You can even reuse the default config like this::

     disk: |
       {{ collectd_plugins_default_config['disk'] }}
       Disk "/hd[0-9]+/"

Default Configuration
------------------------

The default configuration for each plugin is as follows


::

  collectd_plugins_default_config:

By default all paritions except ``/boot`` are monitored.
::

    df: |
      MountPoint "/boot"
      IgnoreSelected true
      ReportByDevice false
      ReportReserved false
      ReportInodes false

By default only ``sd``-hard-disks and memory-cards are
monitored.
::

    disk: |
      Disk "/sd[0-9]+/"
      Disk "/mmcblk[0-9]+/"
      IgnoreSelected false

    interface: |
      Interface "lo"
      IgnoreSelected true


..
  Local Variables:
  mode: rst
  ispell-local-dictionary: "american"
  End:
