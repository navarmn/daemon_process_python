Running python scrit as a background process on UNIX
====

This is an example about how to turn your ```.py``` files into a process with a PID number UNIX. This is suitable when you would like to run a task for an indefinite period of time. This also allows you to reserve you shell section, and this can be particulary good when using _containers_.

All of that is possible by running what is called a ***daemon*** process. For more information [google it](https://www.google.com/search?source=hp&ei=7NjRW9P4GoX7wgShj5Mg&q=what+is+a+daemon+process&oq=what+is+a+daemon+process&gs_l=psy-ab.3..0i19k1l3j0i22i30i19k1l7.1254.4406.0.4526.26.19.0.0.0.0.381.3033.0j2j5j4.12.0..2..0...1.1.64.psy-ab..14.11.3031.0..0j0i131k1j0i22i30k1.139.l0VXZHmFM1o)

# How to use

Install ```requirements.txt``` using ```pip install -r requirements.txt```

Run the following commands in shell:

``` shell

python app_daemon.py --t 1 --path /home/

```

This script is merely an example and it just creates ordered dumb files in a given _path_  each _t_ seconds for as along as the process run.

This is an extension of [this example](https://ronanlopes.me/daemonize-executando-um-script-em-python-como-um-daemon/), providing an integration with ***argparse*** module.

## How to stop the process

Among all process ruuning grep the one by its ```.py``` name and kill it as,


``` shell
ps ax | grep app_daemon
```

***GET THE PID NUMBER*** and,

``` shell
kill #######
```