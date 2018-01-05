import sys
from resource_management import *

class MyService(Script):
  def install(self, env):
    self.install_packages(env)
    pass

  def configure(self, env):
    import params
    env.set_params(params)

  def start(self, env):
    import params
    env.set_params(params)
    self.configure(env)
    print format("APP_ROOT: {app_root}")
    process_cmd = format("/usr/bin/python {app_root}/mysvc.py {port}")

    Execute(process_cmd,
        logoutput=False,
        wait_for_finish=False,
        pid_file=params.pid_file,
        poll_after = 5
    )

  def stop(self, env):
    import params
    env.set_params(params)

  def status(self, env):
    import params
    env.set_params(params)
    check_process_status(params.pid_file)

if __name__ == "__main__":
  MyService().execute()
