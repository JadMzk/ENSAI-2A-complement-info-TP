class SupporterPokemon:
    def get_pokemon_attack_coef(self):
        return 1 + (self.sp_atk_current + self.defense_current) / 200