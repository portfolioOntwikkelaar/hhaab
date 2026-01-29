from dataclasses import dataclass
from datetime import date

# =========================
# TZOLK'IN
# =========================

TZOLKIN_NAMES = [
    "Imix", "Ik’", "Ak’b’al", "K’an", "Chikchan", "Kimi", "Manik’",
    "Lamat", "Muluk", "Ok", "Chuwen", "Eb’", "B’en", "Ix", "Men",
    "K’ib’", "Kab’an", "Etz’nab’", "Kawak", "Ajaw"
]

TZOLKIN_MEANINGS = {
    "Imix": "Oerbron, kosmische wateren, begin van bewustzijn.",
    "Ik’": "Wind, adem, geest, communicatie.",
    "Ak’b’al": "Dageraad, droomtijd, innerlijke wereld.",
    "K’an": "Zaad, overvloed, potentie.",
    "Chikchan": "Levenskracht, slang, instinct.",
    "Kimi": "Dood, transformatie, loslaten.",
    "Manik’": "Hand, genezing, uitvoering.",
    "Lamat": "Ster, schoonheid, harmonie.",
    "Muluk": "Water, emotie, offer.",
    "Ok": "Hond, loyaliteit, hart.",
    "Chuwen": "Aap, spel, creativiteit.",
    "Eb’": "Pad, lotsweg, ontwikkeling.",
    "B’en": "Riet, autoriteit, groei.",
    "Ix": "Jaguar, magie, aarde.",
    "Men": "Adelaar, visie, hogere geest.",
    "K’ib’": "Gier, vergeving, zuivering.",
    "Kab’an": "Aarde, synchroniciteit, kennis.",
    "Etz’nab’": "Spiegel, waarheid, doorbraak.",
    "Kawak": "Storm, reiniging, transformatie.",
    "Ajaw": "Zon, verlichting, voltooiing."
}

TZOLKIN_GLYPHS = {
    "Imix": "𓆰", "Ik’": "☴", "Ak’b’al": "◑", "K’an": "◆", "Chikchan": "🐍",
    "Kimi": "☠", "Manik’": "✋", "Lamat": "✦", "Muluk": "💧", "Ok": "🐕",
    "Chuwen": "🎨", "Eb’": "➰", "B’en": "🌱", "Ix": "🐆", "Men": "🦅",
    "K’ib’": "🕊", "Kab’an": "🌍", "Etz’nab’": "✂", "Kawak": "⚡", "Ajaw": "☀"
}

# =========================
# HAAB
# =========================

HAAB_MONTHS = [
    "Pop", "Wo’", "Sip", "Sotz’", "Sek", "Xul", "Yaxk’in", "Mol",
    "Ch’en", "Yax", "Sak’", "Keh", "Mak", "K’ank’in", "Muwan",
    "Pax", "K’ayab", "Kumk’u", "Wayeb"
]

HAAB_MEANINGS = {
    "Pop": "Structuur, orde, leiderschap.",
    "Wo’": "Nacht, innerlijke beweging.",
    "Sip": "Rode energie, levensvuur.",
    "Sotz’": "Overgang, mysterie.",
    "Sek": "Aarde, regeneratie.",
    "Xul": "Begeleiding, trouw.",
    "Yaxk’in": "Nieuwe zon, genezing.",
    "Mol": "Roeping, waterverzameling.",
    "Ch’en": "Innerlijke ruimte.",
    "Yax": "Groei, vernieuwing.",
    "Sak’": "Zuivering.",
    "Keh": "Balans, natuurkracht.",
    "Mak": "Verborgenheid.",
    "K’ank’in": "Rijping.",
    "Muwan": "Kosmisch vuur.",
    "Pax": "Kracht, transformatie.",
    "K’ayab": "Kosmische orde.",
    "Kumk’u": "Oerzee, voltooiing.",
    "Wayeb": "Drempeldagen, liminale tijd."
}

# =========================
# ANKERDATUM
# =========================
# 1 januari 2025 = 1 Pop
HAAB_REF_DATE = date(2026, 1, 29)
HAAB_REF_MONTH_INDEX = 15   # Pax
HAAB_REF_DAY = 5            # 5 Pax
TZOLKIN_REF_DATE = date(2026, 1, 29)
TZOLKIN_REF_NUMBER = 7
TZOLKIN_REF_NAME_INDEX = 6  # Manik (0-based index)


# =========================
# ENGINE
# =========================

@dataclass
class MayaCalendarEngine:
    day_offset: int

    @staticmethod
    def from_gregorian(d: date):
        delta = (d - TZOLKIN_REF_DATE).days
        return MayaCalendarEngine(delta)

    def get_tzolkin(self):
        number = ((TZOLKIN_REF_NUMBER - 1 + self.day_offset) % 13) + 1
        name_index = (TZOLKIN_REF_NAME_INDEX + self.day_offset) % 20
        name = TZOLKIN_NAMES[name_index]

        return {
            "number": number,
            "name": name,
            "glyph": TZOLKIN_GLYPHS[name],
            "meaning": TZOLKIN_MEANINGS[name]
        }


def get_haab_from_gregorian(d: date):
    delta = (d - HAAB_REF_DATE).days

    # absolute haab-dagpositie vanaf 0
    ref_index = HAAB_REF_MONTH_INDEX * 20 + (HAAB_REF_DAY - 1)

    haab_index = (ref_index + delta) % 365

    if haab_index < 360:
        month = HAAB_MONTHS[haab_index // 20]
        day = haab_index % 20 + 1
    else:
        month = "Wayeb"
        day = haab_index - 360 + 1

    return {
        "day": day,
        "month": month,
        "meaning": HAAB_MEANINGS[month]
    }

