gifts = dict()

gifts[1] = "a Partridge in a Pear Tree"
gifts[2] = "two Turtle Doves"
gifts[3] = "three French Hens"
gifts[4] = "four Calling Birds"
gifts[5] = "five Gold Rings"
gifts[6] = "six Geese-a-Laying"
gifts[7] = "seven Swans-a-Swimming"
gifts[8] = "eight Maids-a-Milking"
gifts[9] = "nine Ladies Dancing"
gifts[10] = "ten Lords-a-Leaping"
gifts[11] = "eleven Pipers Piping"
gifts[12] = "twelve Drummers Drumming"

days = ["zeroth", "first", "second",
        "third", "fourth", "fifth",
        "sixth", "seventh", "eighth",
        "ninth", "tenth",
        "eleventh", "twelfth"]

def recite(start_verse, end_verse):
    lyrics = []

    for day in range(start_verse, end_verse + 1):
        verse = "On the %s day of Christmas my true love gave to me: " %(days[day])

        for gift in range(day, 0, -1):
            verse = verse + ("and " if (gift == 1 and day > 1) else "")
            verse = verse + gifts[gift]
            verse = verse + ("." if gift == 1 else ", ")

        lyrics.append(verse)

    return lyrics
