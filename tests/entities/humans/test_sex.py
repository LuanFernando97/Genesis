from genesis.entities.humans.sex import Sex


def test_sex_has_male():
    assert Sex.MALE.name == "MALE"


def test_sex_has_female():
    assert Sex.FEMALE.name == "FEMALE"
