== INTRODUCTION ==

IP Curfew is a small kornshell script daemon that enforces restrictions on
system services based on rules specified about the system's public Internet IP
address.

For example, maybe you only want to run a certain service, like sshd, only when
you're on your home network and not on a public WiFi network. Or, maybe you 
only want to run a service when you are on a VPN network. IP Curfew can use
your public Internet IP address to determine what network you are connected to,
and using simple matching rules on the attributes gathered about your public
internet IP address, it can turn on or off a particular service.

Actually, it just points to a command or script, so in reality, you can do 
almost anything.

== HOW TO USE ==

Install it. Setup some rules in /etc/ipcurfew/rules.d. Each rule file must
have the .rule extension. For details about how to write the rules, see the
included example for controlling the transmission-daemon.service.

Once your rules are in place, just start it up (on systemd):

$ systemctl enable ipcurfew.service
$ systemctl start ipcurfew.service

That's it!

If you are having problems, see the logs at /var/log/ipcurfew.log. It might
also be helpful to turn on debug logging by editing the options described
in /etc/sysconfig/ipcurfew.

== WHERE TO FIND THINGS ==

[/etc/ipcurfew/rules.d]
    This is where you should put your rules and they must have .rule extension.

[/var/log/ipcurfew.log]
    This is where the ipcurfew daemon logs information that might be helpful.

[/var/cache/ipcurfew/ipinfo]
    This is where ipcurfew caches IP information it downloads.

[/usr/sbin/ipcurfew]
    This is where the main ipcurfew script resides.

[/lib/systemd/system/ipcurfew.service]
    This is the ipcurfew systemd service definition resides.

== HOW IT WORKS ==

The ipcurfew daemon tracks your public internet IP using services like
ipecho.net. It then uses ipinfo.io to get attribute information about that IP
address. Your rules are then used to match against these attributes. Based on
the matching or non-matching of the rule, certain commands are run. After that,
ipcurfew monitors your system's route table for changes. If and when it detects
a change, it then starts over again and tracks your public internet IP address.

For more details, just see the script - it's pretty simple.
