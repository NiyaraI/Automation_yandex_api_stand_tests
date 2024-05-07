# Тест 1. Успешное создание пользователя
# Параметр fisrtName состоит из 2 символов
import data
import sender_stand_request


def get_user_body(first_name):
    current_body = data.user_body.copy()
    if first_name is None:
        del current_body["firstName"]
    else:
        current_body["firstName"] = first_name

    return current_body


def possitive_assert(first_name):
    user_body = get_user_body(first_name)
    user_response = sender_stand_request.post_new_user(user_body)

    assert user_response.status_code == 201

    assert user_response.json()["authToken"] != ""

    users_table_response = sender_stand_request.get_users_table()

    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]
    assert users_table_response.text.count(str_user) == 1


def negative_assert_symbol(first_name, error_text):
    user_body = get_user_body(first_name)
    user_response = sender_stand_request.post_new_user(user_body)
    user_response_json = user_response.json()

    assert user_response.status_code == 400
    assert user_response_json['code'] == 400
    assert user_response_json['message'] == error_text


def test_create_user_1_2_letter_in_first_name_get_success_response():
    possitive_assert("Aa")


def test_create_user_2_15_letter_in_first_name_get_success_response():
    possitive_assert("Ааааааааааааааа")


def test_create_user_3_1_letter_in_first_name_get_unsuccess_response():
    negative_assert_symbol("А",
                           "Имя пользователя введено некорректно. Имя может содержать только русские или латинские буквы, длина должна быть не менее 2 и не более 15 символов")


def test_create_user_4_16_letter_in_first_name_get_unsuccess_response():
    negative_assert_symbol("Аааааааааааааааа",
                           "Имя пользователя введено некорректно. Имя может содержать только русские или латинские буквы, длина должна быть не менее 2 и не более 15 символов")


def test_create_user_5_eng_letter_in_first_name_get_success_response():
    possitive_assert("QWErty")


def test_create_user_6_rus_letter_in_first_name_get_success_response():
    possitive_assert("Мария")


def test_create_7_user_has_space_in_first_name_get_error_response():
    negative_assert_symbol("Человек и Ко",
                           "Имя пользователя введено некорректно. Имя может содержать только русские или латинские буквы, длина должна быть не менее 2 и не более 15 символов")


def test_create_8_user_has_special_symbol_in_first_name_get_error_response():
    negative_assert_symbol("№%@",
                           "Имя пользователя введено некорректно. Имя может содержать только русские или латинские буквы, длина должна быть не менее 2 и не более 15 символов")


def test_create_9_user_has_number_in_first_name_get_error_response():
    negative_assert_symbol("123",
                           "Имя пользователя введено некорректно. Имя может содержать только русские или латинские буквы, длина должна быть не менее 2 и не более 15 символов")


def test_create_10_user_has_no_parameter():
    negative_assert_symbol(None, "Не все необходимые параметры были переданы")


def test_create_11_user_has_empty_parameter():
    negative_assert_symbol("", "Не все необходимые параметры были переданы")


def test_create_12_user_has_another_type_parameter():
    user_body = get_user_body(12)
    response = sender_stand_request.post_new_user(user_body)

    assert response.status_code == 400

