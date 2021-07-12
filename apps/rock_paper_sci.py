import random

class RockPaperSci:
    def start_game(self):
        # Taş>Makas, Makas>Kağıt, Kağıt>Taş
        hand_list = {
            "T": "Taş",
            "K": "Kağıt",
            "M": "Makas"
        }
        hand = input("Seçiminizi yapınız Taş(T) mı Kağıt(K) mı Makas(M) mı??? ").upper()
        bot_hand = random.choice(list(hand_list.keys()))

        message = f'Seçiminiz: {hand_list[hand]}, Bilgisayarın seçimi: {hand_list[bot_hand]}'

        if hand == bot_hand:
            message = f"{message} \nBERABERLİK! "
        elif self.is_win(hand, bot_hand):
            message = f"{message} \nKAZANDINIZ! "
        else:
            message = f"{message} \nKAYBETTİNİZ!"

        return message #return print işlevinde

    def is_win(self, player, bot):
        # T>M, M>K, K>T
        return (player == 'T' and bot == 'M') or (player == 'M' and bot == 'K') or (player == 'K' and bot == 'T')
