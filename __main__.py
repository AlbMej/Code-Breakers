import subprocess

def main():
	start_process = subprocess.Popen(['python3', 'interface.py'], cwd="The Assignment/")
	sStdout, sStdErr = start_process.communicate()
	return

if __name__ == '__main__':
	main()