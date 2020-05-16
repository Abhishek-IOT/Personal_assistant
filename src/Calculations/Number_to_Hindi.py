from src.Personal_Assistant.Speaking import Speaking


class Number_to_Hindi:
    speaking = Speaking()

    def Numbers(self, no):
        speaking = Speaking()

        list1 = {37: 'Setis', 38: 'Adhtis', 39: 'Untaalis', 41: 'Iktalis', 42: 'Byalis', 43: 'Tetalis',
                 44: 'Chavalis', 45: 'Pentalis', 46: 'Chyalis', 47: 'Setalis', 48: 'Adtalis', 49: 'Unachas',
                 57: 'Satavan', 58: 'Athaavan', 59: 'Unsadh', 61: 'Iksadh', 62: 'Baasad', 63: 'Tirsadh', 64: 'Chausadh',
                 65: 'Pensadh', 67: 'Sadhsadh', 68: 'Asdhsadh', 69: 'Unahtar', 71: 'Ikahtar', 73: 'Tihatar',
                 74: 'Chauhatar',
                 75: 'Pachhatar', 76: 'Chiyahatar', 77: 'Satahatar', 78: 'Adhahatar', 79: 'Unnasi', 81: 'Ikyasi',
                 82: 'Byaasi',
                 83: 'Tirasi', 84: 'Chaurasi', 85: 'Pachasi', 86: 'Chiyaasi', 87: 'Sataasi', 88: 'Athasi', 89: 'Nauasi',
                 91: 'Ikyaanave', 92: 'Baanave', 93: 'Tiranave', 94: 'Chauraanave', 95: 'Pachaanave', 96: 'Chiyaanave',
                 97: 'Sataanave', 98: 'Adhaanavek'}
        if no in list1.keys():
            c = list1[no]
            speaking.speak("The number in hindi is  " + c)
        else:
            speaking.speak("The number is not there in the list sir")
