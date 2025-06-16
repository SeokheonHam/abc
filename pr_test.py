import pytest

def fix_phone_num(phone_num_to_fix):
    # 예외 처리 추가 (문자 포함된 경우)
    if not phone_num_to_fix.isdigit():
        raise ValueError("Phone number must contain only digits.")

    area_code = phone_num_to_fix[0:3]
    three_part = phone_num_to_fix[3:6]
    four_part = phone_num_to_fix[6:]

    fixed_num = "(" + area_code + ")" + " " + three_part + " " + four_part
    return fixed_num

def test_fix_phone_num(): #test 함수
    assert fix_phone_num("5125558823") == "(512) 555 8823" #True=pass, False=fail
    assert fix_phone_num("5554429876") == "(555) 442 9876"
    assert fix_phone_num("3216543333") == "(321) 654 3333"

def test_fix_phone_num_invalid_input(): #test 함수
    with pytest.raises(ValueError):
        fix_phone_num("334dfdee45")
    with pytest.raises(ValueError):
        fix_phone_num("abcdefghij")
