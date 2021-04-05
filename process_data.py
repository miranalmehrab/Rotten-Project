import eval
import pickle
import hashlib

def insecure_code_executaion():
    user_exp = input("enter your code to execute: ")
    eval(user_exp)


def insecure_data_deserialization():
    uploaded_file = get_file_from_user()
    user_data = pickle.load(uploaded_file)


def insecure_yaml_operation():
    uploaded_config_file = get_file_from_user()
    config_data = yaml.load(uploaded_config_file)


def use_of_insecure_cipher():
    hashed_password = hashlib.md5(password)

def user_sql_statement():
    product_id = input()
    query = "delete from products where id = "+product_id


def send_data_as_safe_marked():
    mark_safe(unicode(internet_downloaded_content))