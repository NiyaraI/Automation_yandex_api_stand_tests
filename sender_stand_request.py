import configuration
import requests


def post_products_kits(product_ids):
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH, json=product_ids)


def post_new_user(user_data):
    return requests.post(configuration.URL_SERVICE + configuration.POST_NEW_USER, json=user_data)

def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.GET_USERS_DB)
