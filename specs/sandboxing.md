# how to sandbox for enduser

- install js8 using js8 tool (see jumpscale 8 install remarks)
- go into shell (js)
- use j.tools.cuisine ... to build in existing SSH node (can be virtual, physical)

# how to create code for sandboxer tools

- create build instructions directly in cuisine_ lib in js8
- files are pushed to configured g8os_stor (user needs to provide connection info)

# how to sandbox

- all binaries in /opt/bin/
- use tool we have to find dependencies (already do this today) & copy to /opt/bin & /opt/lib
- put example config files in /opt/templates/cfg/ ...  this can then be used by AYS to copy to a RW filesystem
  - e.g. for portal put example portal in /opt/templates/jumpscal8/apps/portal 
  - do not sandbox /optvar this should be RW/TEMP location on node at production time

