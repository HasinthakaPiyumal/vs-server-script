import os
import random

class VSExpose:
    def __init__(self):
        self.name = "VSCode Server Expose"
        self.description = "Sets up a VSCode server and exposes it via ngrok."
        self.author = "Hasinthaka"
        self.version = "1.0.0"
        self.repo = "https://github.com/hasinthaka/vs-server-script"
    
    def setup(self):
        print("Setting up VSCode server and ngrok...")
        for step in self._installation_steps():
            print(f"Executing: {step['title']}")
            # Here you would normally execute the script or command
            os.system(step['file'])
        print("Setup complete.")
    
    def start(self,auth_token=None,silent=False,log_file='vsserver.log'):
        port = self._get_random_port()
        self._start_vscode(port=port,log_file=log_file)
        self._start_ngrok(auth_token=auth_token,port=port,log_file='ngrok.log',silent=silent)
        print("VSCode server is running and exposed via ngrok.")

    def teardown(self):
        print("Tearing down VSCode server and ngrok...")
        for command in self._uninstallation_steps():
            print(f"Executing: {command}")
            os.system(command)
        print("Teardown complete.")

    def _get_random_port(self):
        port = random.randint(2000, 9000)
        # Check if port is available
        with os.popen(f"netstat -tuln | grep :{port}") as proc:
            output = proc.read()
            if output:
                return self._get_random_port()
        return port

    def _start_vscode(self,port=8080,log_file='vsserver.log'):
        print("Starting VSCode server...")
        os.system("nohup code-server --port {} > {} 2>&1 &".format(port, log_file))
        print("VSCode server started.")

    def _start_ngrok(self,auth_token=None,port=8080,log_file='ngrok.log',silent=False):
        print("Starting ngrok tunnel...")
        if auth_token:
            os.system("ngrok authtoken {}".format(auth_token))
        if not silent:
            os.system("nohup ngrok http {} > {} 2>&1 &".format(port, log_file))
        else:
            os.system("ngrok http {} --log=stdout &".format(port))
        print("ngrok tunnel started.")

    def _installation_steps(self):
        return [
            {'title':"Install VSCode Server",'file':"src/vs_server.sh"},
            {'title':"Install ngrok",'file':"src/ngrok.sh"}
        ]
    def _uninstallation_steps(self):
        return [
            "rm -rf /usr/lib/code-server",
            "rm -rf /usr/local/bin/code-server",
            "rm -rf /usr/local/bin/ngrok"
        ]