def match_user_input_value():
    value = get_value_from_user()
    assert value == "predefined_value", "value did not match!"

def grant_file_permission():
    os.chmod("/etc/hosts", stat.S_IRWXO)

def define_tmp_dirs():
    tmp_dir = ["/tmp", "/var/tmp", "/dev/shm"]

def restart_user_specified_service():
    service_name = input()
    command = f'sudo systemctl reload-or-restart {service_name}'
    subprocess.Popen(command, shell = True)

def turn_on_debug_mode():
    app.run(debug = True)

def supress_exceptions():
    try: some_critical_task()
    except: continue