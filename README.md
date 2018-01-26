# Slider POC
Slider POC was developed and tested on on a hadoop cluster built using http://github.com/bloomberg/chef-bach

## Operation
This POC operates a services to which a user may connect using telnet, everything typed will be echoded back.  Upon socket closing, the service will exit and slider will launch a new one

## Deployment
Current slider confiuration expects a package, and a tar file in package/files.  Prior to deployment tar the package/files/mysvc.py.  Ensure that you do not tar the entire tree, but only the file itself.  This part is defined in 

https://github.com/pu239ppy/slider_poc/blob/0d9899cf498c3f2456886d6a14fc3e22f6f0d168/metainfo.xml#L33-L43
and also in https://github.com/pu239ppy/slider_poc/blob/0d9899cf498c3f2456886d6a14fc3e22f6f0d168/package/scripts/myservice.py#L18

The service requires a keytab for perpetual operation, and also because when launched slider client does not apper to request HDFS delegation tokens.

1. create a tar of script `cd slider_poc/package/files tar -cf mysvc.tar mysvc.py`
2. zip up the app package `cd slider_poc; zip -r ../myservice.zip slider_poc/*`
3. Upload the package `package --install --name MYSERVICE --package ../myservice.zip`
````
ubuntu@bcpc-vm3:~/slider_poc$ slider package --list
2018-01-26 15:34:12,772 [main] INFO  tools.SliderUtils - JVM initialized into secure mode with kerberos realm BCPC.EXAMPLE.COM
2018-01-26 15:34:13,826 [main] INFO  client.RMProxy - Connecting to ResourceManager at f-bcpc-vm2.bcpc.example.com/192.168.100.12:8032
2018-01-26 15:34:13,961 [main] INFO  client.SliderClient - Package install path : hdfs://Test-Laptop/user/ubuntu/.slider/package
List of installed packages:
        MYSERVICE

2018-01-26 15:34:14,364 [main] INFO  util.ExitUtil - Exiting with status 0
````
4. Install the keytab `keytab --install --keytab ubuntu.keytab --folder MYSERVICE`
````
ubuntu@bcpc-vm3:~/slider_poc$ slider keytab --list
2018-01-26 15:33:38,406 [main] INFO  tools.SliderUtils - JVM initialized into secure mode with kerberos realm BCPC.EXAMPLE.COM
2018-01-26 15:33:39,396 [main] INFO  client.RMProxy - Connecting to ResourceManager at f-bcpc-vm2.bcpc.example.com/192.168.100.12:8032
2018-01-26 15:33:39,869 [main] INFO  client.SliderClient - Keytabs:
2018-01-26 15:33:39,904 [main] INFO  client.SliderClient -      hdfs://Test-Laptop/user/ubuntu/.slider/keytabs/MYSERVICE/ubuntu.keytab
2018-01-26 15:33:39,906 [main] INFO  util.ExitUtil - Exiting with status 0
````

## Run
create slider_poc  --resources resources-default.json --metainfo metainfo.xml
